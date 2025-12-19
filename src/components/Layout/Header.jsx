import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';

const Header = () => {
  const {siteConfig} = useDocusaurusContext();
  
  return (
    <header className={clsx('hero hero--primary', 'hero-section')}>
      <div className="container">
        <div className="header-content">
          <div className="logo">
            <img src={useBaseUrl('/img/logo.svg')} alt="Logo" />
            <h1 className="header-title">{siteConfig.title}</h1>
          </div>
          <nav className="header-nav">
            <Link className="nav-link" to="/docs/intro">Book</Link>
            <Link className="nav-link" to="/chatbot">AI Chatbot</Link>
            <Link className="nav-link" to="/login">Log In</Link>
            <Link className="nav-link" to="/signup">Sign Up</Link>
            <Link className="nav-link" to="https://github.com/physical-ai-humanoid-book/physical-ai-humanoid-book">GitHub</Link>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;