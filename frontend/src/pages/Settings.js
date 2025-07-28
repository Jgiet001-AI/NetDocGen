import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  FiSettings,
  FiBriefcase,
  FiFileText,
  FiUser,
  FiLock,
  FiBell
} from 'react-icons/fi';

import Layout from '../components/layout/Layout';
import OrganizationSettings from '../components/settings/OrganizationSettings';
import TemplateList from '../components/templates/TemplateList';

const Settings = () => {
  const [activeTab, setActiveTab] = useState('organization');
  const navigate = useNavigate();

  const tabs = [
    { id: 'organization', label: 'Organization', icon: FiBriefcase },
    { id: 'templates', label: 'Templates', icon: FiFileText },
    { id: 'profile', label: 'Profile', icon: FiUser },
    { id: 'security', label: 'Security', icon: FiLock },
    { id: 'notifications', label: 'Notifications', icon: FiBell },
  ];

  const renderContent = () => {
    switch (activeTab) {
      case 'organization':
        return <OrganizationSettings />;
      case 'templates':
        return <TemplateList />;
      case 'profile':
        return (
          <div className="bg-white shadow rounded-lg p-6">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Profile Settings</h3>
            <p className="text-gray-600">Profile management coming soon...</p>
          </div>
        );
      case 'security':
        return (
          <div className="bg-white shadow rounded-lg p-6">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Security Settings</h3>
            <p className="text-gray-600">Security settings coming soon...</p>
          </div>
        );
      case 'notifications':
        return (
          <div className="bg-white shadow rounded-lg p-6">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Notification Preferences</h3>
            <p className="text-gray-600">Notification settings coming soon...</p>
          </div>
        );
      default:
        return null;
    }
  };

  return (
    <Layout>
      <div className="space-y-6">
        {/* Header */}
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Settings</h1>
          <p className="mt-2 text-gray-600">
            Manage your account and application preferences
          </p>
        </div>

        {/* Tabs */}
        <div className="border-b border-gray-200">
          <nav className="-mb-px flex space-x-8" aria-label="Tabs">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`
                    group inline-flex items-center py-4 px-1 border-b-2 font-medium text-sm
                    ${
                      activeTab === tab.id
                        ? 'border-primary-500 text-primary-600'
                        : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                    }
                  `}
                >
                  <Icon
                    className={`
                      mr-2 h-5 w-5
                      ${
                        activeTab === tab.id
                          ? 'text-primary-500'
                          : 'text-gray-400 group-hover:text-gray-500'
                      }
                    `}
                  />
                  {tab.label}
                </button>
              );
            })}
          </nav>
        </div>

        {/* Content */}
        <div>{renderContent()}</div>
      </div>
    </Layout>
  );
};

export default Settings;