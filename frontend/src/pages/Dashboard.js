import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import { 
  FiFolder, 
  FiFileText, 
  FiUpload, 
  FiClock,
  FiCheckCircle,
  FiAlertCircle,
  FiArrowRight
} from 'react-icons/fi';
import Layout from '../components/layout/Layout';
import { fetchProjects, selectProjects } from '../store/projectSlice';
import { fetchDocuments, selectDocuments } from '../store/documentSlice';
import { selectUser } from '../store/authSlice';
import { format } from 'date-fns';

const Dashboard = () => {
  const dispatch = useDispatch();
  const user = useSelector(selectUser);
  const projects = useSelector(selectProjects);
  const documents = useSelector(selectDocuments);

  useEffect(() => {
    dispatch(fetchProjects());
    dispatch(fetchDocuments());
  }, [dispatch]);

  const recentProjects = Array.isArray(projects) ? projects.slice(0, 3) : [];
  const recentDocuments = Array.isArray(documents) ? documents.slice(0, 5) : [];

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

  const getStatusText = (status) => {
    switch (status) {
      case 'completed':
        return 'Completed';
      case 'processing':
        return 'Processing';
      case 'failed':
        return 'Failed';
      default:
        return 'Uploaded';
    }
  };

  return (
    <Layout>
      <div className="space-y-8">
        {/* Welcome Section */}
        <div>
          <h1 className="text-3xl font-bold text-gray-900">
            Welcome back, {user?.full_name || user?.username}!
          </h1>
          <p className="mt-2 text-gray-600">
            Here's an overview of your network documentation projects.
          </p>
        </div>

        {/* Quick Actions */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <Link
            to="/projects/new"
            className="bg-white p-6 rounded-lg shadow hover:shadow-md transition-shadow border border-gray-200"
          >
            <div className="flex items-center justify-between">
              <div>
                <div className="p-3 bg-primary-100 rounded-lg inline-block">
                  <FiFolder className="h-6 w-6 text-primary-600" />
                </div>
                <h3 className="mt-4 text-lg font-medium text-gray-900">Create Project</h3>
                <p className="mt-1 text-sm text-gray-500">Start a new documentation project</p>
              </div>
              <FiArrowRight className="h-5 w-5 text-gray-400" />
            </div>
          </Link>

          <Link
            to="/upload"
            className="bg-white p-6 rounded-lg shadow hover:shadow-md transition-shadow border border-gray-200"
          >
            <div className="flex items-center justify-between">
              <div>
                <div className="p-3 bg-green-100 rounded-lg inline-block">
                  <FiUpload className="h-6 w-6 text-green-600" />
                </div>
                <h3 className="mt-4 text-lg font-medium text-gray-900">Upload Diagram</h3>
                <p className="mt-1 text-sm text-gray-500">Upload a new Visio diagram</p>
              </div>
              <FiArrowRight className="h-5 w-5 text-gray-400" />
            </div>
          </Link>

          <Link
            to="/documents"
            className="bg-white p-6 rounded-lg shadow hover:shadow-md transition-shadow border border-gray-200"
          >
            <div className="flex items-center justify-between">
              <div>
                <div className="p-3 bg-purple-100 rounded-lg inline-block">
                  <FiFileText className="h-6 w-6 text-purple-600" />
                </div>
                <h3 className="mt-4 text-lg font-medium text-gray-900">View Documents</h3>
                <p className="mt-1 text-sm text-gray-500">Browse all your documents</p>
              </div>
              <FiArrowRight className="h-5 w-5 text-gray-400" />
            </div>
          </Link>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <Link 
            to="/projects" 
            className="bg-white p-6 rounded-lg shadow border border-gray-200 hover:shadow-md transition-shadow cursor-pointer"
          >
            <p className="text-sm font-medium text-gray-600">Total Projects</p>
            <p className="mt-2 text-3xl font-bold text-gray-900">{Array.isArray(projects) ? projects.length : 0}</p>
          </Link>
          <Link 
            to="/documents" 
            className="bg-white p-6 rounded-lg shadow border border-gray-200 hover:shadow-md transition-shadow cursor-pointer"
          >
            <p className="text-sm font-medium text-gray-600">Total Documents</p>
            <p className="mt-2 text-3xl font-bold text-gray-900">{Array.isArray(documents) ? documents.length : 0}</p>
          </Link>
          <div className="bg-white p-6 rounded-lg shadow border border-gray-200">
            <p className="text-sm font-medium text-gray-600">Processing</p>
            <p className="mt-2 text-3xl font-bold text-gray-900">
              {Array.isArray(documents) ? documents.filter(d => d.status === 'processing').length : 0}
            </p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow border border-gray-200">
            <p className="text-sm font-medium text-gray-600">Completed</p>
            <p className="mt-2 text-3xl font-bold text-gray-900">
              {Array.isArray(documents) ? documents.filter(d => d.status === 'completed').length : 0}
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Recent Projects */}
          <div>
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold text-gray-900">Recent Projects</h2>
              <Link to="/projects" className="text-sm text-primary-600 hover:text-primary-700">
                View all →
              </Link>
            </div>
            <div className="bg-white shadow rounded-lg border border-gray-200">
              {recentProjects.length > 0 ? (
                <ul className="divide-y divide-gray-200">
                  {recentProjects.map((project) => (
                    <li key={project.id}>
                      <Link
                        to={`/projects/${project.id}`}
                        className="block px-6 py-4 hover:bg-gray-50"
                      >
                        <div className="flex items-center justify-between">
                          <div>
                            <p className="text-sm font-medium text-gray-900">{project.name}</p>
                            <p className="text-sm text-gray-500">{project.description}</p>
                          </div>
                          <div className="text-sm text-gray-500">
                            {project.document_count || 0} documents
                          </div>
                        </div>
                      </Link>
                    </li>
                  ))}
                </ul>
              ) : (
                <div className="p-6 text-center">
                  <p className="text-gray-500">No projects yet</p>
                  <Link
                    to="/projects/new"
                    className="mt-2 inline-block text-primary-600 hover:text-primary-700"
                  >
                    Create your first project
                  </Link>
                </div>
              )}
            </div>
          </div>

          {/* Recent Documents */}
          <div>
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold text-gray-900">Recent Documents</h2>
              <Link to="/documents" className="text-sm text-primary-600 hover:text-primary-700">
                View all →
              </Link>
            </div>
            <div className="bg-white shadow rounded-lg border border-gray-200">
              {recentDocuments.length > 0 ? (
                <ul className="divide-y divide-gray-200">
                  {recentDocuments.map((document) => (
                    <li key={document.id}>
                      <Link
                        to={`/documents/${document.id}`}
                        className="block px-6 py-4 hover:bg-gray-50"
                      >
                        <div className="flex items-center justify-between">
                          <div className="flex items-center">
                            {getStatusIcon(document.status)}
                            <div className="ml-3">
                              <p className="text-sm font-medium text-gray-900">
                                {document.filename}
                              </p>
                              <p className="text-sm text-gray-500">
                                {getStatusText(document.status)} • {document.created_at ? format(new Date(document.created_at), 'MMM d, yyyy') : 'N/A'}
                              </p>
                            </div>
                          </div>
                        </div>
                      </Link>
                    </li>
                  ))}
                </ul>
              ) : (
                <div className="p-6 text-center">
                  <p className="text-gray-500">No documents yet</p>
                  <Link
                    to="/upload"
                    className="mt-2 inline-block text-primary-600 hover:text-primary-700"
                  >
                    Upload your first diagram
                  </Link>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default Dashboard;