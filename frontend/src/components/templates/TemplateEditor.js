import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Editor from '@monaco-editor/react';
import {
  FiSave,
  FiEye,
  FiX,
  FiCode,
  FiLayout,
  FiSettings,
  FiFileText,
  FiLoader,
  FiInfo,
  FiBook
} from 'react-icons/fi';
import axios from 'axios';
import toast from 'react-hot-toast';
import TemplatePreview from './TemplatePreview';
import TemplateVariableReference from './TemplateVariableReferenceTailwind';
import SectionConfiguration from './SectionConfiguration';

export default function TemplateEditor() {
  const { templateId } = useParams();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [template, setTemplate] = useState({
    name: '',
    description: '',
    template_type: 'network_documentation',
    html_template: '',
    css_styles: '',
    header_template: '',
    footer_template: '',
    cover_page_template: '',
    template_variables: {},
    section_config: {},
    page_margins: { top: '1in', right: '1in', bottom: '1in', left: '1in' },
    font_config: {},
    color_scheme: {},
    logo_config: {}
  });
  
  const [activeTab, setActiveTab] = useState('html');
  const [activeEditor, setActiveEditor] = useState('main');
  const [showPreview, setShowPreview] = useState(true);
  const [showVariableReference, setShowVariableReference] = useState(false);
  const [previewData, setPreviewData] = useState(null);
  const editorRef = useRef(null);

  const isNewTemplate = templateId === 'new';

  useEffect(() => {
    if (!isNewTemplate) {
      fetchTemplate();
    } else {
      loadDefaultTemplate();
      setLoading(false);
    }
  }, [templateId]);

  const fetchTemplate = async () => {
    try {
      const response = await axios.get(`/api/templates/${templateId}`);
      setTemplate(response.data);
    } catch (error) {
      toast.error('Failed to load template');
      navigate('/settings/templates');
    } finally {
      setLoading(false);
    }
  };

  const loadDefaultTemplate = () => {
    setTemplate({
      ...template,
      html_template: `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>{{ title | default('Network Documentation') }}</title>
  <style>{{ css_styles }}</style>
</head>
<body>
  <!-- Header -->
  {{ header_template }}
  
  <!-- Main Content -->
  <div class="container">
    <h1>{{ project_name }}</h1>
    <p>Customer: {{ customer_name }} ({{ customer_organization }})</p>
    
    <h2>Network Overview</h2>
    <div class="network-summary">
      <p>Total Devices: {{ shapes | length }}</p>
      <p>Total Connections: {{ connections | length }}</p>
    </div>
    
    <h2>Device List</h2>
    <table class="device-table">
      <thead>
        <tr>
          <th>Device Name</th>
          <th>Type</th>
          <th>Connections</th>
        </tr>
      </thead>
      <tbody>
        {% for shape in shapes %}
        <tr>
          <td>{{ shape.name }}</td>
          <td>{{ shape.type }}</td>
          <td>{{ shape.connections_count }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
  
  <!-- Footer -->
  {{ footer_template }}
</body>
</html>`,
      css_styles: `body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  margin: 0;
  padding: 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

h1, h2, h3 {
  color: var(--primary-color, #1e3c72);
}

.device-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.device-table th,
.device-table td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
}

.device-table th {
  background-color: #f4f4f4;
  font-weight: bold;
}

.device-table tr:nth-child(even) {
  background-color: #f9f9f9;
}`,
      header_template: `<header class="document-header">
  <div class="header-content">
    {% if organization.logo_url %}
    <img src="{{ organization.logo_url }}" alt="{{ organization.name }}" class="logo">
    {% endif %}
    <div class="header-text">
      <h3>{{ organization.display_name | default(organization.name) }}</h3>
      <p>{{ organization.address_line1 }}, {{ organization.city }}, {{ organization.state }} {{ organization.postal_code }}</p>
    </div>
  </div>
</header>`,
      footer_template: `<footer class="document-footer">
  <div class="footer-content">
    <p>Page <span class="page-number"></span></p>
    <p>{{ organization.name }} - Confidential</p>
    <p>Generated: {{ generated_date }}</p>
  </div>
</footer>`
    });
  };

  const handleSave = async () => {
    setSaving(true);
    try {
      if (isNewTemplate) {
        const orgResponse = await axios.get('/api/organizations/current');
        const organizationId = orgResponse.data.id;
        
        const response = await axios.post('/api/templates', {
          ...template,
          organization_id: organizationId
        });
        toast.success('Template created successfully');
        navigate(`/settings/templates/${response.data.id}/edit`);
      } else {
        await axios.put(`/api/templates/${templateId}`, template);
        toast.success('Template saved successfully');
      }
    } catch (error) {
      toast.error('Failed to save template');
    } finally {
      setSaving(false);
    }
  };

  const getEditorContent = () => {
    switch (activeEditor) {
      case 'header':
        return template.header_template || '';
      case 'footer':
        return template.footer_template || '';
      case 'cover':
        return template.cover_page_template || '';
      default:
        return activeTab === 'html' ? template.html_template : template.css_styles;
    }
  };

  const handleEditorChange = (value) => {
    const updates = { ...template };
    
    switch (activeEditor) {
      case 'header':
        updates.header_template = value;
        break;
      case 'footer':
        updates.footer_template = value;
        break;
      case 'cover':
        updates.cover_page_template = value;
        break;
      default:
        if (activeTab === 'html') {
          updates.html_template = value;
        } else {
          updates.css_styles = value;
        }
    }
    
    setTemplate(updates);
  };

  const handleInsertVariable = (variable) => {
    const editor = editorRef.current;
    if (editor) {
      const position = editor.getPosition();
      const range = {
        startLineNumber: position.lineNumber,
        startColumn: position.column,
        endLineNumber: position.lineNumber,
        endColumn: position.column
      };
      editor.executeEdits('', [
        {
          range: range,
          text: variable,
          forceMoveMarkers: true
        }
      ]);
      editor.focus();
    }
  };

  const handleEditorDidMount = (editor) => {
    editorRef.current = editor;
  };

  const editorOptions = {
    minimap: { enabled: false },
    fontSize: 14,
    wordWrap: 'on',
    lineNumbers: 'on',
    scrollBeyondLastLine: false,
    automaticLayout: true,
    tabSize: 2
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <FiLoader className="h-8 w-8 animate-spin text-primary-600" />
      </div>
    );
  }

  return (
    <div className="h-screen flex flex-col bg-gray-50">
      {/* Header */}
      <div className="bg-white border-b border-gray-200 px-6 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <button
              onClick={() => navigate('/settings/templates')}
              className="text-gray-500 hover:text-gray-700"
            >
              <FiX className="h-5 w-5" />
            </button>
            <div>
              <input
                type="text"
                value={template.name}
                onChange={(e) => setTemplate({ ...template, name: e.target.value })}
                placeholder="Template Name"
                className="text-xl font-semibold bg-transparent border-none focus:outline-none focus:ring-0"
              />
              <input
                type="text"
                value={template.description}
                onChange={(e) => setTemplate({ ...template, description: e.target.value })}
                placeholder="Template description..."
                className="block text-sm text-gray-500 bg-transparent border-none focus:outline-none focus:ring-0 w-full"
              />
            </div>
          </div>
          
          <div className="flex items-center space-x-3">
            <button
              onClick={() => setShowVariableReference(!showVariableReference)}
              className={`inline-flex items-center px-3 py-2 border rounded-md text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 ${
                showVariableReference 
                  ? 'border-primary-500 text-primary-700 bg-primary-50' 
                  : 'border-gray-300 text-gray-700 bg-white hover:bg-gray-50'
              }`}
            >
              <FiBook className="mr-2 h-4 w-4" />
              Variables
            </button>
            
            <button
              onClick={() => setShowPreview(!showPreview)}
              className={`inline-flex items-center px-3 py-2 border rounded-md text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 ${
                showPreview 
                  ? 'border-primary-500 text-primary-700 bg-primary-50' 
                  : 'border-gray-300 text-gray-700 bg-white hover:bg-gray-50'
              }`}
            >
              <FiEye className="mr-2 h-4 w-4" />
              Preview
            </button>
            
            <button
              onClick={handleSave}
              disabled={saving || !template.name}
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
                  Save
                </>
              )}
            </button>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex overflow-hidden">
        {/* Variable Reference Panel */}
        {showVariableReference && (
          <div className="w-96 border-r border-gray-200 bg-white overflow-y-auto">
            <div className="sticky top-0 bg-white border-b border-gray-200 px-4 py-3 flex items-center justify-between">
              <h3 className="text-sm font-medium text-gray-900">Variable Reference</h3>
              <button
                onClick={() => setShowVariableReference(false)}
                className="text-gray-400 hover:text-gray-500"
              >
                <FiX className="h-4 w-4" />
              </button>
            </div>
            <div className="p-4">
              <TemplateVariableReference onInsertVariable={handleInsertVariable} />
            </div>
          </div>
        )}
        
        {/* Editor Panel */}
        <div className={`flex-1 flex flex-col ${showPreview && !showVariableReference ? 'w-1/2' : ''}`}>
          {/* Editor Tabs */}
          <div className="bg-white border-b border-gray-200">
            <div className="flex items-center justify-between px-4">
              <div className="flex space-x-6">
                <button
                  onClick={() => setActiveTab('html')}
                  className={`py-3 px-1 border-b-2 font-medium text-sm transition-colors ${
                    activeTab === 'html'
                      ? 'border-primary-500 text-primary-600'
                      : 'border-transparent text-gray-500 hover:text-gray-700'
                  }`}
                >
                  <FiCode className="inline mr-2" />
                  HTML Template
                </button>
                <button
                  onClick={() => setActiveTab('css')}
                  className={`py-3 px-1 border-b-2 font-medium text-sm transition-colors ${
                    activeTab === 'css'
                      ? 'border-primary-500 text-primary-600'
                      : 'border-transparent text-gray-500 hover:text-gray-700'
                  }`}
                >
                  <FiLayout className="inline mr-2" />
                  CSS Styles
                </button>
                <button
                  onClick={() => setActiveTab('sections')}
                  className={`py-3 px-1 border-b-2 font-medium text-sm transition-colors ${
                    activeTab === 'sections'
                      ? 'border-primary-500 text-primary-600'
                      : 'border-transparent text-gray-500 hover:text-gray-700'
                  }`}
                >
                  <FiSettings className="inline mr-2" />
                  Sections
                </button>
              </div>
              
              {activeTab === 'html' && (
                <select
                  value={activeEditor}
                  onChange={(e) => setActiveEditor(e.target.value)}
                  className="text-sm border-gray-300 rounded-md"
                >
                  <option value="main">Main Template</option>
                  <option value="header">Header Template</option>
                  <option value="footer">Footer Template</option>
                  <option value="cover">Cover Page</option>
                </select>
              )}
            </div>
          </div>

          {/* Monaco Editor or Section Configuration */}
          {activeTab !== 'sections' ? (
            <div className="flex-1 relative">
              <Editor
                language={activeTab === 'html' ? 'html' : 'css'}
                value={getEditorContent()}
                onChange={handleEditorChange}
                onMount={handleEditorDidMount}
                options={editorOptions}
                theme="vs-light"
              />
            </div>
          ) : (
            <div className="flex-1 overflow-y-auto p-6">
              <SectionConfiguration
                sections={template.section_config}
                onChange={(newSections) => setTemplate({ ...template, section_config: newSections })}
              />
            </div>
          )}

        </div>

        {/* Preview Panel */}
        {showPreview && (
          <div className={`${showVariableReference ? 'flex-1' : 'w-1/2'} border-l border-gray-200 bg-white overflow-hidden`}>
            <TemplatePreview
              template={template}
              previewData={previewData}
            />
          </div>
        )}
      </div>
    </div>
  );
}