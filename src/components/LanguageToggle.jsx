import React, { useState, useEffect } from 'react';
import BrowserOnly from '@docusaurus/BrowserOnly';

const LanguageToggle = () => {
  const [currentLanguage, setCurrentLanguage] = useState('en');

  // Load language preference from localStorage on component mount
  useEffect(() => {
    const savedLanguage = localStorage.getItem('preferredLanguage') || 'en';
    setCurrentLanguage(savedLanguage);
  }, []);

  // Handle language change
  const handleLanguageChange = (newLanguage) => {
    if (newLanguage !== currentLanguage) {
      setCurrentLanguage(newLanguage);
      localStorage.setItem('preferredLanguage', newLanguage);

      // In a real implementation, this would trigger UI updates for all content
      // For now, we'll just log the change
      console.log(`Language changed to: ${newLanguage}`);
      
      // Trigger a custom event that other components can listen to
      window.dispatchEvent(new CustomEvent('languageChange', { detail: { newLanguage } }));
    }
  };

  return (
    <BrowserOnly>
      {() => (
        <div className="language-toggle">
          <select
            value={currentLanguage}
            onChange={(e) => handleLanguageChange(e.target.value)}
            aria-label="Select language"
          >
            <option value="en">English</option>
            <option value="ur">Urdu</option>
          </select>
        </div>
      )}
    </BrowserOnly>
  );
};

export default LanguageToggle;