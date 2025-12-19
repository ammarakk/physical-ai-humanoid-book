import React from 'react';
import './CreatorSection.css';

const CreatorSection = () => {
  return (
    <section className="creator-section container padding-vert--lg">
      <div className="row">
        <div className="col col--8 col--offset-2">
          <h2 className="text--center">About the Creator</h2>
          <div className="creator-content">
            <div className="creator-avatar">
              <img 
                src="img/creator-avatar.jpg" 
                alt="Creator Avatar" 
                onError={(e) => {
                  e.target.src = 'https://placehold.co/150x150/0a0a0a/00a8ff?text=AI';
                }}
              />
            </div>
            <div className="creator-info">
              <h3>Dr. AI Researcher</h3>
              <p className="creator-title">Senior AI/Robotics Researcher</p>
              <p>
                Dr. AI Researcher is a leading expert in Physical AI and Humanoid Robotics with over 15 years of experience 
                in the field. With a PhD in Robotics from Stanford University and multiple publications in top-tier 
                conferences, Dr. Researcher brings deep technical expertise to this comprehensive guide.
              </p>
              <div className="creator-credentials">
                <div className="credential">
                  <h4>PhD in Robotics</h4>
                  <p>Stanford University</p>
                </div>
                <div className="credential">
                  <h4>Senior Researcher</h4>
                  <p>AI Lab, Tech Institute</p>
                </div>
                <div className="credential">
                  <h4>20+ Publications</h4>
                  <p>Top-tier conferences</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default CreatorSection;