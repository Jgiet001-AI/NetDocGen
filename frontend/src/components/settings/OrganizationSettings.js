import React, { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import {
  FiSave,
  FiUploadCloud,
  FiLoader
} from 'react-icons/fi';
import axios from 'axios';
import toast from 'react-hot-toast';
import { selectUser } from '../../store/authSlice';

export default function OrganizationSettings() {
  const user = useSelector(selectUser);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [activeTab, setActiveTab] = useState('general');
  const [organization, setOrganization] = useState({
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
    logo_url: '',
    primary_color: '#1e3c72',
    secondary_color: '#2a5298',
    accent_color: '#7e8c9a',
    default_font_family: 'Arial, sans-serif',
    default_font_size: '12pt',
    letterhead_html: '',
    footer_html: '',
    default_template_style: 'professional',
    document_numbering_format: 'DOC-{YYYY}-{MM}-{####}'
  });

  useEffect(() => {
    fetchOrganization();
  }, []);

  const fetchOrganization = async () => {
    try {
      const response = await axios.get('/api/organizations/current');
      if (response.data) {
        setOrganization(response.data);
      }
    } catch (error) {
      if (error.response?.status === 404) {
        toast.success('Configure your organization settings');
      } else {
        toast.error('Failed to load organization settings');
      }
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (field) => (event) => {
    setOrganization({
      ...organization,
      [field]: event.target.value
    });
  };

  const handleSave = async () => {
    setSaving(true);
    try {
      const response = organization.id
        ? await axios.put(`/api/organizations/${organization.id}`, organization)
        : await axios.post('/api/organizations', organization);
      
      setOrganization(response.data);
      toast.success('Organization settings saved successfully');
    } catch (error) {
      toast.error('Failed to save organization settings');
    } finally {
      setSaving(false);
    }
  };

  const handleLogoUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('/api/uploads/logo', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      
      setOrganization({
        ...organization,
        logo_url: response.data.url
      });
      toast.success('Logo uploaded successfully');
    } catch (error) {
      toast.error('Failed to upload logo');
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <FiLoader className="h-8 w-8 animate-spin text-primary-600" />
      </div>
    );
  }

  const tabs = [
    { id: 'general', label: 'General Information' },
    { id: 'branding', label: 'Branding' },
    { id: 'documents', label: 'Document Settings' }
  ];

  return (
    <div className="bg-white shadow rounded-lg">
      <div className="px-6 py-4 border-b border-gray-200">
        <h2 className="text-xl font-semibold text-gray-900">Organization Settings</h2>
        <p className="mt-1 text-sm text-gray-600">
          Configure your organization's branding and document settings
        </p>
      </div>

      {/* Tabs */}
      <div className="border-b border-gray-200">
        <nav className="flex -mb-px px-6">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`
                py-3 px-4 border-b-2 font-medium text-sm transition-colors
                ${
                  activeTab === tab.id
                    ? 'border-primary-500 text-primary-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }
              `}
            >
              {tab.label}
            </button>
          ))}
        </nav>
      </div>

      <div className="p-6">
        {/* General Information Tab */}
        {activeTab === 'general' && (
          <div className="space-y-6">
            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2">
              <div className="sm:col-span-2">
                <label className="block text-sm font-medium text-gray-700">
                  Organization Name
                </label>
                <input
                  type="text"
                  value={organization.name}
                  onChange={handleChange('name')}
                  className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  required
                />
              </div>

              <div className="sm:col-span-2">
                <label className="block text-sm font-medium text-gray-700">
                  Display Name
                </label>
                <input
                  type="text"
                  value={organization.display_name}
                  onChange={handleChange('display_name')}
                  className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  placeholder="Name shown on documents"
                />
              </div>

              <div className="sm:col-span-2">
                <label className="block text-sm font-medium text-gray-700">
                  Description
                </label>
                <textarea
                  rows={3}
                  value={organization.description}
                  onChange={handleChange('description')}
                  className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                />
              </div>
            </div>

            <div className="border-t border-gray-200 pt-6">
              <h3 className="text-lg font-medium text-gray-900 mb-4">Contact Information</h3>
              <div className="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <div>
                  <label className="block text-sm font-medium text-gray-700">
                    Primary Contact
                  </label>
                  <input
                    type="text"
                    value={organization.primary_contact}
                    onChange={handleChange('primary_contact')}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700">
                    Email
                  </label>
                  <input
                    type="email"
                    value={organization.email}
                    onChange={handleChange('email')}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700">
                    Phone
                  </label>
                  <input
                    type="tel"
                    value={organization.phone}
                    onChange={handleChange('phone')}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700">
                    Website
                  </label>
                  <input
                    type="url"
                    value={organization.website}
                    onChange={handleChange('website')}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  />
                </div>
              </div>
            </div>

            <div className="border-t border-gray-200 pt-6">
              <h3 className="text-lg font-medium text-gray-900 mb-4">Address</h3>
              <div className="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <div className="sm:col-span-2">
                  <label className="block text-sm font-medium text-gray-700">
                    Address Line 1
                  </label>
                  <input
                    type="text"
                    value={organization.address_line1}
                    onChange={handleChange('address_line1')}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  />
                </div>

                <div className="sm:col-span-2">
                  <label className="block text-sm font-medium text-gray-700">
                    Address Line 2
                  </label>
                  <input
                    type="text"
                    value={organization.address_line2}
                    onChange={handleChange('address_line2')}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700">
                    City
                  </label>
                  <input
                    type="text"
                    value={organization.city}
                    onChange={handleChange('city')}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700">
                    State/Province
                  </label>
                  <input
                    type="text"
                    value={organization.state}
                    onChange={handleChange('state')}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700">
                    Postal Code
                  </label>
                  <input
                    type="text"
                    value={organization.postal_code}
                    onChange={handleChange('postal_code')}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700">
                    Country
                  </label>
                  <input
                    type="text"
                    value={organization.country}
                    onChange={handleChange('country')}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  />
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Branding Tab */}
        {activeTab === 'branding' && (
          <div className="space-y-6">
            <div>
              <h3 className="text-lg font-medium text-gray-900 mb-4">Logo</h3>
              <div className="flex items-center space-x-4">
                {organization.logo_url && (
                  <img
                    src={organization.logo_url}
                    alt="Organization logo"
                    className="h-24 w-auto object-contain border border-gray-200 rounded"
                  />
                )}
                <label className="cursor-pointer inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500">
                  <FiUploadCloud className="mr-2 h-4 w-4" />
                  Upload Logo
                  <input
                    type="file"
                    className="sr-only"
                    accept="image/*"
                    onChange={handleLogoUpload}
                  />
                </label>
              </div>
            </div>

            <div className="border-t border-gray-200 pt-6">
              <h3 className="text-lg font-medium text-gray-900 mb-4">Colors</h3>
              <div className="grid grid-cols-1 gap-6 sm:grid-cols-3">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Primary Color
                  </label>
                  <div className="flex items-center space-x-2">
                    <input
                      type="color"
                      value={organization.primary_color}
                      onChange={handleChange('primary_color')}
                      className="h-10 w-20 border border-gray-300 rounded cursor-pointer"
                    />
                    <input
                      type="text"
                      value={organization.primary_color}
                      onChange={handleChange('primary_color')}
                      className="flex-1 border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Secondary Color
                  </label>
                  <div className="flex items-center space-x-2">
                    <input
                      type="color"
                      value={organization.secondary_color}
                      onChange={handleChange('secondary_color')}
                      className="h-10 w-20 border border-gray-300 rounded cursor-pointer"
                    />
                    <input
                      type="text"
                      value={organization.secondary_color}
                      onChange={handleChange('secondary_color')}
                      className="flex-1 border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Accent Color
                  </label>
                  <div className="flex items-center space-x-2">
                    <input
                      type="color"
                      value={organization.accent_color}
                      onChange={handleChange('accent_color')}
                      className="h-10 w-20 border border-gray-300 rounded cursor-pointer"
                    />
                    <input
                      type="text"
                      value={organization.accent_color}
                      onChange={handleChange('accent_color')}
                      className="flex-1 border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                    />
                  </div>
                </div>
              </div>
            </div>

            <div className="border-t border-gray-200 pt-6">
              <h3 className="text-lg font-medium text-gray-900 mb-4">Typography</h3>
              <div className="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <div>
                  <label className="block text-sm font-medium text-gray-700">
                    Default Font Family
                  </label>
                  <input
                    type="text"
                    value={organization.default_font_family}
                    onChange={handleChange('default_font_family')}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                    placeholder="Arial, sans-serif"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700">
                    Default Font Size
                  </label>
                  <input
                    type="text"
                    value={organization.default_font_size}
                    onChange={handleChange('default_font_size')}
                    className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                    placeholder="12pt"
                  />
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Document Settings Tab */}
        {activeTab === 'documents' && (
          <div className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-gray-700">
                Document Numbering Format
              </label>
              <input
                type="text"
                value={organization.document_numbering_format}
                onChange={handleChange('document_numbering_format')}
                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
              />
              <p className="mt-2 text-sm text-gray-500">
                Use {'{YYYY}'} for year, {'{MM}'} for month, {'{DD}'} for day, {'{####}'} for sequential number
              </p>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">
                Letterhead HTML
              </label>
              <textarea
                rows={6}
                value={organization.letterhead_html}
                onChange={handleChange('letterhead_html')}
                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm font-mono text-xs"
                placeholder="HTML template for document headers"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">
                Footer HTML
              </label>
              <textarea
                rows={6}
                value={organization.footer_html}
                onChange={handleChange('footer_html')}
                className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm font-mono text-xs"
                placeholder="HTML template for document footers"
              />
            </div>
          </div>
        )}
      </div>

      {/* Save Button */}
      <div className="px-6 py-4 bg-gray-50 border-t border-gray-200 flex justify-end">
        <button
          onClick={handleSave}
          disabled={saving}
          className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {saving ? (
            <>
              <FiLoader className="mr-2 h-4 w-4 animate-spin" />
              Saving...
            </>
          ) : (
            <>
              <FiSave className="mr-2 h-4 w-4" />
              Save Settings
            </>
          )}
        </button>
      </div>
    </div>
  );
}