// apiService.js - A service to handle API calls to the backend

// Get the backend URL from the global configuration
// This is set up in src/clientModules/initAppConfig.js
const getApiBaseUrl = () => {
  if (typeof window !== 'undefined' && window.APP_CONFIG) {
    return window.APP_CONFIG.BACKEND_URL || 'http://localhost:8000';
  }
  return 'http://localhost:8000';
};

const API_BASE_URL = getApiBaseUrl();

// Default headers for API requests
const getDefaultHeaders = () => ({
  'Content-Type': 'application/json',
});

// Get authorization header if token exists
const getAuthHeader = () => {
  const token = localStorage.getItem('access_token');
  if (token) {
    return { 'Authorization': `Bearer ${token}` };
  }
  return {};
};

// Function to merge headers
const getHeaders = (additionalHeaders = {}) => ({
  ...getDefaultHeaders(),
  ...getAuthHeader(),
  ...additionalHeaders,
});

// API service object
const apiService = {
  // Authentication endpoints
  auth: {
    register: async (userData) => {
      const response = await fetch(`${API_BASE_URL}/api/auth/register`, {
        method: 'POST',
        headers: getHeaders(),
        body: JSON.stringify(userData)
      });
      
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Registration failed');
      }
      
      return response.json();
    },
    
    login: async (credentials) => {
      const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
        method: 'POST',
        headers: getHeaders(),
        body: JSON.stringify(credentials)
      });
      
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Login failed');
      }
      
      return response.json();
    },
    
    logout: async () => {
      // In a real implementation, this would invalidate the token on the server
      localStorage.removeItem('access_token');
      return { message: 'Successfully logged out' };
    },
    
    getProfile: async () => {
      const response = await fetch(`${API_BASE_URL}/api/auth/profile`, {
        method: 'GET',
        headers: getHeaders()
      });
      
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Failed to get profile');
      }
      
      return response.json();
    },
    
    updateProfile: async (profileData) => {
      const response = await fetch(`${API_BASE_URL}/api/auth/profile`, {
        method: 'PUT',
        headers: getHeaders(),
        body: JSON.stringify(profileData)
      });
      
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Failed to update profile');
      }
      
      return response.json();
    }
  },
  
  // Chatbot endpoints
  chatbot: {
    query: async (queryData) => {
      const response = await fetch(`${API_BASE_URL}/api/chatbot/query`, {
        method: 'POST',
        headers: getHeaders(),
        body: JSON.stringify(queryData)
      });
      
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Failed to get response from chatbot');
      }
      
      return response.json();
    },
    
    getConversations: async () => {
      const response = await fetch(`${API_BASE_URL}/api/chatbot/conversations`, {
        method: 'GET',
        headers: getHeaders()
      });
      
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Failed to get conversations');
      }
      
      return response.json();
    }
  },
  
  // Book content endpoints
  book: {
    search: async (query) => {
      const response = await fetch(`${API_BASE_URL}/api/book/search?q=${encodeURIComponent(query)}`, {
        method: 'GET',
        headers: getHeaders()
      });
      
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Failed to search book content');
      }
      
      return response.json();
    }
  }
};

export default apiService;