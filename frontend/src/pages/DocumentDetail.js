import React, { useEffect, useState } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { 
  FiArrowLeft, 
  FiDownload,
  FiTrash2,
  FiClock,
  FiCheckCircle,
  FiAlertCircle,
  FiRefreshCw,
  FiFileText,
  FiFolder,
  FiCalendar,
  FiFile
} from 'react-icons/fi';
import { format } from 'date-fns';
import toast from 'react-hot-toast';

import Layout from '../components/layout/Layout';
import { 
  fetchDocument, 
  deleteDocument, 
  downloadDocument,
  selectCurrentDocument 
} from '../store/documentSlice';
import { fetchProjects, selectProjects } from '../store/projectSlice';

const DocumentDetail = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  
  const document = useSelector(selectCurrentDocument);
  const projects = useSelector(selectProjects);
  const isLoading = useSelector(state => state.documents.isLoading);
  
  const [downloadingFormat, setDownloadingFormat] = useState(null);
  const [processingProgress, setProcessingProgress] = useState(0);

  useEffect(() => {
    dispatch(fetchDocument(id));
    dispatch(fetchProjects());
    
    // Poll for status updates if processing
    const interval = setInterval(() => {
      if (document?.status === 'UPLOADED' || 
          document?.status === 'PARSING' || 
          document?.status === 'PARSED' ||
          document?.status === 'GENERATING') {
        dispatch(fetchDocument(id));
        // Update progress based on status
        if (document?.status === 'UPLOADED') {
          setProcessingProgress(10);
        } else if (document?.status === 'PARSING') {
          setProcessingProgress(prev => Math.min(prev + 5, 50));
        } else if (document?.status === 'PARSED') {
          setProcessingProgress(60);
        } else if (document?.status === 'GENERATING') {
          setProcessingProgress(prev => Math.min(prev + 5, 90));
        }
      }
    }, 2000);
    
    return () => clearInterval(interval);
  }, [dispatch, id, document?.status]);

  // Update progress based on status
  useEffect(() => {
    if (document?.status === 'COMPLETED') {
      setProcessingProgress(100);
    } else if (document?.status === 'FAILED') {
      setProcessingProgress(0);
    } else if (document?.status === 'UPLOADED') {
      setProcessingProgress(10);
    } else if (document?.status === 'PARSING') {
      setProcessingProgress(30);
    } else if (document?.status === 'PARSED') {
      setProcessingProgress(60);
    } else if (document?.status === 'GENERATING') {
      setProcessingProgress(80);
    }
  }, [document?.status]);

  const getStatusIcon = (status) => {
    switch (status) {
      case 'COMPLETED':
        return <FiCheckCircle className="h-8 w-8 text-green-500" />;
      case 'UPLOADED':
      case 'PARSING':
      case 'PARSED':
      case 'GENERATING':
        return <FiClock className="h-8 w-8 text-yellow-500 animate-spin" />;
      case 'FAILED':
        return <FiAlertCircle className="h-8 w-8 text-red-500" />;
      default:
        return <FiClock className="h-8 w-8 text-gray-400" />;
    }
  };

  const getStatusText = (status) => {
    switch (status) {
      case 'COMPLETED':
        return 'Processing Complete';
      case 'UPLOADED':
        return 'File Uploaded';
      case 'PARSING':
        return 'Parsing Visio File...';
      case 'PARSED':
        return 'File Parsed Successfully';
      case 'GENERATING':
        return 'Generating Documentation...';
      case 'FAILED':
        return 'Processing Failed';
      default:
        return status || 'Unknown';
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'COMPLETED':
        return 'text-green-600 bg-green-50';
      case 'UPLOADED':
      case 'PARSING':
      case 'PARSED':
      case 'GENERATING':
        return 'text-yellow-600 bg-yellow-50';
      case 'FAILED':
        return 'text-red-600 bg-red-50';
      default:
        return 'text-gray-600 bg-gray-50';
    }
  };

  const handleDownload = async (format) => {
    setDownloadingFormat(format);
    try {
      await dispatch(downloadDocument({ documentId: id, format }));
      toast.success(`Downloaded ${format.toUpperCase()} document`);
    } catch (error) {
      toast.error('Download failed');
    } finally {
      setDownloadingFormat(null);
    }
  };

  const handleDelete = async () => {
    if (window.confirm('Are you sure you want to delete this document? This action cannot be undone.')) {
      const result = await dispatch(deleteDocument(id));
      if (deleteDocument.fulfilled.match(result)) {
        toast.success('Document deleted successfully');
        navigate('/documents');
      }
    }
  };

  const getProjectName = () => {
    const project = projects.find(p => p.id === document?.project_id);
    return project ? project.name : 'Unknown Project';
  };

  if (isLoading || !document) {
    return (
      <Layout>
        <div className="flex justify-center items-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
        </div>
      </Layout>
    );
  }

  const downloadFormats = [
    { id: 'html', name: 'HTML', icon: '🌐', description: 'Interactive web page' },
    { id: 'pdf', name: 'PDF', icon: '📄', description: 'Printable document' },
    { id: 'docx', name: 'Word', icon: '📝', description: 'Editable document' },
    { id: 'markdown', name: 'Markdown', icon: '📋', description: 'Plain text format' }
  ];

  return (
    <Layout>
      <div className="space-y-6">
        {/* Header */}
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <Link
              to="/documents"
              className="text-gray-400 hover:text-gray-600"
            >
              <FiArrowLeft className="h-6 w-6" />
            </Link>
            <div>
              <h1 className="text-3xl font-bold text-gray-900">{document.filename}</h1>
              <p className="mt-1 text-gray-600">Document Details</p>
            </div>
          </div>
          
          <div className="flex items-center space-x-3">
            {document.status === 'processing' && (
              <button
                onClick={() => dispatch(fetchDocument(id))}
                className="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
              >
                <FiRefreshCw className="mr-2 h-4 w-4" />
                Refresh
              </button>
            )}
            <button
              onClick={handleDelete}
              className="inline-flex items-center px-4 py-2 border border-red-300 shadow-sm text-sm font-medium rounded-md text-red-700 bg-white hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
            >
              <FiTrash2 className="mr-2 h-4 w-4" />
              Delete
            </button>
          </div>
        </div>

        {/* Status Card */}
        <div className={`rounded-lg p-6 ${getStatusColor(document.status)}`}>
          <div className="flex items-center">
            {getStatusIcon(document.status)}
            <div className="ml-4">
              <h2 className="text-xl font-semibold">{getStatusText(document.status)}</h2>
              {(document.status === 'processing' || document.status === 'parsing') && (
                <div className="mt-2">
                  <p className="text-sm mb-2">
                    Your document is being processed. This may take a few minutes...
                  </p>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div 
                      className="bg-blue-600 h-2 rounded-full transition-all duration-500"
                      style={{ width: `${processingProgress}%` }}
                    />
                  </div>
                  <p className="mt-1 text-xs">{processingProgress}% complete</p>
                </div>
              )}
              {document.status === 'completed' && (
                <p className="mt-1 text-sm">
                  Your document has been processed successfully and is ready for download.
                </p>
              )}
              {document.status === 'failed' && (
                <div className="mt-2">
                  <p className="text-sm font-semibold text-red-700">Error Details:</p>
                  <p className="mt-1 text-sm text-red-600">
                    {document.error_message || document.error || 'An error occurred while processing your document.'}
                  </p>
                  <div className="mt-3">
                    <button
                      onClick={() => dispatch(fetchDocument(id))}
                      className="text-sm text-primary-600 hover:text-primary-700 underline"
                    >
                      Retry Processing
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Document Info */}
        <div className="bg-white shadow rounded-lg border border-gray-200 p-6">
          <h3 className="text-lg font-medium text-gray-900 mb-4">Document Information</h3>
          <dl className="grid grid-cols-1 gap-x-4 gap-y-6 sm:grid-cols-2">
            <div>
              <dt className="text-sm font-medium text-gray-500 flex items-center">
                <FiFile className="mr-2 h-4 w-4" />
                Filename
              </dt>
              <dd className="mt-1 text-sm text-gray-900">{document.filename}</dd>
            </div>
            <div>
              <dt className="text-sm font-medium text-gray-500 flex items-center">
                <FiFolder className="mr-2 h-4 w-4" />
                Project
              </dt>
              <dd className="mt-1 text-sm text-gray-900">
                <Link 
                  to={`/projects/${document.project_id}`}
                  className="text-primary-600 hover:text-primary-700"
                >
                  {getProjectName()}
                </Link>
              </dd>
            </div>
            <div>
              <dt className="text-sm font-medium text-gray-500 flex items-center">
                <FiCalendar className="mr-2 h-4 w-4" />
                Uploaded
              </dt>
              <dd className="mt-1 text-sm text-gray-900">
                {document.created_at ? format(new Date(document.created_at), 'MMM d, yyyy h:mm a') : 'N/A'}
              </dd>
            </div>
            <div>
              <dt className="text-sm font-medium text-gray-500 flex items-center">
                <FiClock className="mr-2 h-4 w-4" />
                Last Updated
              </dt>
              <dd className="mt-1 text-sm text-gray-900">
                {document.updated_at ? format(new Date(document.updated_at), 'MMM d, yyyy h:mm a') : 'N/A'}
              </dd>
            </div>
          </dl>
        </div>

        {/* Download Options */}
        {document.status === 'completed' && (
          <div className="bg-white shadow rounded-lg border border-gray-200 p-6">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Download Options</h3>
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
              {downloadFormats.map((format) => (
                <button
                  key={format.id}
                  onClick={() => handleDownload(format.id)}
                  disabled={downloadingFormat === format.id}
                  className="relative rounded-lg border border-gray-300 bg-white p-4 shadow-sm hover:border-primary-400 focus:outline-none hover:shadow-md transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <div className="flex flex-col items-center">
                    <span className="text-3xl mb-2">{format.icon}</span>
                    <h4 className="text-sm font-medium text-gray-900">{format.name}</h4>
                    <p className="mt-1 text-xs text-gray-500">{format.description}</p>
                    {downloadingFormat === format.id ? (
                      <div className="mt-2">
                        <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-primary-600"></div>
                      </div>
                    ) : (
                      <FiDownload className="mt-2 h-4 w-4 text-gray-400" />
                    )}
                  </div>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Generated Files Preview (if available) */}
        {document.generated_files && typeof document.generated_files === 'object' && Object.keys(document.generated_files).length > 0 && (
          <div className="bg-white shadow rounded-lg border border-gray-200 p-6">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Generated Files</h3>
            <ul className="space-y-2">
              {Object.entries(document.generated_files).map(([format, path]) => (
                <li key={format} className="flex items-center text-sm text-gray-600">
                  <FiFileText className="mr-2 h-4 w-4" />
                  <span className="font-medium">{format.toUpperCase()}:</span>
                  <span className="ml-2">{path}</span>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </Layout>
  );
};

export default DocumentDetail;