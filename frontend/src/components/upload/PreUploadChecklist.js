import React, { useState } from 'react';
import { CheckCircleIcon, XCircleIcon, InformationCircleIcon } from '@heroicons/react/24/outline';

const PreUploadChecklist = ({ onComplete, onSkip }) => {
  const [checkedItems, setCheckedItems] = useState({});

  const checklistItems = [
    {
      id: 'device_names',
      category: 'Device Information',
      title: 'Device Names & Models',
      description: 'Each network device should have a clear name and model number',
      example: 'e.g., "CORE-SW-01" with model "Cisco Catalyst 9300"',
      required: true
    },
    {
      id: 'ip_addresses',
      category: 'Device Information',
      title: 'IP Addresses',
      description: 'Management IP addresses for each device',
      example: 'e.g., "10.0.1.1" in the device properties',
      required: true
    },
    {
      id: 'vlan_info',
      category: 'VLAN Configuration',
      title: 'VLAN Names and IDs',
      description: 'VLAN information should be documented on connections or in a separate table',
      example: 'e.g., "VLAN 10 - Management", "VLAN 20 - Users"',
      required: true
    },
    {
      id: 'port_info',
      category: 'Connection Details',
      title: 'Port Numbers',
      description: 'Interface/port numbers on connections between devices',
      example: 'e.g., "Gi1/0/1", "Te1/1/1"',
      required: true
    },
    {
      id: 'port_channels',
      category: 'Connection Details',
      title: 'Port Channels / LAG',
      description: 'Aggregated links should be clearly marked',
      example: 'e.g., "Po1", "LACP Channel 1"',
      required: false
    },
    {
      id: 'device_roles',
      category: 'Architecture',
      title: 'Device Roles',
      description: 'Clear indication of device function in the network',
      example: 'e.g., "Core Switch", "Distribution Switch", "Access Switch", "Firewall"',
      required: true
    },
    {
      id: 'network_design',
      category: 'Architecture',
      title: 'Network Design Pattern',
      description: 'Document the overall network design approach',
      example: 'e.g., "Collapsed Core", "Three-Tier", "Spine-Leaf"',
      required: false
    },
    {
      id: 'redundancy',
      category: 'Architecture',
      title: 'Redundancy Paths',
      description: 'Backup connections and failover paths should be visible',
      example: 'e.g., Dotted lines for backup paths',
      required: false
    },
    {
      id: 'connection_types',
      category: 'Connection Details',
      title: 'Connection Types',
      description: 'Specify the type of each connection',
      example: 'e.g., "1Gbps Copper", "10Gbps Fiber", "40Gbps DAC"',
      required: false
    },
    {
      id: 'site_info',
      category: 'Documentation',
      title: 'Site/Location Information',
      description: 'Physical location or site names for devices',
      example: 'e.g., "Building A - Floor 2", "Data Center Row 3"',
      required: false
    }
  ];

  const groupedItems = checklistItems.reduce((acc, item) => {
    if (!acc[item.category]) {
      acc[item.category] = [];
    }
    acc[item.category].push(item);
    return acc;
  }, {});

  const handleCheck = (itemId) => {
    setCheckedItems(prev => ({
      ...prev,
      [itemId]: !prev[itemId]
    }));
  };

  const allRequiredChecked = checklistItems
    .filter(item => item.required)
    .every(item => checkedItems[item.id]);

  const checkedCount = Object.values(checkedItems).filter(Boolean).length;
  const totalCount = checklistItems.length;
  const requiredCount = checklistItems.filter(item => item.required).length;

  return (
    <div className="bg-white rounded-lg shadow-lg p-6 max-w-4xl mx-auto">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-900 mb-2">
          Pre-Upload Checklist
        </h2>
        <p className="text-gray-600">
          Ensure your Visio diagram contains the following information for best results.
          The AI assistant will help fill in any gaps, but having this information upfront 
          will produce more accurate documentation.
        </p>
      </div>

      <div className="mb-6 bg-blue-50 border border-blue-200 rounded-lg p-4">
        <div className="flex items-start">
          <InformationCircleIcon className="h-5 w-5 text-blue-500 mt-0.5 mr-2" />
          <div className="text-sm text-blue-800">
            <p className="font-semibold mb-1">Tip: Shape Data in Visio</p>
            <p>
              Most information should be added to shape data in Visio. Right-click any shape,
              select "Data" → "Shape Data" to add custom properties like IP addresses, VLANs, etc.
            </p>
          </div>
        </div>
      </div>

      <div className="mb-6">
        <div className="flex justify-between items-center mb-2">
          <span className="text-sm font-medium text-gray-700">
            Progress: {checkedCount} / {totalCount} items
          </span>
          <span className="text-sm text-gray-500">
            ({requiredCount} required items)
          </span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-2">
          <div 
            className="bg-blue-600 h-2 rounded-full transition-all duration-300"
            style={{ width: `${(checkedCount / totalCount) * 100}%` }}
          />
        </div>
      </div>

      <div className="space-y-6 mb-6">
        {Object.entries(groupedItems).map(([category, items]) => (
          <div key={category}>
            <h3 className="text-lg font-semibold text-gray-900 mb-3">
              {category}
            </h3>
            <div className="space-y-3">
              {items.map(item => (
                <div 
                  key={item.id}
                  className={`border rounded-lg p-4 transition-all cursor-pointer ${
                    checkedItems[item.id] 
                      ? 'border-green-300 bg-green-50' 
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                  onClick={() => handleCheck(item.id)}
                >
                  <div className="flex items-start">
                    <div className="flex items-center h-5">
                      <input
                        type="checkbox"
                        checked={checkedItems[item.id] || false}
                        onChange={() => handleCheck(item.id)}
                        className="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                        onClick={(e) => e.stopPropagation()}
                      />
                    </div>
                    <div className="ml-3 flex-1">
                      <div className="flex items-center">
                        <label className="font-medium text-gray-900">
                          {item.title}
                        </label>
                        {item.required && (
                          <span className="ml-2 px-2 py-1 text-xs font-medium bg-red-100 text-red-800 rounded">
                            Required
                          </span>
                        )}
                      </div>
                      <p className="text-sm text-gray-600 mt-1">
                        {item.description}
                      </p>
                      {item.example && (
                        <p className="text-sm text-gray-500 italic mt-1">
                          {item.example}
                        </p>
                      )}
                    </div>
                    <div className="ml-3">
                      {checkedItems[item.id] ? (
                        <CheckCircleIcon className="h-5 w-5 text-green-500" />
                      ) : (
                        <XCircleIcon className="h-5 w-5 text-gray-300" />
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      <div className="flex justify-between items-center pt-6 border-t">
        <button
          onClick={onSkip}
          className="text-gray-500 hover:text-gray-700 font-medium"
        >
          Skip Checklist
        </button>
        <div className="space-x-3">
          <button
            onClick={() => onComplete(checkedItems)}
            disabled={!allRequiredChecked}
            className={`px-6 py-2 rounded-lg font-medium transition-colors ${
              allRequiredChecked
                ? 'bg-blue-600 text-white hover:bg-blue-700'
                : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            }`}
          >
            Continue to Upload
          </button>
        </div>
      </div>
    </div>
  );
};

export default PreUploadChecklist;