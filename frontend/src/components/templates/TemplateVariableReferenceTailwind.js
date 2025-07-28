import React, { useState } from 'react';
import {
  FiSearch,
  FiCopy,
  FiCode,
  FiFileText,
  FiServer,
  FiGitBranch,
  FiDatabase,
  FiLayers,
  FiActivity,
  FiSettings,
  FiChevronDown,
  FiChevronRight,
  FiInfo
} from 'react-icons/fi';
import toast from 'react-hot-toast';

const VARIABLE_CATEGORIES = {
  basic: {
    name: 'Basic Information',
    icon: <FiFileText className="h-4 w-4" />,
    variables: [
      { name: 'title', description: 'Document title', example: 'Network Infrastructure Documentation' },
      { name: 'generated_date', description: 'Date when document was generated', example: '2024-01-15 14:30:00' },
      { name: 'version', description: 'Document version', example: '1.0' },
      { name: 'filename', description: 'Original Visio filename', example: 'network-diagram.vsdx' }
    ]
  },
  project: {
    name: 'Project Information',
    icon: <FiFileText className="h-4 w-4" />,
    variables: [
      { name: 'project_name', description: 'Project name', example: 'Data Center Upgrade' },
      { name: 'project_description', description: 'Project description', example: 'Complete network infrastructure upgrade...' },
      { name: 'project_code', description: 'Project code/identifier', example: 'PRJ-2024-001' },
      { name: 'project_manager', description: 'Project manager name', example: 'John Smith' },
      { name: 'start_date', description: 'Project start date', example: '2024-01-01' },
      { name: 'end_date', description: 'Project end date', example: '2024-06-30' },
      { name: 'budget', description: 'Project budget', example: '$500,000' },
      { name: 'priority', description: 'Project priority', example: 'high' }
    ]
  },
  customer: {
    name: 'Customer Information',
    icon: <FiServer className="h-4 w-4" />,
    variables: [
      { name: 'customer_name', description: 'Customer contact name', example: 'Jane Doe' },
      { name: 'customer_organization', description: 'Customer organization name', example: 'Acme Corporation' },
      { name: 'customer_contact_email', description: 'Customer email', example: 'jane.doe@acme.com' },
      { name: 'customer_contact_phone', description: 'Customer phone', example: '+1 (555) 123-4567' },
      { name: 'contract_number', description: 'Contract number', example: 'CTR-2024-0123' },
      { name: 'po_number', description: 'Purchase order number', example: 'PO-456789' }
    ]
  },
  organization: {
    name: 'Organization Branding',
    icon: <FiServer className="h-4 w-4" />,
    variables: [
      { name: 'organization.name', description: 'Organization name', example: 'NetDocGen Inc.' },
      { name: 'organization.display_name', description: 'Organization display name', example: 'NetDocGen Solutions' },
      { name: 'organization.logo_url', description: 'Organization logo URL', example: 'https://example.com/logo.png' },
      { name: 'organization.primary_color', description: 'Primary brand color', example: '#1e3c72' },
      { name: 'organization.secondary_color', description: 'Secondary brand color', example: '#2a5298' },
      { name: 'organization.accent_color', description: 'Accent color', example: '#4CAF50' },
      { name: 'organization.website', description: 'Organization website', example: 'https://netdocgen.com' },
      { name: 'organization.email', description: 'Organization email', example: 'info@netdocgen.com' },
      { name: 'organization.phone', description: 'Organization phone', example: '+1 (555) 987-6543' }
    ]
  },
  network: {
    name: 'Network Topology',
    icon: <FiGitBranch className="h-4 w-4" />,
    variables: [
      { name: 'shapes', description: 'Array of network devices', example: '[{name: "Switch-01", type: "switch", ...}]', isArray: true },
      { name: 'connections', description: 'Array of network connections', example: '[{source: "Switch-01", target: "Router-01", ...}]', isArray: true },
      { name: 'shape_count', description: 'Total number of devices', example: '42' },
      { name: 'connection_count', description: 'Total number of connections', example: '78' },
      { name: 'page_count', description: 'Number of Visio pages', example: '3' },
      { name: 'network_type', description: 'Detected network type', example: 'Hybrid' },
      { name: 'topology_pattern', description: 'Network topology pattern', example: 'Hub and Spoke' }
    ]
  },
  devices: {
    name: 'Device Information',
    icon: <FiDatabase className="h-4 w-4" />,
    variables: [
      { name: 'device_types', description: 'List of unique device types', example: '["switch", "router", "firewall"]', isArray: true },
      { name: 'device_type_distribution', description: 'Count by device type', example: '{switch: 20, router: 5, ...}', isObject: true },
      { name: 'devices_by_type', description: 'Devices grouped by type', example: '{switch: [...], router: [...]}', isObject: true },
      { name: 'most_common_device_type', description: 'Most common device type', example: 'switch' },
      { name: 'most_connected_devices', description: 'Devices with most connections', example: '[{name: "Core-Switch-01", connections: 24}]', isArray: true },
      { name: 'isolated_devices', description: 'Devices with no connections', example: '[{name: "Test-Device-01"}]', isArray: true }
    ]
  },
  metrics: {
    name: 'Network Metrics',
    icon: <FiActivity className="h-4 w-4" />,
    variables: [
      { name: 'avg_connections_per_device', description: 'Average connections per device', example: '3.5' },
      { name: 'network_density', description: 'Network connection density', example: '0.142' },
      { name: 'redundancy_level', description: 'Network redundancy level', example: 'High' },
      { name: 'network_segments', description: 'Number of network segments', example: '3' },
      { name: 'high_density_areas', description: 'Areas with high connection density', example: '[{name: "Core", density: 0.8}]', isArray: true }
    ]
  },
  vlans: {
    name: 'VLAN Configuration',
    icon: <FiLayers className="h-4 w-4" />,
    variables: [
      { name: 'vlans', description: 'Array of VLAN configurations', example: '[{id: "10", name: "Management", subnet: "10.0.10.0/24"}]', isArray: true },
      { name: 'port_channels', description: 'Port channel configurations', example: '[{id: "Po1", members: ["Gi1/0/1", "Gi1/0/2"]}]', isArray: true }
    ]
  },
  custom: {
    name: 'Custom & Conditional',
    icon: <FiSettings className="h-4 w-4" />,
    variables: [
      { name: 'supplemental_data', description: 'User-provided supplemental information', example: '{site_details: {...}, ...}', isObject: true },
      { name: 'ai_analysis', description: 'AI-generated insights', example: '{recommendations: [...], risks: [...]}', isObject: true },
      { name: 'custom_fields', description: 'Custom fields from organization', example: '{department: "IT", location: "Building A"}', isObject: true }
    ]
  }
};

const JINJA2_CONSTRUCTS = [
  { syntax: '{% if condition %}...{% endif %}', description: 'Conditional rendering', example: '{% if vlans %}Show VLAN section{% endif %}' },
  { syntax: '{% for item in list %}...{% endfor %}', description: 'Loop through arrays', example: '{% for device in shapes %}{{ device.name }}{% endfor %}' },
  { syntax: '{{ variable | filter }}', description: 'Apply filters to variables', example: '{{ title | upper }}' },
  { syntax: '{{ variable | default("value") }}', description: 'Provide default values', example: '{{ project_name | default("Untitled Project") }}' },
  { syntax: '{{ variable | length }}', description: 'Get length of arrays/strings', example: '{{ shapes | length }}' },
  { syntax: '{% include "template.html" %}', description: 'Include other templates', example: '{% include "header.html" %}' },
  { syntax: '{% set var = value %}', description: 'Set variables', example: '{% set total = shapes | length %}' },
  { syntax: '{{ variable.property }}', description: 'Access object properties', example: '{{ organization.name }}' }
];

const TEMPLATE_EXAMPLES = [
  {
    title: 'Device Table with Conditional Columns',
    code: `<table>
  <thead>
    <tr>
      <th>Device Name</th>
      <th>Type</th>
      {% if show_ip_addresses %}
      <th>IP Address</th>
      {% endif %}
      <th>Connections</th>
    </tr>
  </thead>
  <tbody>
    {% for device in shapes %}
    <tr>
      <td>{{ device.name }}</td>
      <td>{{ device.type | title }}</td>
      {% if show_ip_addresses %}
      <td>{{ device.properties.ip_address | default('N/A') }}</td>
      {% endif %}
      <td>{{ device.connections_count }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>`
  },
  {
    title: 'VLAN Summary with Fallbacks',
    code: `{% if vlans %}
<h2>VLAN Configuration</h2>
<p>Total VLANs: {{ vlans | length }}</p>
<ul>
  {% for vlan in vlans %}
  <li>
    VLAN {{ vlan.id }}: {{ vlan.name }}
    {% if vlan.subnet %}({{ vlan.subnet }}){% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
<p>No VLAN configuration found in the network diagram.</p>
{% endif %}`
  },
  {
    title: 'Organization Branding Header',
    code: `<header style="background-color: {{ organization.primary_color }};">
  {% if organization.logo_url %}
  <img src="{{ organization.logo_url }}" alt="{{ organization.name }}" style="height: 60px;">
  {% endif %}
  <div>
    <h1>{{ organization.display_name | default(organization.name) }}</h1>
    <p>{{ project_name }} - {{ title }}</p>
  </div>
</header>`
  },
  {
    title: 'Network Metrics Dashboard',
    code: `<div class="metrics-grid">
  <div class="metric-card">
    <h3>Total Devices</h3>
    <p class="metric-value">{{ shapes | length }}</p>
  </div>
  <div class="metric-card">
    <h3>Connections</h3>
    <p class="metric-value">{{ connections | length }}</p>
  </div>
  <div class="metric-card">
    <h3>Network Density</h3>
    <p class="metric-value">{{ "%.2f"|format(network_density) }}</p>
  </div>
  <div class="metric-card">
    <h3>Most Connected</h3>
    <p class="metric-value">
      {{ most_connected_device.name }}
      ({{ most_connected_device.connections }} links)
    </p>
  </div>
</div>`
  }
];

export default function TemplateVariableReference({ onInsertVariable }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [activeTab, setActiveTab] = useState('variables');
  const [expandedCategories, setExpandedCategories] = useState(['basic']);
  const [expandedExamples, setExpandedExamples] = useState([]);

  const handleCopyVariable = (variable) => {
    const text = `{{ ${variable} }}`;
    navigator.clipboard.writeText(text);
    toast.success(`Copied: ${text}`);
  };

  const handleInsertVariable = (variable) => {
    if (onInsertVariable) {
      onInsertVariable(`{{ ${variable} }}`);
      toast.success(`Inserted: {{ ${variable} }}`);
    }
  };

  const toggleCategory = (category) => {
    setExpandedCategories(prev => 
      prev.includes(category) 
        ? prev.filter(c => c !== category)
        : [...prev, category]
    );
  };

  const toggleExample = (index) => {
    setExpandedExamples(prev => 
      prev.includes(index) 
        ? prev.filter(i => i !== index)
        : [...prev, index]
    );
  };

  const filteredVariables = (category) => {
    if (!VARIABLE_CATEGORIES[category]) return [];
    
    return VARIABLE_CATEGORIES[category].variables.filter(variable =>
      variable.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      variable.description.toLowerCase().includes(searchTerm.toLowerCase())
    );
  };

  const renderVariableType = (variable) => {
    if (variable.isArray) {
      return <span className="inline-block px-2 py-1 text-xs font-medium bg-blue-100 text-blue-700 rounded">Array</span>;
    } else if (variable.isObject) {
      return <span className="inline-block px-2 py-1 text-xs font-medium bg-purple-100 text-purple-700 rounded">Object</span>;
    }
    return null;
  };

  return (
    <div className="space-y-4">
      {/* Search */}
      <div className="relative">
        <FiSearch className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-4 w-4" />
        <input
          type="text"
          placeholder="Search variables..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:ring-primary-500 focus:border-primary-500"
        />
      </div>

      {/* Tabs */}
      <div className="border-b border-gray-200">
        <nav className="-mb-px flex space-x-8">
          <button
            onClick={() => setActiveTab('variables')}
            className={`py-2 px-1 border-b-2 font-medium text-sm ${
              activeTab === 'variables'
                ? 'border-primary-500 text-primary-600'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            }`}
          >
            Variables
          </button>
          <button
            onClick={() => setActiveTab('syntax')}
            className={`py-2 px-1 border-b-2 font-medium text-sm ${
              activeTab === 'syntax'
                ? 'border-primary-500 text-primary-600'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            }`}
          >
            Jinja2 Syntax
          </button>
          <button
            onClick={() => setActiveTab('examples')}
            className={`py-2 px-1 border-b-2 font-medium text-sm ${
              activeTab === 'examples'
                ? 'border-primary-500 text-primary-600'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            }`}
          >
            Examples
          </button>
        </nav>
      </div>

      {/* Content */}
      <div className="space-y-2">
        {activeTab === 'variables' && (
          <>
            {Object.entries(VARIABLE_CATEGORIES).map(([key, category]) => {
              const variables = filteredVariables(key);
              if (variables.length === 0 && searchTerm) return null;
              
              return (
                <div key={key} className="border border-gray-200 rounded-lg">
                  <button
                    onClick={() => toggleCategory(key)}
                    className="w-full px-4 py-3 flex items-center justify-between hover:bg-gray-50"
                  >
                    <div className="flex items-center space-x-3">
                      {category.icon}
                      <span className="font-medium text-gray-900">{category.name}</span>
                      <span className="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800">
                        {variables.length}
                      </span>
                    </div>
                    {expandedCategories.includes(key) ? (
                      <FiChevronDown className="h-4 w-4 text-gray-400" />
                    ) : (
                      <FiChevronRight className="h-4 w-4 text-gray-400" />
                    )}
                  </button>
                  
                  {expandedCategories.includes(key) && (
                    <div className="border-t border-gray-200">
                      <table className="min-w-full divide-y divide-gray-200">
                        <thead className="bg-gray-50">
                          <tr>
                            <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Variable</th>
                            <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
                            <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Type</th>
                            <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
                          </tr>
                        </thead>
                        <tbody className="bg-white divide-y divide-gray-200">
                          {variables.map((variable) => (
                            <tr key={variable.name} className="hover:bg-gray-50">
                              <td className="px-4 py-2 whitespace-nowrap">
                                <code className="text-sm bg-gray-100 px-2 py-1 rounded font-mono">
                                  {variable.name}
                                </code>
                              </td>
                              <td className="px-4 py-2 text-sm text-gray-900">
                                {variable.description}
                                <div className="text-xs text-gray-500 mt-1">
                                  Ex: {variable.example}
                                </div>
                              </td>
                              <td className="px-4 py-2 whitespace-nowrap">
                                {renderVariableType(variable)}
                              </td>
                              <td className="px-4 py-2 whitespace-nowrap">
                                <div className="flex space-x-2">
                                  <button
                                    onClick={() => handleCopyVariable(variable.name)}
                                    className="text-gray-400 hover:text-gray-600"
                                    title="Copy variable"
                                  >
                                    <FiCopy className="h-4 w-4" />
                                  </button>
                                  {onInsertVariable && (
                                    <button
                                      onClick={() => handleInsertVariable(variable.name)}
                                      className="text-gray-400 hover:text-gray-600"
                                      title="Insert variable"
                                    >
                                      <FiCode className="h-4 w-4" />
                                    </button>
                                  )}
                                </div>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  )}
                </div>
              );
            })}
          </>
        )}

        {activeTab === 'syntax' && (
          <div className="space-y-4">
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
              <div className="flex">
                <FiInfo className="h-5 w-5 text-blue-400 mt-0.5" />
                <div className="ml-3">
                  <h3 className="text-sm font-medium text-blue-800">About Jinja2</h3>
                  <p className="mt-1 text-sm text-blue-700">
                    Templates use Jinja2 syntax for dynamic content. Here are the most common constructs:
                  </p>
                </div>
              </div>
            </div>
            
            <div className="overflow-x-auto">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Syntax</th>
                    <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
                    <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Example</th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {JINJA2_CONSTRUCTS.map((construct, index) => (
                    <tr key={index}>
                      <td className="px-4 py-3 whitespace-nowrap">
                        <code className="text-sm bg-gray-100 px-2 py-1 rounded font-mono">
                          {construct.syntax}
                        </code>
                      </td>
                      <td className="px-4 py-3 text-sm text-gray-900">
                        {construct.description}
                      </td>
                      <td className="px-4 py-3">
                        <code className="text-xs bg-gray-100 px-2 py-1 rounded font-mono">
                          {construct.example}
                        </code>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {activeTab === 'examples' && (
          <div className="space-y-3">
            {TEMPLATE_EXAMPLES.map((example, index) => (
              <div key={index} className="border border-gray-200 rounded-lg">
                <button
                  onClick={() => toggleExample(index)}
                  className="w-full px-4 py-3 flex items-center justify-between hover:bg-gray-50 text-left"
                >
                  <span className="font-medium text-gray-900">{example.title}</span>
                  {expandedExamples.includes(index) ? (
                    <FiChevronDown className="h-4 w-4 text-gray-400" />
                  ) : (
                    <FiChevronRight className="h-4 w-4 text-gray-400" />
                  )}
                </button>
                
                {expandedExamples.includes(index) && (
                  <div className="border-t border-gray-200 p-4">
                    <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto text-sm">
                      <code>{example.code}</code>
                    </pre>
                    <div className="mt-3 flex justify-end">
                      <button
                        onClick={() => {
                          navigator.clipboard.writeText(example.code);
                          toast.success('Example copied to clipboard');
                        }}
                        className="inline-flex items-center px-3 py-1 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
                      >
                        <FiCopy className="mr-2 h-4 w-4" />
                        Copy Example
                      </button>
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}