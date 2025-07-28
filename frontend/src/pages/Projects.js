import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import { 
  FiFolder, 
  FiPlus, 
  FiEdit2, 
  FiTrash2,
  FiFileText,
  FiCalendar,
  FiX
} from 'react-icons/fi';
import { Dialog, Transition } from '@headlessui/react';
import { Fragment } from 'react';
import toast from 'react-hot-toast';
import { format } from 'date-fns';

import Layout from '../components/layout/Layout';
import { 
  fetchProjects, 
  createProject, 
  updateProject,
  deleteProject,
  selectProjects,
  selectProjectsLoading,
  clearError
} from '../store/projectSlice';

const Projects = ({ newProject = false }) => {
  const dispatch = useDispatch();
  const projects = useSelector(selectProjects);
  const isLoading = useSelector(selectProjectsLoading);
  
  const [isModalOpen, setIsModalOpen] = useState(newProject);
  const [editingProject, setEditingProject] = useState(null);
  const [deleteConfirm, setDeleteConfirm] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    customer_name: '',
    customer_organization: '',
    customer_contact_name: '',
    customer_contact_email: '',
    customer_contact_phone: '',
    project_code: '',
    project_manager: '',
    contract_number: '',
    po_number: '',
    start_date: '',
    end_date: '',
    budget: '',
    priority: 'medium'
  });

  useEffect(() => {
    dispatch(fetchProjects());
  }, [dispatch]);

  useEffect(() => {
    setIsModalOpen(newProject);
  }, [newProject]);

  const handleOpenModal = (project = null) => {
    if (project) {
      setEditingProject(project);
      setFormData({
        name: project.name,
        description: project.description,
        customer_name: project.customer_name || '',
        customer_organization: project.customer_organization || '',
        customer_contact_name: project.customer_contact_name || '',
        customer_contact_email: project.customer_contact_email || '',
        customer_contact_phone: project.customer_contact_phone || '',
        project_code: project.project_code || '',
        project_manager: project.project_manager || '',
        contract_number: project.contract_number || '',
        po_number: project.po_number || '',
        start_date: project.start_date ? project.start_date.split('T')[0] : '',
        end_date: project.end_date ? project.end_date.split('T')[0] : '',
        budget: project.budget || '',
        priority: project.priority || 'medium'
      });
    } else {
      setEditingProject(null);
      setFormData({ 
        name: '', 
        description: '',
        customer_name: '',
        customer_organization: '',
        customer_contact_name: '',
        customer_contact_email: '',
        customer_contact_phone: '',
        project_code: '',
        project_manager: '',
        contract_number: '',
        po_number: '',
        start_date: '',
        end_date: '',
        budget: '',
        priority: 'medium'
      });
    }
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setEditingProject(null);
    setFormData({ 
      name: '', 
      description: '',
      customer_name: '',
      customer_organization: '',
      customer_contact_name: '',
      customer_contact_email: '',
      customer_contact_phone: '',
      project_code: '',
      project_manager: '',
      contract_number: '',
      po_number: '',
      start_date: '',
      end_date: '',
      budget: '',
      priority: 'medium'
    });
    dispatch(clearError());
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      if (editingProject) {
        const result = await dispatch(updateProject({
          projectId: editingProject.id,
          ...formData
        }));
        if (updateProject.fulfilled.match(result)) {
          toast.success('Project updated successfully');
          handleCloseModal();
        }
      } else {
        const result = await dispatch(createProject(formData));
        if (createProject.fulfilled.match(result)) {
          toast.success('Project created successfully');
          handleCloseModal();
        }
      }
    } catch (error) {
      toast.error('Operation failed');
    }
  };

  const handleDelete = async (projectId) => {
    try {
      const result = await dispatch(deleteProject(projectId));
      if (deleteProject.fulfilled.match(result)) {
        toast.success('Project deleted successfully');
        setDeleteConfirm(null);
      }
    } catch (error) {
      toast.error('Failed to delete project');
    }
  };

  return (
    <Layout>
      <div className="space-y-6">
        {/* Header */}
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Projects</h1>
            <p className="mt-2 text-gray-600">
              Manage your network documentation projects
            </p>
          </div>
          <button
            onClick={() => handleOpenModal()}
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
          >
            <FiPlus className="mr-2 h-4 w-4" />
            New Project
          </button>
        </div>

        {/* Projects Grid */}
        {isLoading ? (
          <div className="flex justify-center items-center h-64">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
          </div>
        ) : !Array.isArray(projects) || projects.length === 0 ? (
          <div className="bg-white shadow rounded-lg border border-gray-200 p-12">
            <div className="text-center">
              <FiFolder className="mx-auto h-12 w-12 text-gray-400" />
              <h3 className="mt-2 text-sm font-medium text-gray-900">No projects</h3>
              <p className="mt-1 text-sm text-gray-500">
                Get started by creating a new project.
              </p>
              <div className="mt-6">
                <button
                  onClick={() => handleOpenModal()}
                  className="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
                >
                  <FiPlus className="mr-2 h-4 w-4" />
                  New Project
                </button>
              </div>
            </div>
          </div>
        ) : (
          <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {Array.isArray(projects) && projects.map((project) => (
              <div
                key={project.id}
                className="bg-white shadow rounded-lg border border-gray-200 hover:shadow-md transition-shadow"
              >
                <div className="p-6">
                  <div className="flex items-center justify-between mb-4">
                    <div className="p-2 bg-primary-100 rounded-lg inline-block">
                      <FiFolder className="h-6 w-6 text-primary-600" />
                    </div>
                    <div className="flex space-x-2">
                      <button
                        onClick={() => handleOpenModal(project)}
                        className="text-gray-400 hover:text-gray-600"
                      >
                        <FiEdit2 className="h-4 w-4" />
                      </button>
                      <button
                        onClick={() => setDeleteConfirm(project.id)}
                        className="text-gray-400 hover:text-red-600"
                      >
                        <FiTrash2 className="h-4 w-4" />
                      </button>
                    </div>
                  </div>
                  
                  <Link to={`/projects/${project.id}`}>
                    <h3 className="text-lg font-medium text-gray-900 hover:text-primary-600">
                      {project.name}
                    </h3>
                  </Link>
                  
                  <p className="mt-2 text-sm text-gray-500 line-clamp-2">
                    {project.description || 'No description'}
                  </p>
                  
                  <div className="mt-4 space-y-2">
                    <div className="flex items-center text-sm text-gray-500">
                      <FiFileText className="mr-2 h-4 w-4" />
                      {project.document_count || 0} documents
                    </div>
                    <div className="flex items-center text-sm text-gray-500">
                      <FiCalendar className="mr-2 h-4 w-4" />
                      Created {project.created_at ? format(new Date(project.created_at), 'MMM d, yyyy') : 'Recently'}
                    </div>
                  </div>
                  
                  <div className="mt-4">
                    <Link
                      to={`/projects/${project.id}`}
                      className="w-full inline-flex justify-center items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
                    >
                      View Details
                    </Link>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Create/Edit Modal */}
        <Transition appear show={isModalOpen} as={Fragment}>
          <Dialog as="div" className="relative z-10" onClose={handleCloseModal}>
            <Transition.Child
              as={Fragment}
              enter="ease-out duration-300"
              enterFrom="opacity-0"
              enterTo="opacity-100"
              leave="ease-in duration-200"
              leaveFrom="opacity-100"
              leaveTo="opacity-0"
            >
              <div className="fixed inset-0 bg-black bg-opacity-25" />
            </Transition.Child>

            <div className="fixed inset-0 overflow-y-auto">
              <div className="flex min-h-full items-center justify-center p-4 text-center">
                <Transition.Child
                  as={Fragment}
                  enter="ease-out duration-300"
                  enterFrom="opacity-0 scale-95"
                  enterTo="opacity-100 scale-100"
                  leave="ease-in duration-200"
                  leaveFrom="opacity-100 scale-100"
                  leaveTo="opacity-0 scale-95"
                >
                  <Dialog.Panel className="w-full max-w-4xl transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all max-h-[90vh] overflow-y-auto">
                    <Dialog.Title
                      as="h3"
                      className="text-lg font-medium leading-6 text-gray-900"
                    >
                      {editingProject ? 'Edit Project' : 'Create New Project'}
                    </Dialog.Title>
                    
                    <form onSubmit={handleSubmit} className="mt-4">
                      <div className="space-y-6">
                        {/* Basic Information */}
                        <div className="border-b border-gray-200 pb-4">
                          <h4 className="text-base font-medium text-gray-900 mb-4">Basic Information</h4>
                          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                            <div className="sm:col-span-2">
                              <label htmlFor="name" className="block text-sm font-medium text-gray-700">
                                Project Name *
                              </label>
                              <input
                                type="text"
                                id="name"
                                name="name"
                                required
                                value={formData.name}
                                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="My Network Project"
                              />
                            </div>
                            
                            <div className="sm:col-span-2">
                              <label htmlFor="description" className="block text-sm font-medium text-gray-700">
                                Description
                              </label>
                              <textarea
                                id="description"
                                name="description"
                                rows={3}
                                value={formData.description}
                                onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="Brief description of your project..."
                              />
                            </div>

                            <div>
                              <label htmlFor="project_code" className="block text-sm font-medium text-gray-700">
                                Project Code
                              </label>
                              <input
                                type="text"
                                id="project_code"
                                name="project_code"
                                value={formData.project_code}
                                onChange={(e) => setFormData({ ...formData, project_code: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="PRJ-2024-001"
                              />
                            </div>

                            <div>
                              <label htmlFor="priority" className="block text-sm font-medium text-gray-700">
                                Priority
                              </label>
                              <select
                                id="priority"
                                name="priority"
                                value={formData.priority}
                                onChange={(e) => setFormData({ ...formData, priority: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                              >
                                <option value="low">Low</option>
                                <option value="medium">Medium</option>
                                <option value="high">High</option>
                              </select>
                            </div>
                          </div>
                        </div>

                        {/* Customer Information */}
                        <div className="border-b border-gray-200 pb-4">
                          <h4 className="text-base font-medium text-gray-900 mb-4">Customer Information</h4>
                          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                            <div>
                              <label htmlFor="customer_name" className="block text-sm font-medium text-gray-700">
                                Customer Name
                              </label>
                              <input
                                type="text"
                                id="customer_name"
                                name="customer_name"
                                value={formData.customer_name}
                                onChange={(e) => setFormData({ ...formData, customer_name: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="John Smith"
                              />
                            </div>

                            <div>
                              <label htmlFor="customer_organization" className="block text-sm font-medium text-gray-700">
                                Customer Organization
                              </label>
                              <input
                                type="text"
                                id="customer_organization"
                                name="customer_organization"
                                value={formData.customer_organization}
                                onChange={(e) => setFormData({ ...formData, customer_organization: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="Acme Corporation"
                              />
                            </div>

                            <div>
                              <label htmlFor="customer_contact_name" className="block text-sm font-medium text-gray-700">
                                Contact Name
                              </label>
                              <input
                                type="text"
                                id="customer_contact_name"
                                name="customer_contact_name"
                                value={formData.customer_contact_name}
                                onChange={(e) => setFormData({ ...formData, customer_contact_name: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="Jane Doe"
                              />
                            </div>

                            <div>
                              <label htmlFor="customer_contact_email" className="block text-sm font-medium text-gray-700">
                                Contact Email
                              </label>
                              <input
                                type="email"
                                id="customer_contact_email"
                                name="customer_contact_email"
                                value={formData.customer_contact_email}
                                onChange={(e) => setFormData({ ...formData, customer_contact_email: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="jane.doe@acme.com"
                              />
                            </div>

                            <div>
                              <label htmlFor="customer_contact_phone" className="block text-sm font-medium text-gray-700">
                                Contact Phone
                              </label>
                              <input
                                type="tel"
                                id="customer_contact_phone"
                                name="customer_contact_phone"
                                value={formData.customer_contact_phone}
                                onChange={(e) => setFormData({ ...formData, customer_contact_phone: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="+1 (555) 123-4567"
                              />
                            </div>
                          </div>
                        </div>

                        {/* Project Details */}
                        <div className="pb-4">
                          <h4 className="text-base font-medium text-gray-900 mb-4">Project Details</h4>
                          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                            <div>
                              <label htmlFor="project_manager" className="block text-sm font-medium text-gray-700">
                                Project Manager
                              </label>
                              <input
                                type="text"
                                id="project_manager"
                                name="project_manager"
                                value={formData.project_manager}
                                onChange={(e) => setFormData({ ...formData, project_manager: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="Alice Johnson"
                              />
                            </div>

                            <div>
                              <label htmlFor="budget" className="block text-sm font-medium text-gray-700">
                                Budget
                              </label>
                              <input
                                type="text"
                                id="budget"
                                name="budget"
                                value={formData.budget}
                                onChange={(e) => setFormData({ ...formData, budget: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="$50,000"
                              />
                            </div>

                            <div>
                              <label htmlFor="contract_number" className="block text-sm font-medium text-gray-700">
                                Contract Number
                              </label>
                              <input
                                type="text"
                                id="contract_number"
                                name="contract_number"
                                value={formData.contract_number}
                                onChange={(e) => setFormData({ ...formData, contract_number: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="CNT-2024-001"
                              />
                            </div>

                            <div>
                              <label htmlFor="po_number" className="block text-sm font-medium text-gray-700">
                                PO Number
                              </label>
                              <input
                                type="text"
                                id="po_number"
                                name="po_number"
                                value={formData.po_number}
                                onChange={(e) => setFormData({ ...formData, po_number: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="PO-2024-001"
                              />
                            </div>

                            <div>
                              <label htmlFor="start_date" className="block text-sm font-medium text-gray-700">
                                Start Date
                              </label>
                              <input
                                type="date"
                                id="start_date"
                                name="start_date"
                                value={formData.start_date}
                                onChange={(e) => setFormData({ ...formData, start_date: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                              />
                            </div>

                            <div>
                              <label htmlFor="end_date" className="block text-sm font-medium text-gray-700">
                                End Date
                              </label>
                              <input
                                type="date"
                                id="end_date"
                                name="end_date"
                                value={formData.end_date}
                                onChange={(e) => setFormData({ ...formData, end_date: e.target.value })}
                                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                              />
                            </div>
                          </div>
                        </div>
                      </div>

                      <div className="mt-6 flex justify-end space-x-3">
                        <button
                          type="button"
                          onClick={handleCloseModal}
                          className="inline-flex justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus-visible:ring-2 focus-visible:ring-primary-500 focus-visible:ring-offset-2"
                        >
                          Cancel
                        </button>
                        <button
                          type="submit"
                          className="inline-flex justify-center rounded-md border border-transparent bg-primary-600 px-4 py-2 text-sm font-medium text-white hover:bg-primary-700 focus:outline-none focus-visible:ring-2 focus-visible:ring-primary-500 focus-visible:ring-offset-2"
                        >
                          {editingProject ? 'Update' : 'Create'}
                        </button>
                      </div>
                    </form>
                  </Dialog.Panel>
                </Transition.Child>
              </div>
            </div>
          </Dialog>
        </Transition>

        {/* Delete Confirmation */}
        <Transition appear show={deleteConfirm !== null} as={Fragment}>
          <Dialog 
            as="div" 
            className="relative z-10" 
            onClose={() => setDeleteConfirm(null)}
          >
            <Transition.Child
              as={Fragment}
              enter="ease-out duration-300"
              enterFrom="opacity-0"
              enterTo="opacity-100"
              leave="ease-in duration-200"
              leaveFrom="opacity-100"
              leaveTo="opacity-0"
            >
              <div className="fixed inset-0 bg-black bg-opacity-25" />
            </Transition.Child>

            <div className="fixed inset-0 overflow-y-auto">
              <div className="flex min-h-full items-center justify-center p-4 text-center">
                <Transition.Child
                  as={Fragment}
                  enter="ease-out duration-300"
                  enterFrom="opacity-0 scale-95"
                  enterTo="opacity-100 scale-100"
                  leave="ease-in duration-200"
                  leaveFrom="opacity-100 scale-100"
                  leaveTo="opacity-0 scale-95"
                >
                  <Dialog.Panel className="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all">
                    <Dialog.Title
                      as="h3"
                      className="text-lg font-medium leading-6 text-gray-900"
                    >
                      Delete Project
                    </Dialog.Title>
                    
                    <div className="mt-2">
                      <p className="text-sm text-gray-500">
                        Are you sure you want to delete this project? This action cannot be undone and will also delete all associated documents.
                      </p>
                    </div>

                    <div className="mt-4 flex justify-end space-x-3">
                      <button
                        type="button"
                        onClick={() => setDeleteConfirm(null)}
                        className="inline-flex justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus-visible:ring-2 focus-visible:ring-primary-500 focus-visible:ring-offset-2"
                      >
                        Cancel
                      </button>
                      <button
                        type="button"
                        onClick={() => handleDelete(deleteConfirm)}
                        className="inline-flex justify-center rounded-md border border-transparent bg-red-600 px-4 py-2 text-sm font-medium text-white hover:bg-red-700 focus:outline-none focus-visible:ring-2 focus-visible:ring-red-500 focus-visible:ring-offset-2"
                      >
                        Delete
                      </button>
                    </div>
                  </Dialog.Panel>
                </Transition.Child>
              </div>
            </div>
          </Dialog>
        </Transition>
      </div>
    </Layout>
  );
};

export default Projects;