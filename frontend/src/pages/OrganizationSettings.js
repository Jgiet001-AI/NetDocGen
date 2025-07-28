import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { 
  FiSave, 
  FiUpload, 
  FiEye,
  FiSettings,
  FiUsers,
  FiFileText
} from 'react-icons/fi';
import toast from 'react-hot-toast';

import Layout from '../components/layout/Layout';
import { createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Redux thunks for organization management
export const fetchCurrentOrganization = createAsyncThunk(
  'organization/fetchCurrent',
  async (_, { rejectWithValue }) => {
    try {
      const response = await axios.get(`${API_URL}/api/organizations/current`);
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to fetch organization');
    }
  }
);

export const updateOrganization = createAsyncThunk(
  'organization/update',
  async ({ organizationId, data }, { rejectWithValue }) => {
    try {
      const response = await axios.put(`${API_URL}/api/organizations/${organizationId}`, data);
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to update organization');
    }
  }
);

export const uploadOrganizationLogo = createAsyncThunk(
  'organization/uploadLogo',
  async ({ organizationId, logoFile }, { rejectWithValue }) => {
    try {
      const formData = new FormData();
      formData.append('logo', logoFile);
      
      const response = await axios.post(
        `${API_URL}/api/organizations/${organizationId}/logo`,
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      );
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to upload logo');
    }
  }
);

const OrganizationSettings = () => {
  const dispatch = useDispatch();
  const [activeTab, setActiveTab] = useState('general');
  const [organization, setOrganization] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    display_name: '',
    description: '',
    primary_contact: '',
    email: '',
    phone: '',
    website: '',
    address_line1: '',
    address_line2: '',
    city: '',
    state: '',
    postal_code: '',
    country: '',
    primary_color: '#1e3c72',
    secondary_color: '#2a5298',
    accent_color: '#4CAF50',
    default_font_family: 'Arial',
    default_font_size: '14px',
    letterhead_html: '',
    footer_html: '',
    default_template_style: 'professional',
    document_numbering_format: 'DOC-{year}-{seq:04d}'
  });
  const [logoFile, setLogoFile] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    loadOrganization();
  }, []);

  const loadOrganization = async () => {
    try {
      setIsLoading(true);
      const result = await dispatch(fetchCurrentOrganization()).unwrap();
      if (result) {
        setOrganization(result);
        setFormData({
          name: result.name || '',
          display_name: result.display_name || '',
          description: result.description || '',
          primary_contact: result.primary_contact || '',
          email: result.email || '',
          phone: result.phone || '',
          website: result.website || '',
          address_line1: result.address_line1 || '',
          address_line2: result.address_line2 || '',
          city: result.city || '',
          state: result.state || '',
          postal_code: result.postal_code || '',
          country: result.country || '',
          primary_color: result.primary_color || '#1e3c72',
          secondary_color: result.secondary_color || '#2a5298',
          accent_color: result.accent_color || '#4CAF50',
          default_font_family: result.default_font_family || 'Arial',
          default_font_size: result.default_font_size || '14px',
          letterhead_html: result.letterhead_html || '',
          footer_html: result.footer_html || '',
          default_template_style: result.default_template_style || 'professional',
          document_numbering_format: result.document_numbering_format || 'DOC-{year}-{seq:04d}'
        });
      }
    } catch (error) {
      console.error('Error loading organization:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleLogoChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      if (file.size > 5 * 1024 * 1024) { // 5MB limit
        toast.error('Logo file must be smaller than 5MB');
        return;
      }
      if (!file.type.startsWith('image/')) {
        toast.error('Please select an image file');
        return;
      }
      setLogoFile(file);
    }
  };

  const handleSaveGeneral = async () => {
    if (!organization) {
      toast.error('No organization to update');
      return;
    }

    try {
      setIsLoading(true);
      await dispatch(updateOrganization({
        organizationId: organization.id,
        data: formData
      })).unwrap();
      
      toast.success('Organization settings updated successfully');
    } catch (error) {
      toast.error('Failed to update organization settings');
      console.error('Update error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleUploadLogo = async () => {
    if (!logoFile || !organization) return;

    try {
      setIsLoading(true);
      await dispatch(uploadOrganizationLogo({
        organizationId: organization.id,
        logoFile
      })).unwrap();
      
      toast.success('Logo uploaded successfully');
      setLogoFile(null);
      await loadOrganization(); // Refresh to get new logo URL
    } catch (error) {
      toast.error('Failed to upload logo');
      console.error('Upload error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const tabs = [
    { id: 'general', label: 'General', icon: FiSettings },
    { id: 'branding', label: 'Branding', icon: FiEye },
    { id: 'templates', label: 'Templates', icon: FiFileText }
  ];

  if (isLoading && !organization) {
    return (
      <Layout>
        <div className="flex justify-center items-center h-64">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
        </div>
      </Layout>
    );
  }

  if (!organization) {
    return (
      <Layout>
        <div className="max-w-4xl mx-auto">
          <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-6">
            <h2 className="text-lg font-semibold text-yellow-800 mb-2">No Organization Found</h2>
            <p className="text-yellow-700">
              You need to be associated with an organization to access these settings. 
              Please contact your administrator.
            </p>
          </div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="max-w-6xl mx-auto">
        <div className="mb-6">
          <h1 className="text-3xl font-bold text-gray-900">Organization Settings</h1>
          <p className="mt-2 text-gray-600">
            Manage your organization's profile, branding, and document templates
          </p>
        </div>

        {/* Tab Navigation */}
        <div className="border-b border-gray-200 mb-6">
          <nav className="-mb-px flex space-x-8">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`py-2 px-1 border-b-2 font-medium text-sm flex items-center ${
                  activeTab === tab.id
                    ? 'border-primary-500 text-primary-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                <tab.icon className="mr-2 h-4 w-4" />
                {tab.label}
              </button>
            ))}
          </nav>
        </div>

        {/* General Settings Tab */}
        {activeTab === 'general' && (
          <div className="space-y-6">
            <div className="bg-white shadow rounded-lg">
              <div className="px-6 py-4 border-b border-gray-200">
                <h2 className="text-lg font-medium text-gray-900">Organization Information</h2>
              </div>
              <div className="p-6 space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-700">
                      Organization Name
                    </label>
                    <input
                      type="text"
                      name="name"
                      value={formData.name}
                      onChange={handleInputChange}
                      className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                      required
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-700">
                      Display Name
                    </label>
                    <input
                      type="text"
                      name="display_name"
                      value={formData.display_name}
                      onChange={handleInputChange}
                      className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                      placeholder="Name shown on documents"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700">
                    Description
                  </label>
                  <textarea
                    name="description"
                    value={formData.description}
                    onChange={handleInputChange}
                    rows={3}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                  />
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-700">
                      Primary Contact
                    </label>
                    <input
                      type="text"
                      name="primary_contact"
                      value={formData.primary_contact}
                      onChange={handleInputChange}
                      className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-700">
                      Email
                    </label>
                    <input
                      type="email"
                      name="email"
                      value={formData.email}
                      onChange={handleInputChange}
                      className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                    />
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-700">
                      Phone
                    </label>
                    <input
                      type="tel"
                      name="phone"
                      value={formData.phone}
                      onChange={handleInputChange}
                      className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700">
                    Website
                  </label>
                  <input
                    type="url"
                    name="website"
                    value={formData.website}
                    onChange={handleInputChange}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                    placeholder="https://example.com"
                  />
                </div>

                <div className="space-y-4">
                  <h3 className="text-md font-medium text-gray-900">Address</h3>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700">
                        Address Line 1
                      </label>
                      <input
                        type="text"
                        name="address_line1"
                        value={formData.address_line1}
                        onChange={handleInputChange}
                        className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                      />
                    </div>
                    
                    <div>
                      <label className="block text-sm font-medium text-gray-700">
                        Address Line 2
                      </label>
                      <input
                        type="text"
                        name="address_line2"
                        value={formData.address_line2}
                        onChange={handleInputChange}
                        className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                      />
                    </div>
                  </div>
                  
                  <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700">
                        City
                      </label>
                      <input
                        type="text"
                        name="city"
                        value={formData.city}
                        onChange={handleInputChange}
                        className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                      />
                    </div>
                    
                    <div>
                      <label className="block text-sm font-medium text-gray-700">
                        State/Province
                      </label>
                      <input
                        type="text"
                        name="state"
                        value={formData.state}
                        onChange={handleInputChange}
                        className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                      />
                    </div>
                    
                    <div>
                      <label className="block text-sm font-medium text-gray-700">
                        Postal Code
                      </label>
                      <input
                        type="text"
                        name="postal_code"
                        value={formData.postal_code}
                        onChange={handleInputChange}
                        className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                      />
                    </div>
                    
                    <div>
                      <label className="block text-sm font-medium text-gray-700">
                        Country
                      </label>
                      <input
                        type="text"
                        name="country"
                        value={formData.country}
                        onChange={handleInputChange}
                        className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                      />
                    </div>
                  </div>
                </div>

                <div className="flex justify-end">
                  <button
                    onClick={handleSaveGeneral}
                    disabled={isLoading}
                    className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50"
                  >
                    <FiSave className="mr-2 h-4 w-4" />
                    {isLoading ? 'Saving...' : 'Save General Settings'}
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Branding Tab */}
        {activeTab === 'branding' && (
          <div className="space-y-6">
            {/* Logo Upload */}
            <div className="bg-white shadow rounded-lg">
              <div className="px-6 py-4 border-b border-gray-200">
                <h2 className="text-lg font-medium text-gray-900">Organization Logo</h2>
              </div>
              <div className="p-6">
                <div className="flex items-center space-x-6">
                  {organization.logo_url ? (
                    <div className="shrink-0">
                      <img
                        src={organization.logo_url}
                        alt="Organization Logo"
                        className="h-16 w-16 object-contain border border-gray-300 rounded"
                      />
                    </div>
                  ) : (
                    <div className="shrink-0 h-16 w-16 bg-gray-100 border border-gray-300 rounded flex items-center justify-center">
                      <FiUpload className="h-6 w-6 text-gray-400" />
                    </div>
                  )}
                  
                  <div className="flex-1">
                    <input
                      type="file"
                      accept="image/*"
                      onChange={handleLogoChange}
                      className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-medium file:bg-primary-50 file:text-primary-700 hover:file:bg-primary-100"
                    />
                    <p className="mt-1 text-sm text-gray-500">
                      PNG, JPG, or SVG up to 5MB. Recommended size: 300x100px
                    </p>
                  </div>
                  
                  {logoFile && (
                    <button
                      onClick={handleUploadLogo}
                      disabled={isLoading}
                      className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50"
                    >
                      <FiUpload className="mr-2 h-4 w-4" />
                      {isLoading ? 'Uploading...' : 'Upload Logo'}
                    </button>
                  )}
                </div>
              </div>
            </div>

            {/* Color Scheme */}
            <div className="bg-white shadow rounded-lg">
              <div className="px-6 py-4 border-b border-gray-200">
                <h2 className="text-lg font-medium text-gray-900">Color Scheme</h2>
              </div>
              <div className="p-6">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-700">
                      Primary Color
                    </label>
                    <div className="mt-1 flex items-center space-x-3">
                      <input
                        type="color"
                        name="primary_color"
                        value={formData.primary_color}
                        onChange={handleInputChange}
                        className="h-10 w-16 border border-gray-300 rounded-md"
                      />
                      <input
                        type="text"
                        name="primary_color"
                        value={formData.primary_color}
                        onChange={handleInputChange}
                        className="flex-1 border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                      />
                    </div>
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-700">
                      Secondary Color
                    </label>
                    <div className="mt-1 flex items-center space-x-3">
                      <input
                        type="color"
                        name="secondary_color"
                        value={formData.secondary_color}
                        onChange={handleInputChange}
                        className="h-10 w-16 border border-gray-300 rounded-md"
                      />
                      <input
                        type="text"
                        name="secondary_color"
                        value={formData.secondary_color}
                        onChange={handleInputChange}
                        className="flex-1 border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                      />
                    </div>
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-700">
                      Accent Color
                    </label>
                    <div className="mt-1 flex items-center space-x-3">
                      <input
                        type="color"
                        name="accent_color"
                        value={formData.accent_color}
                        onChange={handleInputChange}
                        className="h-10 w-16 border border-gray-300 rounded-md"
                      />
                      <input
                        type="text"
                        name="accent_color"
                        value={formData.accent_color}
                        onChange={handleInputChange}
                        className="flex-1 border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                      />
                    </div>
                  </div>
                </div>

                {/* Font Settings */}
                <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-700">
                      Default Font Family
                    </label>
                    <select
                      name="default_font_family"
                      value={formData.default_font_family}
                      onChange={handleInputChange}
                      className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                    >
                      <option value="Arial">Arial</option>
                      <option value="Helvetica">Helvetica</option>
                      <option value="Times New Roman">Times New Roman</option>
                      <option value="Calibri">Calibri</option>
                      <option value="Open Sans">Open Sans</option>
                      <option value="Roboto">Roboto</option>
                    </select>
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-gray-700">
                      Default Font Size
                    </label>
                    <select
                      name="default_font_size"
                      value={formData.default_font_size}
                      onChange={handleInputChange}
                      className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
                    >
                      <option value="12px">12px</option>
                      <option value="14px">14px</option>
                      <option value="16px">16px</option>
                      <option value="18px">18px</option>
                    </select>
                  </div>
                </div>

                <div className="mt-6 flex justify-end">
                  <button
                    onClick={handleSaveGeneral}
                    disabled={isLoading}
                    className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50"
                  >
                    <FiSave className="mr-2 h-4 w-4" />
                    {isLoading ? 'Saving...' : 'Save Branding Settings'}
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Templates Tab */}
        {activeTab === 'templates' && (
          <div className="bg-white shadow rounded-lg">
            <div className="px-6 py-4 border-b border-gray-200">
              <h2 className="text-lg font-medium text-gray-900">Document Templates</h2>
            </div>
            <div className="p-6">
              <p className="text-gray-600 mb-4">
                Manage custom document templates for your organization.
              </p>
              <div className="text-center py-12">
                <FiFileText className="mx-auto h-12 w-12 text-gray-400" />
                <h3 className="mt-2 text-sm font-medium text-gray-900">No custom templates</h3>
                <p className="mt-1 text-sm text-gray-500">
                  Template management is coming soon.
                </p>
              </div>
            </div>
          </div>
        )}
      </div>
    </Layout>
  );
};

export default OrganizationSettings;