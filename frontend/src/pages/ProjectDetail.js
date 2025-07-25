import React, { useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { 
  FiArrowLeft, 
  FiEdit2, 
  FiTrash2,
  FiUpload,
  FiFileText,
  FiClock,
  FiCheckCircle,
  FiAlertCircle,
  FiDownload
} from 'react-icons/fi';
import { format } from 'date-fns';
import toast from 'react-hot-toast';

import Layout from '../components/layout/Layout';
import { fetchProject, selectCurrentProject, deleteProject } from '../store/projectSlice';
import { fetchDocuments, selectDocuments } from '../store/documentSlice';

const ProjectDetail = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  
  const project = useSelector(selectCurrentProject);
  const allDocuments = useSelector(selectDocuments);
  const projectDocuments = Array.isArray(allDocuments) ? allDocuments.filter(doc => doc.project_id === id) : [];

  useEffect(() => {
    dispatch(fetchProject(id));
    dispatch(fetchDocuments(id));
  }, [dispatch, id]);

  const handleDelete = async () => {
    if (window.confirm('Are you sure you want to delete this project? This action cannot be undone.')) {
      const result = await dispatch(deleteProject(id));
      if (deleteProject.fulfilled.match(result)) {
        toast.success('Project deleted successfully');
        navigate('/projects');
      }
    }
  };

  const getStatusIcon = (status) => {
    switch (status) {
      case 'completed':
        return <FiCheckCircle className="h-5 w-5 text-green-500" />;
      case 'processing':
        return <FiClock className="h-5 w-5 text-yellow-500 animate-spin" />;
      case 'failed':
        return <FiAlertCircle className="h-5 w-5 text-red-500" />;
      default:
        return <FiClock className="h-5 w-5 text-gray-400" />;
    }
  };

  const getStatusBadge = (status) => {
    const statusConfig = {
      completed: 'bg-green-100 text-green-800',
      processing: 'bg-yellow-100 text-yellow-800',
      failed: 'bg-red-100 text-red-800',
      uploaded: 'bg-gray-100 text-gray-800'
    };

    return (
      <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${statusConfig[status] || statusConfig.uploaded}`}>
        {status.charAt(0).toUpperCase() + status.slice(1)}
      </span>
    );
  };

  if (!project) {
    return (
      <Layout>
        <div className="flex justify-center items-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="space-y-6">
        {/* Header */}
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <Link
              to="/projects"
              className="text-gray-400 hover:text-gray-600"
            >
              <FiArrowLeft className="h-6 w-6" />
            </Link>
            <div>
              <h1 className="text-3xl font-bold text-gray-900">{project.name}</h1>
              <p className="mt-1 text-gray-600">{project.description}</p>
            </div>
          </div>
          
          <div className="flex items-center space-x-3">
            <Link
              to={`/upload?project=${id}`}
              className="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
            >
              <FiUpload className="mr-2 h-4 w-4" />
              Upload Diagram
            </Link>
            <button
              onClick={() => navigate(`/projects/${id}/edit`)}
              className="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
            >
              <FiEdit2 className="mr-2 h-4 w-4" />
              Edit
            </button>
            <button
              onClick={handleDelete}
              className="inline-flex items-center px-4 py-2 border border-red-300 shadow-sm text-sm font-medium rounded-md text-red-700 bg-white hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
            >
              <FiTrash2 className="mr-2 h-4 w-4" />
              Delete
            </button>
          </div>
        </div>

        {/* Project Info */}
        <div className="bg-white shadow rounded-lg border border-gray-200 p-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
              <p className="text-sm font-medium text-gray-500">Created</p>
              <p className="mt-1 text-sm text-gray-900">
                {project.created_at ? format(new Date(project.created_at), 'MMM d, yyyy h:mm a') : 'N/A'}
              </p>
            </div>
            <div>
              <p className="text-sm font-medium text-gray-500">Last Updated</p>
              <p className="mt-1 text-sm text-gray-900">
                {project.updated_at ? format(new Date(project.updated_at), 'MMM d, yyyy h:mm a') : 'N/A'}
              </p>
            </div>
            <div>
              <p className="text-sm font-medium text-gray-500">Documents</p>
              <p className="mt-1 text-sm text-gray-900">
                {projectDocuments.length} total
              </p>
            </div>
          </div>
        </div>

        {/* Documents List */}
        <div>
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Project Documents</h2>
          
          {projectDocuments.length === 0 ? (
            <div className="bg-white shadow rounded-lg border border-gray-200 p-12">
              <div className="text-center">
                <FiFileText className="mx-auto h-12 w-12 text-gray-400" />
                <h3 className="mt-2 text-sm font-medium text-gray-900">No documents</h3>
                <p className="mt-1 text-sm text-gray-500">
                  Upload a Visio diagram to get started.
                </p>
                <div className="mt-6">
                  <Link
                    to={`/upload?project=${id}`}
                    className="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
                  >
                    <FiUpload className="mr-2 h-4 w-4" />
                    Upload Diagram
                  </Link>
                </div>
              </div>
            </div>
          ) : (
            <div className="bg-white shadow overflow-hidden sm:rounded-md">
              <ul className="divide-y divide-gray-200">
                {projectDocuments.map((document) => (
                  <li key={document.id}>
                    <Link
                      to={`/documents/${document.id}`}
                      className="block hover:bg-gray-50"
                    >
                      <div className="px-4 py-4 sm:px-6">
                        <div className="flex items-center justify-between">
                          <div className="flex items-center">
                            {getStatusIcon(document.status)}
                            <div className="ml-3">
                              <p className="text-sm font-medium text-gray-900">
                                {document.filename}
                              </p>
                              <p className="text-sm text-gray-500">
                                Uploaded {document.created_at ? format(new Date(document.created_at), 'MMM d, yyyy h:mm a') : 'Recently'}
                              </p>
                            </div>
                          </div>
                          
                          <div className="flex items-center space-x-4">
                            {getStatusBadge(document.status)}
                            
                            {document.status === 'completed' && (
                              <div className="flex space-x-2">
                                <button
                                  onClick={(e) => {
                                    e.preventDefault();
                                    // Handle download
                                  }}
                                  className="text-primary-600 hover:text-primary-700"
                                  title="Download HTML"
                                >
                                  <FiDownload className="h-5 w-5" />
                                </button>
                              </div>
                            )}
                          </div>
                        </div>
                        
                        {document.error && (
                          <div className="mt-2">
                            <p className="text-sm text-red-600">
                              Error: {document.error}
                            </p>
                          </div>
                        )}
                      </div>
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>
    </Layout>
  );
};

export default ProjectDetail;