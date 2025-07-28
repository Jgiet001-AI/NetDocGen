import React, { useState, useEffect, useRef } from 'react';
import {
  FiRefreshCw,
  FiDownload,
  FiMaximize2,
  FiMinimize2,
  FiSmartphone,
  FiTablet,
  FiMonitor,
  FiLoader
} from 'react-icons/fi';
import axios from 'axios';
import toast from 'react-hot-toast';

export default function TemplatePreview({ template, previewData: externalData }) {
  const iframeRef = useRef(null);
  const [loading, setLoading] = useState(false);
  const [viewMode, setViewMode] = useState('desktop');
  const [fullscreen, setFullscreen] = useState(false);
  const [renderedHtml, setRenderedHtml] = useState('');
  
  // Default sample data
  const defaultSampleData = {
    title: 'Network Infrastructure Documentation',
    project_name: 'Corporate Network Upgrade',
    generated_date: new Date().toLocaleDateString(),
    version: '1.0',
    customer_name: 'John Smith',
    customer_organization: 'Acme Corporation',
    customer_contact_name: 'Jane Doe',
    customer_contact_email: 'jane.doe@acme.com',
    customer_contact_phone: '+1 (555) 123-4567',
    project_code: 'PRJ-2025-001',
    project_manager: 'Alice Johnson',
    organization: {
      name: 'NetDocGen Solutions',
      display_name: 'NetDocGen Solutions Inc.',
      logo_url: '/logo-placeholder.png',
      primary_color: '#1e3c72',
      secondary_color: '#2a5298',
      accent_color: '#4CAF50',
      address_line1: '123 Tech Street',
      city: 'San Francisco',
      state: 'CA',
      postal_code: '94105'
    },
    shapes: [
      { 
        name: 'Core-Switch-01', 
        type: 'switch', 
        connections_count: 12,
        properties: {
          model: 'Cisco Catalyst 9300',
          ip_address: '10.0.1.1',
          location: 'Data Center Rack A1'
        }
      },
      { 
        name: 'Firewall-01', 
        type: 'firewall', 
        connections_count: 4,
        properties: {
          model: 'Palo Alto PA-850',
          ip_address: '10.0.0.1',
          location: 'Data Center Rack A2'
        }
      },
      { 
        name: 'Router-01', 
        type: 'router', 
        connections_count: 3,
        properties: {
          model: 'Cisco ISR 4451',
          ip_address: '10.0.0.254',
          location: 'Data Center Rack A3'
        }
      },
      { 
        name: 'Access-Switch-01', 
        type: 'switch', 
        connections_count: 24,
        properties: {
          model: 'Cisco Catalyst 2960',
          ip_address: '10.0.2.1',
          location: 'Floor 1 IDF'
        }
      }
    ],
    connections: [
      { 
        source_name: 'Core-Switch-01', 
        target_name: 'Firewall-01', 
        connection_type: '10G Ethernet',
        vlan: '100'
      },
      { 
        source_name: 'Firewall-01', 
        target_name: 'Router-01', 
        connection_type: '1G Ethernet',
        vlan: '200'
      },
      { 
        source_name: 'Core-Switch-01', 
        target_name: 'Access-Switch-01', 
        connection_type: '1G Ethernet Trunk',
        vlan: 'All'
      }
    ],
    vlans: [
      { id: 100, name: 'Management', subnet: '10.0.1.0/24' },
      { id: 200, name: 'DMZ', subnet: '10.0.200.0/24' },
      { id: 300, name: 'Users', subnet: '10.0.3.0/24' },
      { id: 400, name: 'Servers', subnet: '10.0.4.0/24' }
    ],
    network_summary: 'This network infrastructure consists of a hierarchical design with core switching, firewall protection, and distributed access layer. The topology provides redundancy and scalability for future growth.'
  };

  const previewData = externalData || defaultSampleData;

  useEffect(() => {
    renderTemplate();
  }, [template, previewData]);

  const renderTemplate = async () => {
    setLoading(true);
    try {
      // Simulate server-side rendering (in production, this would be an API call)
      const html = await renderJinja2Template(
        template.html_template,
        previewData,
        template
      );
      setRenderedHtml(html);
      updateIframe(html);
    } catch (error) {
      console.error('Template rendering error:', error);
      setRenderedHtml(`<div style="color: red; padding: 20px;">Error rendering template: ${error.message}</div>`);
    } finally {
      setLoading(false);
    }
  };

  // Simple client-side Jinja2-like template rendering
  const renderJinja2Template = async (templateStr, data, templateConfig) => {
    let html = templateStr || '<p>No template content</p>';
    
    // Replace header and footer templates
    if (templateConfig.header_template) {
      html = html.replace('{{ header_template }}', templateConfig.header_template);
    }
    if (templateConfig.footer_template) {
      html = html.replace('{{ footer_template }}', templateConfig.footer_template);
    }
    
    // Replace CSS styles
    html = html.replace('{{ css_styles }}', templateConfig.css_styles || '');
    
    // Simple variable replacement
    const replaceVariables = (str, obj, prefix = '') => {
      Object.entries(obj).forEach(([key, value]) => {
        const varPattern = new RegExp(`{{ ${prefix}${key} }}`, 'g');
        const varPatternDefault = new RegExp(`{{ ${prefix}${key} \\| default\\('([^']*)'\\) }}`, 'g');
        
        if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
          str = replaceVariables(str, value, `${prefix}${key}.`);
        } else if (Array.isArray(value)) {
          // Handle arrays (simplified - in production, use proper templating)
          str = str.replace(varPattern, JSON.stringify(value));
        } else {
          str = str.replace(varPatternDefault, value || '$1');
          str = str.replace(varPattern, value || '');
        }
      });
      return str;
    };
    
    html = replaceVariables(html, data);
    
    // Handle for loops (simplified)
    const forLoopPattern = /{% for (\w+) in (\w+) %}([\s\S]*?){% endfor %}/g;
    html = html.replace(forLoopPattern, (match, itemName, arrayName, loopContent) => {
      const array = data[arrayName] || [];
      return array.map(item => {
        let content = loopContent;
        Object.entries(item).forEach(([key, value]) => {
          content = content.replace(new RegExp(`{{ ${itemName}.${key} }}`, 'g'), value);
        });
        return content;
      }).join('');
    });
    
    // Handle length filter
    html = html.replace(/{{ (\w+) \| length }}/g, (match, varName) => {
      const value = data[varName];
      return Array.isArray(value) ? value.length : 0;
    });
    
    // Add CSS variables for branding
    const brandingStyles = `
      <style>
        :root {
          --primary-color: ${data.organization?.primary_color || '#1e3c72'};
          --secondary-color: ${data.organization?.secondary_color || '#2a5298'};
          --accent-color: ${data.organization?.accent_color || '#4CAF50'};
        }
      </style>
    `;
    html = html.replace('</head>', `${brandingStyles}</head>`);
    
    return html;
  };

  const updateIframe = (html) => {
    if (iframeRef.current) {
      const doc = iframeRef.current.contentDocument;
      doc.open();
      doc.write(html);
      doc.close();
    }
  };

  const handleDownload = () => {
    const blob = new Blob([renderedHtml], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${template.name || 'template'}_preview.html`;
    a.click();
    URL.revokeObjectURL(url);
    toast.success('Preview downloaded');
  };

  const getViewportStyle = () => {
    switch (viewMode) {
      case 'mobile':
        return { width: '375px', height: '667px', margin: '0 auto' };
      case 'tablet':
        return { width: '768px', height: '1024px', margin: '0 auto' };
      default:
        return { width: '100%', height: '100%' };
    }
  };

  return (
    <div className={`flex flex-col h-full ${fullscreen ? 'fixed inset-0 z-50 bg-white' : ''}`}>
      {/* Preview Controls */}
      <div className="bg-gray-50 border-b border-gray-200 px-4 py-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <div className="flex items-center bg-white border border-gray-300 rounded-md">
              <button
                onClick={() => setViewMode('desktop')}
                className={`px-3 py-1.5 text-sm ${
                  viewMode === 'desktop' 
                    ? 'bg-primary-50 text-primary-700' 
                    : 'text-gray-600 hover:text-gray-900'
                }`}
                title="Desktop view"
              >
                <FiMonitor className="h-4 w-4" />
              </button>
              <button
                onClick={() => setViewMode('tablet')}
                className={`px-3 py-1.5 text-sm border-l border-r border-gray-300 ${
                  viewMode === 'tablet' 
                    ? 'bg-primary-50 text-primary-700' 
                    : 'text-gray-600 hover:text-gray-900'
                }`}
                title="Tablet view"
              >
                <FiTablet className="h-4 w-4" />
              </button>
              <button
                onClick={() => setViewMode('mobile')}
                className={`px-3 py-1.5 text-sm ${
                  viewMode === 'mobile' 
                    ? 'bg-primary-50 text-primary-700' 
                    : 'text-gray-600 hover:text-gray-900'
                }`}
                title="Mobile view"
              >
                <FiSmartphone className="h-4 w-4" />
              </button>
            </div>
            
            <span className="text-sm text-gray-500">
              Preview Mode: {viewMode.charAt(0).toUpperCase() + viewMode.slice(1)}
            </span>
          </div>
          
          <div className="flex items-center space-x-2">
            <button
              onClick={renderTemplate}
              disabled={loading}
              className="p-2 text-gray-600 hover:text-gray-900 disabled:opacity-50"
              title="Refresh preview"
            >
              <FiRefreshCw className={`h-4 w-4 ${loading ? 'animate-spin' : ''}`} />
            </button>
            
            <button
              onClick={handleDownload}
              className="p-2 text-gray-600 hover:text-gray-900"
              title="Download preview"
            >
              <FiDownload className="h-4 w-4" />
            </button>
            
            <button
              onClick={() => setFullscreen(!fullscreen)}
              className="p-2 text-gray-600 hover:text-gray-900"
              title={fullscreen ? 'Exit fullscreen' : 'Enter fullscreen'}
            >
              {fullscreen ? <FiMinimize2 className="h-4 w-4" /> : <FiMaximize2 className="h-4 w-4" />}
            </button>
          </div>
        </div>
      </div>

      {/* Preview Content */}
      <div className="flex-1 bg-gray-100 overflow-auto p-4">
        {loading ? (
          <div className="flex items-center justify-center h-full">
            <FiLoader className="h-8 w-8 animate-spin text-gray-400" />
          </div>
        ) : (
          <div style={getViewportStyle()} className="bg-white shadow-lg">
            <iframe
              ref={iframeRef}
              className="w-full h-full border-0"
              title="Template Preview"
              sandbox="allow-same-origin"
            />
          </div>
        )}
      </div>
    </div>
  );
}