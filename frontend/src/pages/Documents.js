import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import { 
  FiFileText, 
  FiFolder,
  FiClock,
  FiCheckCircle,
  FiAlertCircle,
  FiDownload,
  FiSearch,
  FiFilter
} from 'react-icons/fi';
import { format } from 'date-fns';

import Layout from '../components/layout/Layout';
import { fetchDocuments, selectDocuments } from '../store/documentSlice';
import { fetchProjects, selectProjects } from '../store/projectSlice';

const Documents = () => {
  const dispatch = useDispatch();
  const documents = useSelector(selectDocuments);
  const projects = useSelector(selectProjects);
  const isLoading = useSelector(state => state.documents.isLoading);
  
  const [searchTerm, setSearchTerm] = useState('');
  const [statusFilter, setStatusFilter] = useState('all');
  const [projectFilter, setProjectFilter] = useState('all');

  useEffect(() => {
    dispatch(fetchDocuments());
    dispatch(fetchProjects());
  }, [dispatch]);

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

  // Filter documents
  const filteredDocuments = Array.isArray(documents) ? documents.filter(doc => {
    const matchesSearch = doc.filename.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesStatus = statusFilter === 'all' || doc.status === statusFilter;
    const matchesProject = projectFilter === 'all' || doc.project_id === projectFilter;
    
    return matchesSearch && matchesStatus && matchesProject;
  }) : [];

  // Get project name by ID
  const getProjectName = (projectId) => {
    const project = Array.isArray(projects) ? projects.find(p => p.id === projectId) : null;
    return project ? project.name : 'Unknown Project';
  };

  return (
    <Layout>
      <div className="space-y-6">
        {/* Header */}
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Documents</h1>
            <p className="mt-2 text-gray-600">
              Manage all your network documentation files
            </p>
          </div>
          <Link
            to="/upload"
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
          >
            Upload New
          </Link>
        </div>

        {/* Filters */}
        <div className="bg-white shadow rounded-lg border border-gray-200 p-4">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {/* Search */}
            <div>
              <label htmlFor="search" className="sr-only">Search documents</label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <FiSearch className="h-5 w-5 text-gray-400" />
                </div>
                <input
                  type="text"
                  id="search"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md leading-5 bg-white placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:ring-1 focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  placeholder="Search documents..."
                />
              </div>
            </div>

            {/* Status Filter */}
            <div>
              <label htmlFor="status" className="sr-only">Filter by status</label>
              <select
                id="status"
                value={statusFilter}
                onChange={(e) => setStatusFilter(e.target.value)}
                className="block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm rounded-md"
              >
                <option value="all">All Statuses</option>
                <option value="uploaded">Uploaded</option>
                <option value="processing">Processing</option>
                <option value="completed">Completed</option>
                <option value="failed">Failed</option>
              </select>
            </div>

            {/* Project Filter */}
            <div>
              <label htmlFor="project" className="sr-only">Filter by project</label>
              <select
                id="project"
                value={projectFilter}
                onChange={(e) => setProjectFilter(e.target.value)}
                className="block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm rounded-md"
              >
                <option value="all">All Projects</option>
                {Array.isArray(projects) && projects.map((project) => (
                  <option key={project.id} value={project.id}>
                    {project.name}
                  </option>
                ))}
              </select>
            </div>
          </div>
        </div>

        {/* Documents List */}
        {isLoading ? (
          <div className="flex justify-center items-center h-64">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
          </div>
        ) : filteredDocuments.length === 0 ? (
          <div className="bg-white shadow rounded-lg border border-gray-200 p-12">
            <div className="text-center">
              <FiFileText className="mx-auto h-12 w-12 text-gray-400" />
              <h3 className="mt-2 text-sm font-medium text-gray-900">
                {searchTerm || statusFilter !== 'all' || projectFilter !== 'all'
                  ? 'No documents found'
                  : 'No documents yet'}
              </h3>
              <p className="mt-1 text-sm text-gray-500">
                {searchTerm || statusFilter !== 'all' || projectFilter !== 'all'
                  ? 'Try adjusting your filters'
                  : 'Upload a Visio diagram to get started'}
              </p>
              {!searchTerm && statusFilter === 'all' && projectFilter === 'all' && (
                <div className="mt-6">
                  <Link
                    to="/upload"
                    className="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
                  >
                    Upload Document
                  </Link>
                </div>
              )}
            </div>
          </div>
        ) : (
          <div className="bg-white shadow overflow-hidden sm:rounded-md">
            <ul className="divide-y divide-gray-200">
              {filteredDocuments.map((document) => (
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
                            <div className="flex items-center">
                              <p className="text-sm font-medium text-gray-900">
                                {document.filename}
                              </p>
                            </div>
                            <div className="mt-1 flex items-center text-sm text-gray-500">
                              <FiFolder className="mr-1 h-4 w-4" />
                              <span className="mr-4">{getProjectName(document.project_id)}</span>
                              <span>
                                Uploaded {document.created_at ? format(new Date(document.created_at), 'MMM d, yyyy h:mm a') : 'Recently'}
                              </span>
                            </div>
                          </div>
                        </div>
                        
                        <div className="flex items-center space-x-4">
                          {getStatusBadge(document.status)}
                          
                          {document.status === 'completed' && (
                            <button
                              onClick={(e) => {
                                e.preventDefault();
                                // Handle download
                              }}
                              className="text-primary-600 hover:text-primary-700"
                              title="Download"
                            >
                              <FiDownload className="h-5 w-5" />
                            </button>
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
    </Layout>
  );
};

export default Documents;