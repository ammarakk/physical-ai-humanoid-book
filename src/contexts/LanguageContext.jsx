import React, { createContext, useContext, useState, useEffect } from 'react';

const LanguageContext = createContext();

export const useLanguage = () => {
  const context = useContext(LanguageContext);
  if (!context) {
    throw new Error('useLanguage must be used within a LanguageProvider');
  }
  return context;
};

export const LanguageProvider = ({ children }) => {
  const [currentLanguage, setCurrentLanguage] = useState('en');

  useEffect(() => {
    // Load language preference from localStorage on initial load
    const savedLanguage = localStorage.getItem('preferredLanguage') || 'en';
    setCurrentLanguage(savedLanguage);
  }, []);

  const changeLanguage = (newLanguage) => {
    if (newLanguage !== currentLanguage) {
      setCurrentLanguage(newLanguage);
      localStorage.setItem('preferredLanguage', newLanguage);
      
      // Dispatch a custom event that other components can listen to
      window.dispatchEvent(new CustomEvent('languageChange', { 
        detail: { newLanguage } 
      }));
    }
  };

  const value = {
    currentLanguage,
    changeLanguage,
    t: (key) => {
      // Simple translation function - in a real app, this would use proper translation files
      const translations = {
        'en': {
          'language.english': 'English',
          'language.urdu': 'Urdu',
          'toggle.language': 'Toggle Language'
        },
        'ur': {
          'language.english': 'انگریزی',
          'language.urdu': 'اردو',
          'toggle.language': 'زبان تبدیل کریں'
        }
      };
      
      return translations[currentLanguage]?.[key] || key;
    }
  };

  return (
    <LanguageContext.Provider value={value}>
      {children}
    </LanguageContext.Provider>
  );
};