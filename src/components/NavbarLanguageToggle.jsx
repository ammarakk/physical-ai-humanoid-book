import React from 'react';
import { useLanguage } from '@site/src/contexts/LanguageContext';
import './LanguageToggle.css';

const NavbarLanguageToggle = () => {
  const { currentLanguage, changeLanguage } = useLanguage();

  const handleLanguageChange = (e) => {
    changeLanguage(e.target.value);
  };

  return (
    <div className="navbar__item navbar__language-toggle">
      <select
        value={currentLanguage}
        onChange={handleLanguageChange}
        aria-label="Select language"
        className="navbar__language-select"
      >
        <option value="en">EN</option>
        <option value="ur">UR</option>
      </select>
    </div>
  );
};

export default NavbarLanguageToggle;