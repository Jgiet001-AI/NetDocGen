import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { Provider } from 'react-redux';
import { PersistGate } from 'redux-persist/integration/react';
import { Toaster } from 'react-hot-toast';
import axios from 'axios';

import { store, persistor } from './store';
import ErrorBoundary from './components/ErrorBoundary';
import PrivateRoute from './components/auth/PrivateRoute';
import LoginForm from './components/auth/LoginForm';
import RegisterForm from './components/auth/RegisterForm';
import Dashboard from './pages/Dashboard';
import Projects from './pages/Projects';
import ProjectDetail from './pages/ProjectDetail';
import Documents from './pages/Documents';
import DocumentDetail from './pages/DocumentDetail';
import Upload from './pages/Upload';
import Settings from './pages/Settings';
import TemplateEditor from './components/templates/TemplateEditor';
import TemplatePreviewPage from './pages/TemplatePreviewPage';

// Configure axios defaults
axios.defaults.baseURL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Add auth token to requests if it exists
const token = localStorage.getItem('token');
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

// Add response interceptor for token expiration
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expired or invalid
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

function App() {
  return (
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistor}>
        <ErrorBoundary>
          <Router>
            <div className="App">
            <Toaster 
            position="top-right"
            toastOptions={{
              duration: 4000,
              style: {
                background: '#363636',
                color: '#fff',
              },
              success: {
                iconTheme: {
                  primary: '#10B981',
                  secondary: '#fff',
                },
              },
              error: {
                iconTheme: {
                  primary: '#EF4444',
                  secondary: '#fff',
                },
              },
            }}
          />
          
          <Routes>
            {/* Public Routes */}
            <Route path="/login" element={<LoginForm />} />
            <Route path="/register" element={<RegisterForm />} />
            
            {/* Private Routes */}
            <Route path="/dashboard" element={
              <PrivateRoute>
                <Dashboard />
              </PrivateRoute>
            } />
            
            <Route path="/projects" element={
              <PrivateRoute>
                <Projects />
              </PrivateRoute>
            } />
            
            <Route path="/projects/new" element={
              <PrivateRoute>
                <Projects newProject />
              </PrivateRoute>
            } />
            
            <Route path="/projects/:id" element={
              <PrivateRoute>
                <ProjectDetail />
              </PrivateRoute>
            } />
            
            <Route path="/documents" element={
              <PrivateRoute>
                <Documents />
              </PrivateRoute>
            } />
            
            <Route path="/documents/:id" element={
              <PrivateRoute>
                <DocumentDetail />
              </PrivateRoute>
            } />
            
            <Route path="/upload" element={
              <PrivateRoute>
                <Upload />
              </PrivateRoute>
            } />
            
            <Route path="/settings" element={
              <PrivateRoute>
                <Settings />
              </PrivateRoute>
            } />
            
            <Route path="/settings/templates/:templateId/edit" element={
              <PrivateRoute>
                <TemplateEditor />
              </PrivateRoute>
            } />
            
            <Route path="/settings/templates/:templateId/preview" element={
              <PrivateRoute>
                <TemplatePreviewPage />
              </PrivateRoute>
            } />
            
            {/* Default redirect */}
            <Route path="/" element={<Navigate to="/dashboard" replace />} />
            <Route path="*" element={<Navigate to="/dashboard" replace />} />
          </Routes>
        </div>
      </Router>
    </ErrorBoundary>
    </PersistGate>
    </Provider>
  );
}

export default App;