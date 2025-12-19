import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ children }) => {
  // In a real implementation, you would check for the presence of a valid token
  // const token = localStorage.getItem('access_token');
  
  // For demo purposes, we'll simulate a check
  const token = localStorage.getItem('access_token');
  
  return token ? children : <Navigate to="/login" replace />;
};

export default ProtectedRoute;