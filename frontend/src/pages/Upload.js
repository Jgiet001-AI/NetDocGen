import React, { useState, useCallback, useEffect } from 'react';
import { useDropzone } from 'react-dropzone';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { 
  FiUploadCloud, 
  FiFile, 
  FiX, 
  FiCheckCircle,
  FiAlertCircle
} from 'react-icons/fi';
import toast from 'react-hot-toast';

import Layout from '../components/layout/Layout';
import { fetchProjects, selectProjects } from '../store/projectSlice';
import { uploadDocument, setUploadProgress } from '../store/documentSlice';
import PreUploadChecklist from '../components/upload/PreUploadChecklist';
import InteractiveHelper from '../components/upload/InteractiveHelper';

const Upload = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  
  const projects = useSelector(selectProjects);
  const uploadProgress = useSelector(state => state.documents.uploadProgress);
  const isUploading = useSelector(state => state.documents.isUploading);
  
  const [selectedProject, setSelectedProject] = useState(searchParams.get('project') || '');
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState(null); // 'success' | 'error' | null
  const [showChecklist, setShowChecklist] = useState(true);
  const [checklistCompleted, setChecklistCompleted] = useState(false);
  const [checklistData, setChecklistData] = useState({});
  const [showHelper, setShowHelper] = useState(false);
  const [uploadedDocumentId, setUploadedDocumentId] = useState(null);

  useEffect(() => {
    dispatch(fetchProjects());
  }, [dispatch]);

  const onDrop = useCallback((acceptedFiles, rejectedFiles) => {
    if (rejectedFiles.length > 0) {
      toast.error('Please upload only .vsd, .vsdx, or .vsdm files');
      return;
    }

    if (acceptedFiles.length > 0) {
      setSelectedFile(acceptedFiles[0]);
      setUploadStatus(null);
      dispatch(setUploadProgress(0));
    }
  }, [dispatch]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/vnd.visio': ['.vsd'],
      'application/vnd.ms-visio.drawing': ['.vsdx'],
      'application/vnd.ms-visio.drawing.macroenabled.12': ['.vsdm']
    },
    maxFiles: 1,
    multiple: false
  });

  const handleUpload = async () => {
    if (!selectedFile) {
      toast.error('Please select a file');
      return;
    }

    if (!selectedProject) {
      toast.error('Please select a project');
      return;
    }

    try {
      const result = await dispatch(uploadDocument({
        file: selectedFile,
        projectId: selectedProject,
        onUploadProgress: (progress) => {
          dispatch(setUploadProgress(progress));
        }
      }));

      if (uploadDocument.fulfilled.match(result)) {
        setUploadStatus('success');
        toast.success('File uploaded successfully! Processing will begin shortly.');
        setUploadedDocumentId(result.payload.id);
        
        // Show interactive helper to gather additional information
        setShowHelper(true);
      } else {
        setUploadStatus('error');
        toast.error('Upload failed. Please try again.');
      }
    } catch (error) {
      setUploadStatus('error');
      toast.error('Upload failed. Please try again.');
    }
  };

  const removeFile = () => {
    setSelectedFile(null);
    setUploadStatus(null);
    dispatch(setUploadProgress(0));
  };

  const handleChecklistComplete = (checkedItems) => {
    setChecklistData(checkedItems);
    setChecklistCompleted(true);
    setShowChecklist(false);
    toast.success('Checklist completed! You can now upload your diagram.');
  };

  const handleChecklistSkip = () => {
    setShowChecklist(false);
    toast.success('Checklist skipped. The AI will help fill in missing information.');
  };

  const handleHelperComplete = (answers, files) => {
    toast.success('Additional information saved successfully!');
    // Navigate to document detail
    navigate(`/documents/${uploadedDocumentId}`);
  };

  // Show interactive helper after successful upload
  if (showHelper && uploadedDocumentId) {
    return (
      <Layout>
        <InteractiveHelper
          documentId={uploadedDocumentId}
          missingInfo={[]} // Will be populated by backend analysis
          onComplete={handleHelperComplete}
        />
      </Layout>
    );
  }

  // Show checklist first
  if (showChecklist) {
    return (
      <Layout>
        <PreUploadChecklist
          onComplete={handleChecklistComplete}
          onSkip={handleChecklistSkip}
        />
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="max-w-3xl mx-auto">
        <div className="space-y-6">
          {/* Header */}
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Upload Visio Diagram</h1>
            <p className="mt-2 text-gray-600">
              Upload your network diagram to generate documentation
            </p>
            {checklistCompleted && (
              <div className="mt-3 flex items-center text-sm text-green-600">
                <FiCheckCircle className="mr-2" />
                Pre-upload checklist completed
              </div>
            )}
          </div>

          {/* Project Selection */}
          <div className="bg-white shadow rounded-lg border border-gray-200 p-6">
            <label htmlFor="project" className="block text-sm font-medium text-gray-700">
              Select Project
            </label>
            <select
              id="project"
              value={selectedProject}
              onChange={(e) => setSelectedProject(e.target.value)}
              className="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm rounded-md"
              disabled={isUploading}
            >
              <option value="">Choose a project...</option>
              {Array.isArray(projects) && projects.map((project) => (
                <option key={project.id} value={project.id}>
                  {project.name}
                </option>
              ))}
            </select>
            
            {(!Array.isArray(projects) || projects.length === 0) && (
              <p className="mt-2 text-sm text-gray-500">
                No projects found.{' '}
                <button
                  onClick={() => navigate('/projects/new')}
                  className="text-primary-600 hover:text-primary-700"
                >
                  Create one first
                </button>
              </p>
            )}
          </div>

          {/* Upload Area */}
          <div className="bg-white shadow rounded-lg border border-gray-200 p-6">
            {!selectedFile ? (
              <div
                {...getRootProps()}
                className={`border-2 border-dashed rounded-lg p-12 text-center cursor-pointer transition-colors ${
                  isDragActive
                    ? 'border-primary-500 bg-primary-50'
                    : 'border-gray-300 hover:border-gray-400'
                }`}
              >
                <input {...getInputProps()} />
                <FiUploadCloud className="mx-auto h-12 w-12 text-gray-400" />
                <p className="mt-2 text-sm text-gray-600">
                  {isDragActive
                    ? 'Drop the file here...'
                    : 'Drag and drop your Visio file here, or click to select'}
                </p>
                <p className="mt-1 text-xs text-gray-500">
                  Supported formats: .vsd, .vsdx, .vsdm (Max size: 50MB)
                </p>
              </div>
            ) : (
              <div className="space-y-4">
                {/* File Info */}
                <div className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
                  <div className="flex items-center">
                    <FiFile className="h-8 w-8 text-gray-400" />
                    <div className="ml-3">
                      <p className="text-sm font-medium text-gray-900">
                        {selectedFile.name}
                      </p>
                      <p className="text-sm text-gray-500">
                        {(selectedFile.size / 1024 / 1024).toFixed(2)} MB
                      </p>
                    </div>
                  </div>
                  
                  {!isUploading && (
                    <button
                      onClick={removeFile}
                      className="text-gray-400 hover:text-gray-600"
                    >
                      <FiX className="h-5 w-5" />
                    </button>
                  )}
                </div>

                {/* Upload Progress */}
                {(isUploading || uploadProgress > 0) && (
                  <div>
                    <div className="flex justify-between text-sm text-gray-600 mb-1">
                      <span>Uploading...</span>
                      <span>{uploadProgress}%</span>
                    </div>
                    <div className="w-full bg-gray-200 rounded-full h-2">
                      <div
                        className="bg-primary-600 h-2 rounded-full transition-all duration-300"
                        style={{ width: `${uploadProgress}%` }}
                      />
                    </div>
                  </div>
                )}

                {/* Upload Status */}
                {uploadStatus === 'success' && (
                  <div className="flex items-center p-4 bg-green-50 rounded-lg">
                    <FiCheckCircle className="h-5 w-5 text-green-500" />
                    <p className="ml-2 text-sm text-green-800">
                      Upload successful! Redirecting to document...
                    </p>
                  </div>
                )}

                {uploadStatus === 'error' && (
                  <div className="flex items-center p-4 bg-red-50 rounded-lg">
                    <FiAlertCircle className="h-5 w-5 text-red-500" />
                    <p className="ml-2 text-sm text-red-800">
                      Upload failed. Please try again.
                    </p>
                  </div>
                )}
              </div>
            )}
          </div>

          {/* Actions */}
          <div className="flex justify-end space-x-3">
            <button
              onClick={() => navigate(-1)}
              className="px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
              disabled={isUploading}
            >
              Cancel
            </button>
            <button
              onClick={handleUpload}
              disabled={!selectedFile || !selectedProject || isUploading}
              className="px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isUploading ? 'Uploading...' : 'Upload and Process'}
            </button>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default Upload;