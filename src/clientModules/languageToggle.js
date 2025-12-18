import { useLanguage } from '@site/src/contexts/LanguageContext';
import React from 'react';
import ReactDOM from 'react-dom';

const LanguageToggleComponent = () => {
  const { currentLanguage, changeLanguage } = useLanguage();

  const handleLanguageChange = (e) => {
    changeLanguage(e.target.value);
  };

  return (
    <select
      value={currentLanguage}
      onChange={handleLanguageChange}
      aria-label="Select language"
      style={{
        backgroundColor: 'var(--ifm-navbar-link-color, #fff)',
        color: 'var(--ifm-navbar-background-color, #000)',
        border: '1px solid var(--ifm-navbar-link-color, #ccc)',
        borderRadius: '4px',
        padding: '0.25rem 0.5rem',
        fontSize: '0.8rem',
        cursor: 'pointer',
        marginLeft: '0.5rem'
      }}
    >
      <option value="en">EN</option>
      <option value="ur">UR</option>
    </select>
  );
};

// Render the language toggle in the placeholder
if (typeof window !== 'undefined') {
  // Wait for the DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      const placeholder = document.getElementById('language-toggle-placeholder');
      if (placeholder) {
        // Wrap the component in the LanguageProvider context
        const wrapper = document.createElement('div');
        placeholder.appendChild(wrapper);
        
        // Since we can't directly access the LanguageProvider context here,
        // we'll render a simple implementation
        ReactDOM.render(
          React.createElement(() => {
            const [currentLanguage, setCurrentLanguage] = React.useState('en');
            
            React.useEffect(() => {
              const savedLanguage = localStorage.getItem('preferredLanguage') || 'en';
              setCurrentLanguage(savedLanguage);
            }, []);
            
            const handleLanguageChange = (newLanguage) => {
              if (newLanguage !== currentLanguage) {
                setCurrentLanguage(newLanguage);
                localStorage.setItem('preferredLanguage', newLanguage);
                
                // Dispatch a custom event that other components can listen to
                window.dispatchEvent(new CustomEvent('languageChange', { 
                  detail: { newLanguage } 
                }));
              }
            };
            
            return (
              <select
                value={currentLanguage}
                onChange={(e) => handleLanguageChange(e.target.value)}
                aria-label="Select language"
                style={{
                  backgroundColor: 'var(--ifm-navbar-link-color, #fff)',
                  color: 'var(--ifm-navbar-background-color, #000)',
                  border: '1px solid var(--ifm-navbar-link-color, #ccc)',
                  borderRadius: '4px',
                  padding: '0.25rem 0.5rem',
                  fontSize: '0.8rem',
                  cursor: 'pointer',
                  marginLeft: '0.5rem'
                }}
              >
                <option value="en">EN</option>
                <option value="ur">UR</option>
              </select>
            );
          }),
          wrapper
        );
      }
    });
  } else {
    // DOM is already ready
    const placeholder = document.getElementById('language-toggle-placeholder');
    if (placeholder) {
      const wrapper = document.createElement('div');
      placeholder.appendChild(wrapper);
      
      ReactDOM.render(
        React.createElement(() => {
          const [currentLanguage, setCurrentLanguage] = React.useState('en');
          
          React.useEffect(() => {
            const savedLanguage = localStorage.getItem('preferredLanguage') || 'en';
            setCurrentLanguage(savedLanguage);
          }, []);
          
          const handleLanguageChange = (newLanguage) => {
            if (newLanguage !== currentLanguage) {
              setCurrentLanguage(newLanguage);
              localStorage.setItem('preferredLanguage', newLanguage);
              
              // Dispatch a custom event that other components can listen to
              window.dispatchEvent(new CustomEvent('languageChange', { 
                detail: { newLanguage } 
              }));
            }
          };
          
          return (
            <select
              value={currentLanguage}
              onChange={(e) => handleLanguageChange(e.target.value)}
              aria-label="Select language"
              style={{
                backgroundColor: 'var(--ifm-navbar-link-color, #fff)',
                color: 'var(--ifm-navbar-background-color, #000)',
                border: '1px solid var(--ifm-navbar-link-color, #ccc)',
                borderRadius: '4px',
                padding: '0.25rem 0.5rem',
                fontSize: '0.8rem',
                cursor: 'pointer',
                marginLeft: '0.5rem'
              }}
            >
              <option value="en">EN</option>
              <option value="ur">UR</option>
            </select>
          );
        }),
        wrapper
      );
    }
  }
}