import React, { useState } from 'react';
import {
  FiMove,
  FiEye,
  FiEyeOff,
  FiSettings,
  FiChevronDown,
  FiChevronRight,
  FiPlus,
  FiTrash2,
  FiEdit2,
  FiCheck,
  FiX
} from 'react-icons/fi';
import { DndContext, closestCenter, KeyboardSensor, PointerSensor, useSensor, useSensors } from '@dnd-kit/core';
import { arrayMove, SortableContext, sortableKeyboardCoordinates, verticalListSortingStrategy } from '@dnd-kit/sortable';
import { useSortable } from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';
import toast from 'react-hot-toast';

const DEFAULT_SECTIONS = [
  {
    id: 'cover',
    name: 'Cover Page',
    description: 'Title page with project and customer information',
    enabled: true,
    required: false,
    settings: {
      showLogo: true,
      showDate: true,
      showVersion: true,
      backgroundColor: 'gradient'
    }
  },
  {
    id: 'toc',
    name: 'Table of Contents',
    description: 'Automatically generated table of contents',
    enabled: true,
    required: false,
    settings: {
      maxDepth: 3,
      showPageNumbers: true
    }
  },
  {
    id: 'executive_summary',
    name: 'Executive Summary',
    description: 'High-level overview for stakeholders',
    enabled: true,
    required: false,
    settings: {
      showMetrics: true,
      showKeyFindings: true
    }
  },
  {
    id: 'network_overview',
    name: 'Network Overview',
    description: 'Overall network architecture and statistics',
    enabled: true,
    required: true,
    settings: {
      showTopology: true,
      showStatistics: true,
      showDiagram: true
    }
  },
  {
    id: 'device_inventory',
    name: 'Device Inventory',
    description: 'Detailed list of all network devices',
    enabled: true,
    required: true,
    settings: {
      groupByType: true,
      showProperties: true,
      showConnections: true,
      showIPAddresses: true
    }
  },
  {
    id: 'connections',
    name: 'Network Connections',
    description: 'Connection matrix and details',
    enabled: true,
    required: true,
    settings: {
      showMatrix: false,
      showTable: true,
      showVLANs: true
    }
  },
  {
    id: 'vlans',
    name: 'VLAN Configuration',
    description: 'VLAN details and assignments',
    enabled: true,
    required: false,
    settings: {
      showSubnets: true,
      showGateways: true,
      showDHCP: true
    }
  },
  {
    id: 'analysis',
    name: 'Network Analysis',
    description: 'AI-powered insights and recommendations',
    enabled: true,
    required: false,
    settings: {
      showRecommendations: true,
      showRisks: true,
      showOptimizations: true
    }
  },
  {
    id: 'appendix',
    name: 'Appendix',
    description: 'Additional technical details and references',
    enabled: false,
    required: false,
    settings: {
      showGlossary: true,
      showReferences: true
    }
  }
];

function SortableSection({ section, onToggle, onEdit, onDelete, onSettingsChange }) {
  const [isExpanded, setIsExpanded] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [editName, setEditName] = useState(section.name);
  
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition,
    isDragging
  } = useSortable({ id: section.id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    opacity: isDragging ? 0.5 : 1
  };

  const handleSave = () => {
    onEdit(section.id, { name: editName });
    setIsEditing(false);
  };

  const handleCancel = () => {
    setEditName(section.name);
    setIsEditing(false);
  };

  return (
    <div
      ref={setNodeRef}
      style={style}
      className={`bg-white border rounded-lg ${isDragging ? 'shadow-lg' : 'shadow-sm'}`}
    >
      <div className="p-4">
        <div className="flex items-start justify-between">
          <div className="flex items-start space-x-3 flex-1">
            <button
              {...attributes}
              {...listeners}
              className="mt-1 text-gray-400 hover:text-gray-600 cursor-move"
            >
              <FiMove className="h-5 w-5" />
            </button>
            
            <div className="flex-1">
              <div className="flex items-center space-x-2">
                {isEditing ? (
                  <div className="flex items-center space-x-2 flex-1">
                    <input
                      type="text"
                      value={editName}
                      onChange={(e) => setEditName(e.target.value)}
                      className="flex-1 px-2 py-1 border border-gray-300 rounded-md focus:ring-primary-500 focus:border-primary-500"
                      autoFocus
                    />
                    <button
                      onClick={handleSave}
                      className="text-green-600 hover:text-green-700"
                    >
                      <FiCheck className="h-4 w-4" />
                    </button>
                    <button
                      onClick={handleCancel}
                      className="text-gray-400 hover:text-gray-600"
                    >
                      <FiX className="h-4 w-4" />
                    </button>
                  </div>
                ) : (
                  <>
                    <h3 className="text-sm font-medium text-gray-900">
                      {section.name}
                    </h3>
                    {section.required && (
                      <span className="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-gray-100 text-gray-600">
                        Required
                      </span>
                    )}
                    {!section.enabled && (
                      <span className="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-yellow-100 text-yellow-800">
                        Disabled
                      </span>
                    )}
                  </>
                )}
              </div>
              <p className="mt-1 text-sm text-gray-500">{section.description}</p>
            </div>
          </div>
          
          <div className="flex items-center space-x-2 ml-4">
            <button
              onClick={() => onToggle(section.id)}
              className={`p-1 rounded ${
                section.enabled
                  ? 'text-green-600 hover:text-green-700'
                  : 'text-gray-400 hover:text-gray-600'
              }`}
              disabled={section.required}
              title={section.required ? 'This section is required' : 'Toggle section'}
            >
              {section.enabled ? <FiEye className="h-4 w-4" /> : <FiEyeOff className="h-4 w-4" />}
            </button>
            
            <button
              onClick={() => setIsExpanded(!isExpanded)}
              className="p-1 text-gray-400 hover:text-gray-600"
            >
              {isExpanded ? <FiChevronDown className="h-4 w-4" /> : <FiChevronRight className="h-4 w-4" />}
            </button>
            
            {!section.required && (
              <>
                <button
                  onClick={() => setIsEditing(true)}
                  className="p-1 text-gray-400 hover:text-gray-600"
                >
                  <FiEdit2 className="h-4 w-4" />
                </button>
                <button
                  onClick={() => onDelete(section.id)}
                  className="p-1 text-red-400 hover:text-red-600"
                >
                  <FiTrash2 className="h-4 w-4" />
                </button>
              </>
            )}
          </div>
        </div>
        
        {isExpanded && section.settings && (
          <div className="mt-4 pl-8 space-y-3">
            <h4 className="text-sm font-medium text-gray-700 flex items-center">
              <FiSettings className="mr-2 h-4 w-4" />
              Section Settings
            </h4>
            {Object.entries(section.settings).map(([key, value]) => (
              <div key={key} className="flex items-center justify-between">
                <label className="text-sm text-gray-600">
                  {key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase())}
                </label>
                <input
                  type="checkbox"
                  checked={value}
                  onChange={(e) => onSettingsChange(section.id, key, e.target.checked)}
                  className="h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded"
                />
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default function SectionConfiguration({ sections: initialSections, onChange }) {
  const [sections, setSections] = useState(initialSections || DEFAULT_SECTIONS);
  const [showAddSection, setShowAddSection] = useState(false);
  const [newSection, setNewSection] = useState({
    name: '',
    description: '',
    enabled: true
  });

  const sensors = useSensors(
    useSensor(PointerSensor),
    useSensor(KeyboardSensor, {
      coordinateGetter: sortableKeyboardCoordinates,
    })
  );

  const handleDragEnd = (event) => {
    const { active, over } = event;

    if (active.id !== over.id) {
      setSections((items) => {
        const oldIndex = items.findIndex(item => item.id === active.id);
        const newIndex = items.findIndex(item => item.id === over.id);
        const newItems = arrayMove(items, oldIndex, newIndex);
        onChange?.(newItems);
        return newItems;
      });
    }
  };

  const handleToggle = (sectionId) => {
    setSections(prev => {
      const newSections = prev.map(section =>
        section.id === sectionId
          ? { ...section, enabled: !section.enabled }
          : section
      );
      onChange?.(newSections);
      return newSections;
    });
  };

  const handleEdit = (sectionId, updates) => {
    setSections(prev => {
      const newSections = prev.map(section =>
        section.id === sectionId
          ? { ...section, ...updates }
          : section
      );
      onChange?.(newSections);
      return newSections;
    });
  };

  const handleDelete = (sectionId) => {
    setSections(prev => {
      const newSections = prev.filter(section => section.id !== sectionId);
      onChange?.(newSections);
      toast.success('Section removed');
      return newSections;
    });
  };

  const handleSettingsChange = (sectionId, key, value) => {
    setSections(prev => {
      const newSections = prev.map(section =>
        section.id === sectionId
          ? { ...section, settings: { ...section.settings, [key]: value } }
          : section
      );
      onChange?.(newSections);
      return newSections;
    });
  };

  const handleAddSection = () => {
    if (!newSection.name) {
      toast.error('Section name is required');
      return;
    }

    const section = {
      id: `custom_${Date.now()}`,
      name: newSection.name,
      description: newSection.description,
      enabled: newSection.enabled,
      required: false,
      settings: {}
    };

    setSections(prev => {
      const newSections = [...prev, section];
      onChange?.(newSections);
      return newSections;
    });

    setNewSection({ name: '', description: '', enabled: true });
    setShowAddSection(false);
    toast.success('Section added');
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-lg font-medium text-gray-900">Section Configuration</h3>
          <p className="mt-1 text-sm text-gray-500">
            Drag sections to reorder, toggle visibility, and configure settings
          </p>
        </div>
        <button
          onClick={() => setShowAddSection(true)}
          className="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm leading-4 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
        >
          <FiPlus className="mr-2 h-4 w-4" />
          Add Section
        </button>
      </div>

      <DndContext
        sensors={sensors}
        collisionDetection={closestCenter}
        onDragEnd={handleDragEnd}
      >
        <SortableContext
          items={sections.map(s => s.id)}
          strategy={verticalListSortingStrategy}
        >
          <div className="space-y-3">
            {sections.map(section => (
              <SortableSection
                key={section.id}
                section={section}
                onToggle={handleToggle}
                onEdit={handleEdit}
                onDelete={handleDelete}
                onSettingsChange={handleSettingsChange}
              />
            ))}
          </div>
        </SortableContext>
      </DndContext>

      {/* Add Section Dialog */}
      {showAddSection && (
        <div className="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 max-w-md w-full">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Add Custom Section</h3>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700">
                  Section Name
                </label>
                <input
                  type="text"
                  value={newSection.name}
                  onChange={(e) => setNewSection({ ...newSection, name: e.target.value })}
                  className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  placeholder="e.g., Security Analysis"
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700">
                  Description
                </label>
                <textarea
                  value={newSection.description}
                  onChange={(e) => setNewSection({ ...newSection, description: e.target.value })}
                  rows={3}
                  className="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                  placeholder="Brief description of the section content"
                />
              </div>
              
              <div className="flex items-center">
                <input
                  type="checkbox"
                  id="enabled"
                  checked={newSection.enabled}
                  onChange={(e) => setNewSection({ ...newSection, enabled: e.target.checked })}
                  className="h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded"
                />
                <label htmlFor="enabled" className="ml-2 block text-sm text-gray-900">
                  Enable section by default
                </label>
              </div>
            </div>
            
            <div className="mt-6 flex justify-end space-x-3">
              <button
                onClick={() => setShowAddSection(false)}
                className="px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
              >
                Cancel
              </button>
              <button
                onClick={handleAddSection}
                className="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
              >
                Add Section
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}