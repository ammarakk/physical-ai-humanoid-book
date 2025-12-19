import React from 'react';
import Layout from '@theme/Layout';
import HeroSection from '@site/src/components/LandingPage/HeroSection';
import CreatorSection from '@site/src/components/LandingPage/CreatorSection';

export default function LandingPage() {
  return (
    <Layout
      title={`Welcome`}
      description="Physical AI & Humanoid Robotics - An AI-powered exploration with interactive learning tools">
      <main>
        <HeroSection />
        <div className="container padding-vert--lg">
          <div className="row">
            <div className="col col--6 col--offset-3">
              <h2 className="text--center">Explore Physical AI & Humanoid Robotics</h2>
              <p className="text--center">
                This interactive platform combines traditional book learning with AI-powered assistance
                to enhance your understanding of Physical AI and Humanoid Robotics concepts.
              </p>
            </div>
          </div>
        </div>
        <CreatorSection />
      </main>
    </Layout>
  );
}