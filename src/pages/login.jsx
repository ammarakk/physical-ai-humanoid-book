import React from 'react';
import Layout from '@theme/Layout';
import Login from '../components/Auth/Login';

export default function LoginPage() {
  return (
    <Layout
      title={`Login`}
      description="Login to access the Physical AI & Humanoid Robotics book platform">
      <main>
        <div className="container padding-vert--lg">
          <div className="row">
            <div className="col col--6 col--offset-3">
              <Login />
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}