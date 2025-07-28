import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  FiFileText,
  FiPlus,
  FiEdit2,
  FiTrash2,
  FiCopy,
  FiEye,
  FiDownload,
  FiUpload,
  FiLock,
  FiLoader,
  FiSearch
} from 'react-icons/fi';
import axios from 'axios';
import toast from 'react-hot-toast';
import { format } from 'date-fns';

export default function TemplateList() {
  const navigate = useNavigate();
  const [templates, setTemplates] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterType, setFilterType] = useState('all');
  const [deleteConfirm, setDeleteConfirm] = useState(null);
  const [importDialogOpen, setImportDialogOpen] = useState(false);
  const fileInputRef = React.useRef(null);

  useEffect(() => {
    fetchTemplates();
  }, []);

  const fetchTemplates = async () => {
    try {
      const response = await axios.get('/api/templates');
      setTemplates(response.data);
    } catch (error) {
      toast.error('Failed to load templates');
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (templateId) => {
    try {
      await axios.delete(`/api/templates/${templateId}`);
      toast.success('Template deleted successfully');
      fetchTemplates();
      setDeleteConfirm(null);
    } catch (error) {
      toast.error('Failed to delete template');
    }
  };

  const handleExportTemplate = async (template) => {
    try {
      // Create a complete template export object
      const exportData = {
        version: '1.0',
        exportDate: new Date().toISOString(),
        template: {
          name: template.name,
          description: template.description,
          template_type: template.template_type,
          html_template: template.html_template,
          css_styles: template.css_styles,
          header_template: template.header_template,
          footer_template: template.footer_template,
          cover_page_template: template.cover_page_template,
          template_variables: template.template_variables,
          section_config: template.section_config,
          page_margins: template.page_margins,
          font_config: template.font_config,
          color_scheme: template.color_scheme,
          logo_config: template.logo_config
        }
      };

      // Create and download the file
      const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${template.name.toLowerCase().replace(/\s+/g, '-')}-template.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      
      toast.success('Template exported successfully');
    } catch (error) {
      toast.error('Failed to export template');
    }
  };

  const handleImportTemplate = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    try {
      const text = await file.text();
      const importData = JSON.parse(text);
      
      // Validate import data
      if (!importData.version || !importData.template) {
        throw new Error('Invalid template file format');
      }
      
      // Get current organization
      const orgResponse = await axios.get('/api/organizations/current');
      const organizationId = orgResponse.data.id;
      
      // Create new template from import
      const templateData = {
        ...importData.template,
        organization_id: organizationId,
        name: `${importData.template.name} (Imported)`, // Add suffix to avoid conflicts
        is_system_template: false
      };
      
      await axios.post('/api/templates', templateData);
      toast.success('Template imported successfully');
      fetchTemplates();
      setImportDialogOpen(false);
    } catch (error) {
      if (error.message === 'Invalid template file format') {
        toast.error('Invalid template file format');
      } else {
        toast.error('Failed to import template');
      }
    }
    
    // Reset file input
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const handleClone = async (templateId, templateName) => {
    const name = prompt(`Enter name for cloned template:`, `Copy of ${templateName}`);
    if (!name) return;

    try {
      await axios.post(`/api/templates/${templateId}/clone`, { name });
      toast.success('Template cloned successfully');
      fetchTemplates();
    } catch (error) {
      toast.error('Failed to clone template');
    }
  };

  const handleExport = async (templateId, templateName) => {
    try {
      const response = await axios.get(`/api/templates/${templateId}`);
      const template = response.data;
      handleExportTemplate(template);
    } catch (error) {
      toast.error('Failed to export template');
    }
  };

  const filteredTemplates = templates.filter(template => {
    const matchesSearch = template.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         template.description?.toLowerCase().includes(searchTerm.toLowerCase());
    
    const matchesType = filterType === 'all' || 
                       (filterType === 'system' && template.is_system_template) ||
                       (filterType === 'custom' && !template.is_system_template);
    
    return matchesSearch && matchesType;
  });

  const getTemplateTypeColor = (type) => {
    const colors = {
      network_documentation: 'bg-blue-100 text-blue-800',
      executive_summary: 'bg-purple-100 text-purple-800',
      technical_report: 'bg-green-100 text-green-800',
      custom: 'bg-gray-100 text-gray-800'
    };
    return colors[type] || colors.custom;
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <FiLoader className="h-8 w-8 animate-spin text-primary-600" />
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header and Controls */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div className="flex-1 max-w-lg">
          <div className="relative">
            <FiSearch className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" />
            <input
              type="text"
              placeholder="Search templates..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
        </div>
        
        <div className="flex items-center gap-4">
          <select
            value={filterType}
            onChange={(e) => setFilterType(e.target.value)}
            className="border border-gray-300 rounded-md px-4 py-2 focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="all">All Templates</option>
            <option value="system">System Templates</option>
            <option value="custom">Custom Templates</option>
          </select>
          
          <button
            onClick={() => setImportDialogOpen(true)}
            className="inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
          >
            <FiUpload className="mr-2 h-4 w-4" />
            Import
          </button>
          
          <button
            onClick={() => navigate('/settings/templates/new')}
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
          >
            <FiPlus className="mr-2 h-4 w-4" />
            New Template
          </button>
        </div>
      </div>

      {/* Templates Grid */}
      {filteredTemplates.length === 0 ? (
        <div className="bg-white shadow rounded-lg border border-gray-200 p-12">
          <div className="text-center">
            <FiFileText className="mx-auto h-12 w-12 text-gray-400" />
            <h3 className="mt-2 text-sm font-medium text-gray-900">No templates found</h3>
            <p className="mt-1 text-sm text-gray-500">
              {searchTerm ? 'Try adjusting your search.' : 'Get started by creating a new template.'}
            </p>
            {!searchTerm && (
              <div className="mt-6">
                <button
                  onClick={() => navigate('/settings/templates/new')}
                  className="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
                >
                  <FiPlus className="mr-2 h-4 w-4" />
                  Create Template
                </button>
              </div>
            )}
          </div>
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {filteredTemplates.map((template) => (
            <div
              key={template.id}
              className="bg-white shadow rounded-lg border border-gray-200 hover:shadow-md transition-shadow"
            >
              <div className="p-6">
                <div className="flex items-start justify-between">
                  <div className="flex items-center">
                    <div className="p-2 bg-gray-100 rounded-lg">
                      <FiFileText className="h-6 w-6 text-gray-600" />
                    </div>
                    {template.is_system_template && (
                      <div className="ml-2" title="System Template">
                        <FiLock className="h-4 w-4 text-gray-400" />
                      </div>
                    )}
                  </div>
                  <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${getTemplateTypeColor(template.template_type)}`}>
                    {template.template_type.replace(/_/g, ' ')}
                  </span>
                </div>
                
                <h3 className="mt-4 text-lg font-medium text-gray-900">
                  {template.name}
                </h3>
                
                <p className="mt-2 text-sm text-gray-500 line-clamp-2">
                  {template.description || 'No description available'}
                </p>
                
                <div className="mt-4 space-y-1 text-sm text-gray-500">
                  <div>Version: {template.version || '1.0'}</div>
                  <div>Author: {template.author || 'Unknown'}</div>
                  <div>Used: {template.usage_count || 0} times</div>
                  <div>Created: {format(new Date(template.created_at), 'MMM d, yyyy')}</div>
                </div>
                
                <div className="mt-6 flex flex-wrap gap-2">
                  <button
                    onClick={() => navigate(`/settings/templates/${template.id}/preview`)}
                    className="inline-flex items-center px-3 py-1.5 border border-gray-300 shadow-sm text-xs font-medium rounded text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
                  >
                    <FiEye className="mr-1 h-3 w-3" />
                    Preview
                  </button>
                  
                  {!template.is_system_template && (
                    <button
                      onClick={() => navigate(`/settings/templates/${template.id}/edit`)}
                      className="inline-flex items-center px-3 py-1.5 border border-gray-300 shadow-sm text-xs font-medium rounded text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
                    >
                      <FiEdit2 className="mr-1 h-3 w-3" />
                      Edit
                    </button>
                  )}
                  
                  <button
                    onClick={() => handleClone(template.id, template.name)}
                    className="inline-flex items-center px-3 py-1.5 border border-gray-300 shadow-sm text-xs font-medium rounded text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
                  >
                    <FiCopy className="mr-1 h-3 w-3" />
                    Clone
                  </button>
                  
                  <button
                    onClick={() => handleExport(template.id, template.name)}
                    className="inline-flex items-center px-3 py-1.5 border border-gray-300 shadow-sm text-xs font-medium rounded text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
                  >
                    <FiDownload className="mr-1 h-3 w-3" />
                    Export
                  </button>
                  
                  {!template.is_system_template && (
                    <button
                      onClick={() => setDeleteConfirm(template)}
                      className="inline-flex items-center px-3 py-1.5 border border-gray-300 shadow-sm text-xs font-medium rounded text-red-700 bg-white hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                    >
                      <FiTrash2 className="mr-1 h-3 w-3" />
                      Delete
                    </button>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Delete Confirmation Modal */}
      {deleteConfirm && (
        <div className="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg max-w-md w-full p-6">
            <h3 className="text-lg font-medium text-gray-900 mb-4">
              Delete Template
            </h3>
            <p className="text-sm text-gray-500 mb-4">
              Are you sure you want to delete "{deleteConfirm.name}"? This action cannot be undone.
            </p>
            <div className="flex justify-end space-x-3">
              <button
                onClick={() => setDeleteConfirm(null)}
                className="px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
              >
                Cancel
              </button>
              <button
                onClick={() => handleDelete(deleteConfirm.id)}
                className="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      )}
      
      {/* Import Template Dialog */}
      {importDialogOpen && (
        <div className="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg max-w-md w-full p-6">
            <h3 className="text-lg font-medium text-gray-900 mb-4">
              Import Template
            </h3>
            <p className="text-sm text-gray-500 mb-4">
              Select a template JSON file to import. The template will be added to your organization.
            </p>
            
            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Template File
              </label>
              <input
                ref={fileInputRef}
                type="file"
                accept=".json"
                onChange={handleImportTemplate}
                className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-medium file:bg-primary-50 file:text-primary-700 hover:file:bg-primary-100"
              />
            </div>
            
            <div className="bg-blue-50 border border-blue-200 rounded-md p-3 mb-4">
              <p className="text-sm text-blue-800">
                <strong>Note:</strong> Imported templates will be created as custom templates for your organization.
              </p>
            </div>
            
            <div className="flex justify-end space-x-3">
              <button
                onClick={() => setImportDialogOpen(false)}
                className="px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}