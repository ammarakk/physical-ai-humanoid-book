import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import './HeroSection.css'; // We'll create this CSS file

const HeroSection = () => {
  const {siteConfig} = useDocusaurusContext();
  
  return (
    <header className={clsx('hero hero--primary', 'hero-section')}>
      <div className="container">
        <div className="row">
          <div className="col col--6">
            <h1 className="hero__title">{siteConfig.title}</h1>
            <p className="hero__subtitle">{siteConfig.tagline}</p>
            <p className="hero__description">
              An AI-powered exploration of Physical AI and Humanoid Robotics with interactive learning tools.
            </p>
            <div className="hero-buttons">
              <Link className="button button--secondary button--lg" to="/docs/intro">
                Read the Book
              </Link>
              <Link className="button button--primary button--lg" to="/chatbot">
                Open AI Chatbot
              </Link>
            </div>
          </div>
          <div className="col col--6">
            <div className="landing-animation">
              <div className="landing-robot"></div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default HeroSection;