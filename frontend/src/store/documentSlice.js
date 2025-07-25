import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const initialState = {
  documents: [],
  currentDocument: null,
  uploadProgress: 0,
  isLoading: false,
  isUploading: false,
  error: null,
};

// Async thunks
export const uploadDocument = createAsyncThunk(
  'documents/upload',
  async ({ file, projectId, onUploadProgress }, { rejectWithValue }) => {
    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await axios.post(
        `${API_URL}/api/documents/upload?project_id=${projectId}`,
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
          onUploadProgress: (progressEvent) => {
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            onUploadProgress && onUploadProgress(percentCompleted);
          },
        }
      );

      return response.data;
    } catch (error) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to upload document');
    }
  }
);

export const fetchDocuments = createAsyncThunk(
  'documents/fetchAll',
  async (projectId, { rejectWithValue }) => {
    try {
      const url = projectId 
        ? `${API_URL}/api/documents?project_id=${projectId}`
        : `${API_URL}/api/documents`;
      const response = await axios.get(url);
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to fetch documents');
    }
  }
);

export const fetchDocument = createAsyncThunk(
  'documents/fetchOne',
  async (documentId, { rejectWithValue }) => {
    try {
      const response = await axios.get(`${API_URL}/api/documents/${documentId}`);
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to fetch document');
    }
  }
);

export const downloadDocument = createAsyncThunk(
  'documents/download',
  async ({ documentId, format }, { rejectWithValue }) => {
    try {
      const response = await axios.get(
        `${API_URL}/api/documents/${documentId}/download/${format}`,
        {
          responseType: 'blob',
        }
      );

      // Create download link
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `document.${format}`);
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);

      return { documentId, format };
    } catch (error) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to download document');
    }
  }
);

export const deleteDocument = createAsyncThunk(
  'documents/delete',
  async (documentId, { rejectWithValue }) => {
    try {
      await axios.delete(`${API_URL}/api/documents/${documentId}`);
      return documentId;
    } catch (error) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to delete document');
    }
  }
);

const documentSlice = createSlice({
  name: 'documents',
  initialState,
  reducers: {
    clearError: (state) => {
      state.error = null;
    },
    setUploadProgress: (state, action) => {
      state.uploadProgress = action.payload;
    },
    updateDocumentStatus: (state, action) => {
      const { documentId, status } = action.payload;
      const document = state.documents.find(d => d.id === documentId);
      if (document) {
        document.status = status;
      }
      if (state.currentDocument?.id === documentId) {
        state.currentDocument.status = status;
      }
    },
  },
  extraReducers: (builder) => {
    builder
      // Upload document
      .addCase(uploadDocument.pending, (state) => {
        state.isUploading = true;
        state.error = null;
        state.uploadProgress = 0;
      })
      .addCase(uploadDocument.fulfilled, (state, action) => {
        state.isUploading = false;
        state.documents.push(action.payload);
        state.uploadProgress = 100;
      })
      .addCase(uploadDocument.rejected, (state, action) => {
        state.isUploading = false;
        state.error = action.payload;
        state.uploadProgress = 0;
      })
      // Fetch documents
      .addCase(fetchDocuments.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(fetchDocuments.fulfilled, (state, action) => {
        state.isLoading = false;
        // Ensure we always have an array
        state.documents = Array.isArray(action.payload) ? action.payload : [];
      })
      .addCase(fetchDocuments.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload;
      })
      // Fetch single document
      .addCase(fetchDocument.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(fetchDocument.fulfilled, (state, action) => {
        state.isLoading = false;
        state.currentDocument = action.payload;
      })
      .addCase(fetchDocument.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload;
      })
      // Delete document
      .addCase(deleteDocument.fulfilled, (state, action) => {
        state.documents = state.documents.filter(d => d.id !== action.payload);
        if (state.currentDocument?.id === action.payload) {
          state.currentDocument = null;
        }
      });
  },
});

export const { clearError, setUploadProgress, updateDocumentStatus } = documentSlice.actions;

export default documentSlice.reducer;

// Selectors
export const selectDocuments = (state) => state.documents.documents;
export const selectCurrentDocument = (state) => state.documents.currentDocument;
export const selectUploadProgress = (state) => state.documents.uploadProgress;
export const selectIsUploading = (state) => state.documents.isUploading;