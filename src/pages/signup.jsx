import React from 'react';
import Layout from '@theme/Layout';
import Signup from '../components/Auth/Signup';

export default function SignupPage() {
  return (
    <Layout
      title={`Sign Up`}
      description="Create an account for the Physical AI & Humanoid Robotics book platform">
      <main>
        <div className="container padding-vert--lg">
          <div className="row">
            <div className="col col--6 col--offset-3">
              <Signup />
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}