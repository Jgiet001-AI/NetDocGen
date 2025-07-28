import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { FiArrowLeft, FiLoader } from 'react-icons/fi';
import axios from 'axios';
import toast from 'react-hot-toast';
import TemplatePreview from '../components/templates/TemplatePreview';

export default function TemplatePreviewPage() {
  const { templateId } = useParams();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [template, setTemplate] = useState(null);

  useEffect(() => {
    fetchTemplate();
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

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
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
              <FiArrowLeft className="h-5 w-5" />
            </button>
            <div>
              <h1 className="text-xl font-semibold text-gray-900">{template.name}</h1>
              <p className="text-sm text-gray-500">Template Preview</p>
            </div>
          </div>
        </div>
      </div>

      {/* Preview */}
      <div className="flex-1 overflow-hidden">
        <TemplatePreview template={template} />
      </div>
    </div>
  );
}