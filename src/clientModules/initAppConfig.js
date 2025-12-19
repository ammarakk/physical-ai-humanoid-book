// src/clientModules/initAppConfig.js
// Initialize application configuration that will be available in the browser

// Define the configuration
// Since process.env doesn't work directly in browser, we'll use a global variable approach
// The actual URL can be set in the docusaurus.config.js using the 'themeConfig' or 'customFields'
const appConfig = {
  BACKEND_URL: 'http://localhost:8000'  // Default value, can be changed by environment or build process
};

// Make the configuration available globally
if (typeof window !== 'undefined') {
  window.APP_CONFIG = { ...window.APP_CONFIG, ...appConfig };
}