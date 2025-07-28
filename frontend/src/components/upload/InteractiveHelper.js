import React, { useState, useEffect } from 'react';
import { 
  ChatBubbleLeftRightIcon, 
  PaperClipIcon,
  CpuChipIcon,
  CircleStackIcon,
  GlobeAltIcon,
  CubeIcon,
  CubeTransparentIcon,
  BuildingOfficeIcon,
  ShieldCheckIcon,
  WifiIcon,
  SparklesIcon,
  QuestionMarkCircleIcon,
  ArrowRightIcon,
  ArrowLeftIcon,
  CheckCircleIcon,
  ClockIcon,
  InformationCircleIcon,
  LightBulbIcon
} from '@heroicons/react/24/outline';
import axios from 'axios';
import toast from 'react-hot-toast';

const InteractiveHelper = ({ documentId, missingInfo, onComplete }) => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState({});
  const [supplementalFiles, setSupplementalFiles] = useState({});
  const [isProcessing, setIsProcessing] = useState(false);
  const [suggestions, setSuggestions] = useState([]);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [autoFillAvailable, setAutoFillAvailable] = useState(false);

  // Network topology icons mapping
  const topologyIcons = {
    collapsed_core: CircleStackIcon,
    three_tier: CubeIcon,
    spine_leaf: CubeTransparentIcon,
    hub_spoke: GlobeAltIcon,
    mesh: CpuChipIcon,
    star: CpuChipIcon,
    ring: CpuChipIcon,
    bus: CpuChipIcon,
    hybrid: CubeTransparentIcon,
    dmz: ShieldCheckIcon,
    campus: BuildingOfficeIcon,
    wan: WifiIcon,
    not_sure: SparklesIcon,
    other: QuestionMarkCircleIcon
  };

  const questions = [
    {
      id: 'network_design',
      question: 'What network design pattern is used in this infrastructure?',
      type: 'select',
      options: [
        { 
          value: 'collapsed_core', 
          label: 'Collapsed Core',
          description: 'Core + Distribution combined',
          icon: topologyIcons.collapsed_core
        },
        { 
          value: 'three_tier', 
          label: 'Three-Tier',
          description: 'Core, Distribution, Access layers',
          icon: topologyIcons.three_tier
        },
        { 
          value: 'spine_leaf', 
          label: 'Spine-Leaf',
          description: 'Modern data center design',
          icon: topologyIcons.spine_leaf
        },
        { 
          value: 'hub_spoke', 
          label: 'Hub and Spoke',
          description: 'Central hub with branches',
          icon: topologyIcons.hub_spoke
        },
        { 
          value: 'mesh', 
          label: 'Mesh Network',
          description: 'Full or partial mesh topology',
          icon: topologyIcons.mesh
        },
        { 
          value: 'dmz', 
          label: 'DMZ/Security',
          description: 'Security-focused architecture',
          icon: topologyIcons.dmz
        },
        { 
          value: 'campus', 
          label: 'Campus Network',
          description: 'Multi-building enterprise',
          icon: topologyIcons.campus
        },
        { 
          value: 'wan', 
          label: 'WAN/Branch',
          description: 'Wide area network',
          icon: topologyIcons.wan
        },
        { 
          value: 'not_sure', 
          label: 'Let AI Analyze',
          description: 'AI will detect the pattern',
          icon: topologyIcons.not_sure,
          highlight: true
        }
      ],
      help: 'Select the network architecture that best matches your diagram. This helps organize the documentation.',
      required: true,
      allowNotSure: true,
      estimatedTime: '30 seconds'
    },
    {
      id: 'vlan_list',
      question: 'Do you have a VLAN list document?',
      type: 'file_or_text',
      placeholder: 'Paste VLAN information or upload a file',
      fileTypes: ['.csv', '.xlsx', '.txt'],
      textFormat: 'VLAN ID, Name, Description\n10, Management, Network Management\n20, Users, User Access',
      help: 'VLAN information helps document network segmentation',
      required: false
    },
    {
      id: 'device_details',
      question: 'Can you provide additional device details?',
      type: 'table',
      columns: [
        { key: 'name', label: 'Device Name', required: true },
        { key: 'model', label: 'Model', required: true, allowNotSure: true },
        { key: 'ip', label: 'Management IP', required: false },
        { key: 'role', label: 'Role', required: true, allowNotSure: true, 
          options: ['Core Switch', 'Distribution Switch', 'Access Switch', 'Router', 'Firewall', 'Load Balancer', 'Server', 'Wireless Controller', 'Not Sure'] }
      ],
      help: 'Fill in any missing device information from your diagram. Use "Not Sure" for fields where AI should infer the information.',
      required: false,
      allowNotSure: true
    },
    {
      id: 'port_channels',
      question: 'Are there any port channels or link aggregations?',
      type: 'dynamic_list',
      fields: [
        { key: 'name', label: 'Port Channel Name', placeholder: 'e.g., Po1' },
        { key: 'members', label: 'Member Interfaces', placeholder: 'e.g., Gi1/0/1, Gi1/0/2' },
        { key: 'protocol', label: 'Protocol', options: ['LACP', 'PAgP', 'Static'] },
        { key: 'devices', label: 'Connected Devices', placeholder: 'e.g., CORE-SW-01 to DIST-SW-01' }
      ],
      help: 'Document aggregated links for redundancy and bandwidth',
      required: false
    },
    {
      id: 'missing_connections',
      question: 'Are there any logical connections not shown in the diagram?',
      type: 'connections',
      help: 'Add VPN tunnels, wireless links, or other logical connections',
      required: false
    },
    {
      id: 'site_details',
      question: 'Can you provide site/location details?',
      type: 'text',
      multiline: true,
      placeholder: 'Describe physical locations, buildings, floors, rack locations, etc.',
      help: 'Physical location information for documentation',
      required: false
    }
  ];

  // Filter questions based on what's missing
  const relevantQuestions = questions.filter(q => {
    if (missingInfo?.includes(q.id)) return true;
    if (q.required) return true;
    return false;
  });

  const currentQ = relevantQuestions[currentQuestion];
  
  // Calculate estimated time remaining
  const calculateTimeRemaining = () => {
    const remainingQuestions = relevantQuestions.length - currentQuestion;
    const avgTimePerQuestion = 30; // seconds
    return Math.ceil(remainingQuestions * avgTimePerQuestion / 60);
  };
  
  // Keyboard shortcuts
  useEffect(() => {
    const handleKeyPress = (e) => {
      if (currentQ?.type === 'select' && currentQ.id === 'network_design') {
        const keyNum = parseInt(e.key);
        if (keyNum >= 1 && keyNum <= 9 && currentQ.options[keyNum - 1]) {
          handleAnswer(currentQ.options[keyNum - 1].value);
        }
      }
      
      // Arrow keys for navigation
      if (e.key === 'ArrowRight' || e.key === 'Enter') {
        if (currentQ && (!currentQ.required || answers[currentQ.id])) {
          e.preventDefault();
          handleNext();
        }
      } else if (e.key === 'ArrowLeft' && currentQuestion > 0) {
        e.preventDefault();
        handlePrevious();
      }
    };
    
    window.addEventListener('keydown', handleKeyPress);
    return () => window.removeEventListener('keydown', handleKeyPress);
  }, [currentQuestion, currentQ, answers]);

  const handleAnswer = (answer) => {
    setAnswers(prev => ({
      ...prev,
      [currentQ.id]: answer
    }));
  };

  const handleNext = () => {
    if (currentQuestion < relevantQuestions.length - 1) {
      setCurrentQuestion(prev => prev + 1);
    } else {
      handleSubmit();
    }
  };

  const handlePrevious = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(prev => prev - 1);
    }
  };

  const handleSkip = () => {
    if (!currentQ.required) {
      handleNext();
    }
  };

  const handleFileUpload = async (file, questionId) => {
    setSupplementalFiles(prev => ({
      ...prev,
      [questionId]: file
    }));
  };

  const handleSubmit = async () => {
    console.log('handleSubmit called with answers:', answers);
    console.log('Current question:', currentQ.id);
    setIsProcessing(true);
    try {
      // Submit supplemental information
      const formData = new FormData();
      formData.append('answers', JSON.stringify(answers));
      
      // Add files if any
      if (supplementalFiles && Object.keys(supplementalFiles).length > 0) {
        Object.entries(supplementalFiles).forEach(([key, file]) => {
          formData.append('files', file, `file_${key}`);
        });
      }

      console.log('Submitting to API...');
      const response = await axios.post(
        `/api/documents/${documentId}/supplemental`,
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        }
      );
      console.log('API Response:', response.data);

      console.log('API call successful, calling onComplete');
      if (onComplete) {
        onComplete(answers, supplementalFiles);
      } else {
        console.error('onComplete callback is not defined!');
      }
    } catch (error) {
      console.error('Error submitting supplemental info:', error);
      console.error('Error response:', error.response?.data);
      toast.error(`Error: ${error.response?.data?.detail || error.message}`);
    } finally {
      setIsProcessing(false);
    }
  };

  // Get AI suggestions for current question
  const getAISuggestions = async () => {
    if (currentQ && (currentQ.type === 'select' || currentQ.type === 'table')) {
      try {
        const response = await axios.post(
          `/api/analysis/documents/${documentId}/suggest`,
          { question_type: currentQ.id },
          {
            headers: {
              'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
          }
        );
        setSuggestions(response.data.suggestions || []);
      } catch (error) {
        console.error('Error getting AI suggestions:', error);
      }
    }
  };
  
  // Auto-fill from diagram analysis
  const handleAutoFill = async () => {
    setIsAnalyzing(true);
    try {
      const response = await axios.post(
        `/api/analysis/documents/${documentId}/auto-analyze`,
        {},
        {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        }
      );
      
      if (response.data.analysis) {
        // Pre-fill answers based on AI analysis
        const aiAnswers = response.data.analysis;
        setAnswers(prev => ({
          ...prev,
          ...aiAnswers
        }));
        
        toast.success('AI has analyzed your diagram and pre-filled some answers!');
        setAutoFillAvailable(false);
      }
    } catch (error) {
      console.error('Error auto-filling from diagram:', error);
      toast.error('Failed to auto-analyze diagram');
    } finally {
      setIsAnalyzing(false);
    }
  };

  useEffect(() => {
    if (currentQ) {
      getAISuggestions();
    }
  }, [currentQuestion]); // eslint-disable-line react-hooks/exhaustive-deps

  const renderQuestionInput = () => {
    switch (currentQ.type) {
      case 'select':
        // Grid layout for topology cards
        if (currentQ.id === 'network_design') {
          return (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {currentQ.options.map((option, index) => {
                const Icon = option.icon || QuestionMarkCircleIcon;
                const isSelected = answers[currentQ.id] === option.value;
                const keyNumber = index + 1;
                return (
                  <button
                    key={option.value}
                    onClick={() => handleAnswer(option.value)}
                    className={`relative p-6 border-2 rounded-xl cursor-pointer transition-all transform hover:scale-105 ${
                      isSelected
                        ? 'border-blue-500 bg-blue-50 shadow-lg'
                        : option.highlight
                        ? 'border-purple-300 bg-purple-50 hover:border-purple-400'
                        : 'border-gray-200 bg-white hover:border-gray-300 hover:shadow-md'
                    }`}
                  >
                    {/* Keyboard shortcut number */}
                    {keyNumber <= 9 && (
                      <div className="absolute top-3 left-3">
                        <kbd className="px-2 py-1 bg-gray-100 border border-gray-300 rounded text-xs font-mono">
                          {keyNumber}
                        </kbd>
                      </div>
                    )}
                    
                    {isSelected && (
                      <CheckCircleIcon className="absolute top-3 right-3 h-6 w-6 text-blue-600" />
                    )}
                    
                    <div className="flex flex-col items-center text-center space-y-3">
                      <Icon className={`h-12 w-12 ${
                        isSelected ? 'text-blue-600' : 
                        option.highlight ? 'text-purple-600' : 'text-gray-600'
                      }`} />
                      <div>
                        <h4 className={`font-semibold text-lg ${
                          isSelected ? 'text-blue-900' : 'text-gray-900'
                        }`}>
                          {option.label}
                        </h4>
                        <p className="text-sm text-gray-600 mt-1">
                          {option.description}
                        </p>
                      </div>
                    </div>
                  </button>
                );
              })}
            </div>
          );
        }
        
        // Default select rendering for other questions
        return (
          <div className="space-y-2">
            {currentQ.options.map(option => (
              <label
                key={option.value}
                className={`block p-4 border rounded-lg cursor-pointer transition-all ${
                  answers[currentQ.id] === option.value
                    ? 'border-blue-500 bg-blue-50'
                    : 'border-gray-200 hover:border-gray-300'
                }`}
              >
                <input
                  type="radio"
                  name={currentQ.id}
                  value={option.value}
                  checked={answers[currentQ.id] === option.value}
                  onChange={(e) => handleAnswer(e.target.value)}
                  className="sr-only"
                />
                <div className="font-medium">{option.label}</div>
              </label>
            ))}
          </div>
        );

      case 'file_or_text':
        return (
          <div className="space-y-4">
            <div className="border-2 border-dashed border-gray-300 rounded-lg p-6">
              <div className="text-center">
                <PaperClipIcon className="mx-auto h-12 w-12 text-gray-400" />
                <p className="mt-2 text-sm text-gray-600">
                  Upload a file or paste text below
                </p>
                <input
                  type="file"
                  accept={currentQ.fileTypes?.join(',')}
                  onChange={(e) => handleFileUpload(e.target.files[0], currentQ.id)}
                  className="hidden"
                  id="file-upload"
                />
                <label
                  htmlFor="file-upload"
                  className="mt-2 inline-flex items-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 cursor-pointer"
                >
                  Choose File
                </label>
              </div>
            </div>
            <div className="relative">
              <textarea
                placeholder={currentQ.placeholder}
                value={answers[currentQ.id] || ''}
                onChange={(e) => handleAnswer(e.target.value)}
                rows={6}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
              />
              {currentQ.textFormat && (
                <p className="mt-1 text-xs text-gray-500">
                  Format: {currentQ.textFormat}
                </p>
              )}
            </div>
          </div>
        );

      case 'table':
        return (
          <DeviceTable
            columns={currentQ.columns}
            data={answers[currentQ.id] || []}
            onChange={handleAnswer}
            suggestions={suggestions}
          />
        );

      case 'dynamic_list':
        return (
          <DynamicList
            fields={currentQ.fields}
            data={answers[currentQ.id] || []}
            onChange={handleAnswer}
          />
        );

      case 'connections':
        return (
          <ConnectionBuilder
            data={answers[currentQ.id] || []}
            onChange={handleAnswer}
            documentId={documentId}
          />
        );

      case 'text':
        return (
          <textarea
            placeholder={currentQ.placeholder}
            value={answers[currentQ.id] || ''}
            onChange={(e) => handleAnswer(e.target.value)}
            rows={currentQ.multiline ? 6 : 1}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        );

      default:
        return null;
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-lg p-6 max-w-4xl mx-auto">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center">
          <ChatBubbleLeftRightIcon className="h-8 w-8 text-blue-600 mr-3" />
          <div>
            <h2 className="text-2xl font-bold text-gray-900">
              Documentation Assistant
            </h2>
            <p className="text-gray-600">
              Let me help you complete your network documentation
            </p>
          </div>
        </div>
        
        {currentQuestion === 0 && (
          <button
            onClick={handleAutoFill}
            disabled={isAnalyzing}
            className={`inline-flex items-center px-4 py-2 rounded-lg font-medium transition-all ${
              isAnalyzing
                ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                : 'bg-purple-600 text-white hover:bg-purple-700 hover:shadow-md'
            }`}
          >
            {isAnalyzing ? (
              <>
                <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                Analyzing...
              </>
            ) : (
              <>
                <SparklesIcon className="h-4 w-4 mr-2" />
                Auto-fill from diagram
              </>
            )}
          </button>
        )}
      </div>

      <div className="mb-6">
        <div className="flex justify-between items-center mb-2">
          <div className="flex items-center gap-4">
            <span className="text-sm font-medium text-gray-700">
              Question {currentQuestion + 1} of {relevantQuestions.length}
            </span>
            <div className="flex items-center text-sm text-gray-500">
              <ClockIcon className="h-4 w-4 mr-1" />
              <span>~{calculateTimeRemaining()} min remaining</span>
            </div>
          </div>
          {!currentQ.required && (
            <button
              onClick={handleSkip}
              className="text-sm text-blue-600 hover:text-blue-700 transition-colors"
            >
              Skip this question
            </button>
          )}
        </div>
        <div className="relative">
          <div className="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
            <div
              className="bg-gradient-to-r from-blue-500 to-blue-600 h-3 rounded-full transition-all duration-500 ease-out"
              style={{ width: `${((currentQuestion + 1) / relevantQuestions.length) * 100}%` }}
            />
          </div>
          <div className="absolute -top-1 transition-all duration-500 ease-out"
               style={{ left: `${((currentQuestion + 1) / relevantQuestions.length) * 100}%` }}>
            <div className="w-5 h-5 bg-blue-600 rounded-full border-2 border-white shadow-md" />
          </div>
        </div>
      </div>

      {currentQ && (
        <div className="space-y-6">
          <div>
            <div className="flex items-start justify-between">
              <div className="flex-1">
                <h3 className="text-lg font-medium text-gray-900 mb-2">
                  {currentQ.question}
                </h3>
                {currentQ.help && (
                  <p className="text-sm text-gray-600 mb-4">{currentQ.help}</p>
                )}
              </div>
              <button
                className="ml-4 p-2 text-gray-400 hover:text-gray-600 transition-colors"
                title="Learn more about this question"
              >
                <InformationCircleIcon className="h-5 w-5" />
              </button>
            </div>
            
            {/* Keyboard shortcuts hint for network design */}
            {currentQ.id === 'network_design' && (
              <div className="bg-blue-50 border border-blue-200 rounded-lg p-3 mb-4">
                <div className="flex items-center text-sm text-blue-800">
                  <LightBulbIcon className="h-4 w-4 mr-2 flex-shrink-0" />
                  <span>
                    <strong>Pro tip:</strong> Use number keys 1-9 to quickly select options, 
                    or arrow keys to navigate. Press Enter to continue.
                  </span>
                </div>
              </div>
            )}
          </div>

          <div className="min-h-[200px]">
            {renderQuestionInput()}
          </div>

          {suggestions.length > 0 && (
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
              <p className="text-sm font-medium text-blue-900 mb-2">
                AI Suggestions:
              </p>
              <div className="space-y-1">
                {suggestions.map((suggestion, idx) => (
                  <button
                    key={idx}
                    onClick={() => handleAnswer(suggestion)}
                    className="block w-full text-left text-sm text-blue-700 hover:text-blue-800 hover:underline"
                  >
                    → {suggestion}
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>
      )}

      <div className="flex justify-between items-center mt-8 pt-6 border-t">
        <button
          onClick={handlePrevious}
          disabled={currentQuestion === 0}
          className={`inline-flex items-center px-4 py-2 rounded-lg font-medium transition-all ${
            currentQuestion === 0
              ? 'bg-gray-100 text-gray-400 cursor-not-allowed'
              : 'bg-gray-200 text-gray-700 hover:bg-gray-300 hover:shadow-md'
          }`}
        >
          <ArrowLeftIcon className="h-4 w-4 mr-2" />
          Previous
        </button>

        <div className="flex items-center gap-2 text-sm text-gray-500">
          <span>Press</span>
          <kbd className="px-2 py-1 bg-gray-100 border border-gray-300 rounded text-xs">Enter</kbd>
          <span>to continue</span>
        </div>

        <button
          onClick={handleNext}
          disabled={(currentQ.required && !answers[currentQ.id]) || isProcessing}
          className={`inline-flex items-center px-6 py-2 rounded-lg font-medium transition-all ${
            (currentQ.required && !answers[currentQ.id]) || isProcessing
              ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
              : 'bg-blue-600 text-white hover:bg-blue-700 hover:shadow-md transform hover:scale-105'
          }`}
        >
          {isProcessing ? (
            <>
              <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
              Processing...
            </>
          ) : currentQuestion === relevantQuestions.length - 1 ? (
            <>
              Complete
              <CheckCircleIcon className="h-4 w-4 ml-2" />
            </>
          ) : (
            <>
              Next
              <ArrowRightIcon className="h-4 w-4 ml-2" />
            </>
          )}
        </button>
      </div>
    </div>
  );
};

// Sub-components for complex inputs
const DeviceTable = ({ columns, data, onChange, suggestions }) => {
  const [rows, setRows] = useState(data.length > 0 ? data : [{}]);

  const handleCellChange = (rowIndex, columnKey, value) => {
    const newRows = [...rows];
    newRows[rowIndex] = {
      ...newRows[rowIndex],
      [columnKey]: value
    };
    setRows(newRows);
    onChange(newRows.filter(row => Object.values(row).some(v => v)));
  };

  const addRow = () => {
    setRows([...rows, {}]);
  };

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            {columns.map(col => (
              <th
                key={col.key}
                className="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                {col.label}
                {col.required && <span className="text-red-500 ml-1">*</span>}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {rows.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {columns.map(col => (
                <td key={col.key} className="px-3 py-2">
                  <input
                    type="text"
                    value={row[col.key] || ''}
                    onChange={(e) => handleCellChange(rowIndex, col.key, e.target.value)}
                    className="w-full px-2 py-1 border border-gray-300 rounded focus:ring-blue-500 focus:border-blue-500"
                  />
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      <button
        onClick={addRow}
        className="mt-2 text-sm text-blue-600 hover:text-blue-700"
      >
        + Add Row
      </button>
    </div>
  );
};

const DynamicList = ({ fields, data, onChange }) => {
  const [items, setItems] = useState(data.length > 0 ? data : [{}]);

  const handleItemChange = (index, field, value) => {
    const newItems = [...items];
    newItems[index] = {
      ...newItems[index],
      [field]: value
    };
    setItems(newItems);
    onChange(newItems.filter(item => Object.values(item).some(v => v)));
  };

  const addItem = () => {
    setItems([...items, {}]);
  };

  const removeItem = (index) => {
    const newItems = items.filter((_, i) => i !== index);
    setItems(newItems);
    onChange(newItems);
  };

  return (
    <div className="space-y-4">
      {items.map((item, index) => (
        <div key={index} className="border border-gray-200 rounded-lg p-4">
          <div className="grid grid-cols-2 gap-4">
            {fields.map(field => (
              <div key={field.key}>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  {field.label}
                </label>
                {field.options ? (
                  <select
                    value={item[field.key] || ''}
                    onChange={(e) => handleItemChange(index, field.key, e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                  >
                    <option value="">Select...</option>
                    {field.options.map(opt => (
                      <option key={opt} value={opt}>{opt}</option>
                    ))}
                  </select>
                ) : (
                  <input
                    type="text"
                    placeholder={field.placeholder}
                    value={item[field.key] || ''}
                    onChange={(e) => handleItemChange(index, field.key, e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                  />
                )}
              </div>
            ))}
          </div>
          {items.length > 1 && (
            <button
              onClick={() => removeItem(index)}
              className="mt-2 text-sm text-red-600 hover:text-red-700"
            >
              Remove
            </button>
          )}
        </div>
      ))}
      <button
        onClick={addItem}
        className="text-sm text-blue-600 hover:text-blue-700"
      >
        + Add Item
      </button>
    </div>
  );
};

const ConnectionBuilder = ({ data, onChange, documentId }) => {
  // Simplified connection builder
  const [connections, setConnections] = useState(data || []);

  const addConnection = () => {
    setConnections([...connections, {
      source: '',
      target: '',
      type: '',
      description: ''
    }]);
  };

  return (
    <div className="space-y-4">
      <p className="text-sm text-gray-600">
        Add any logical connections not visible in the diagram (VPNs, wireless links, etc.)
      </p>
      {connections.map((conn, index) => (
        <div key={index} className="grid grid-cols-2 gap-4 p-4 border border-gray-200 rounded-lg">
          <input
            type="text"
            placeholder="Source Device"
            value={conn.source}
            onChange={(e) => {
              const newConns = [...connections];
              newConns[index].source = e.target.value;
              setConnections(newConns);
              onChange(newConns);
            }}
            className="px-3 py-2 border border-gray-300 rounded-md"
          />
          <input
            type="text"
            placeholder="Target Device"
            value={conn.target}
            onChange={(e) => {
              const newConns = [...connections];
              newConns[index].target = e.target.value;
              setConnections(newConns);
              onChange(newConns);
            }}
            className="px-3 py-2 border border-gray-300 rounded-md"
          />
          <input
            type="text"
            placeholder="Connection Type (e.g., VPN, Wireless)"
            value={conn.type}
            onChange={(e) => {
              const newConns = [...connections];
              newConns[index].type = e.target.value;
              setConnections(newConns);
              onChange(newConns);
            }}
            className="px-3 py-2 border border-gray-300 rounded-md"
          />
          <input
            type="text"
            placeholder="Description"
            value={conn.description}
            onChange={(e) => {
              const newConns = [...connections];
              newConns[index].description = e.target.value;
              setConnections(newConns);
              onChange(newConns);
            }}
            className="px-3 py-2 border border-gray-300 rounded-md"
          />
        </div>
      ))}
      <button
        onClick={addConnection}
        className="text-sm text-blue-600 hover:text-blue-700"
      >
        + Add Connection
      </button>
    </div>
  );
};

export default InteractiveHelper;