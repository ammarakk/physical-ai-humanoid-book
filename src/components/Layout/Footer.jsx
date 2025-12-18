import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

const Footer = () => {
  const {siteConfig} = useDocusaurusContext();

  return (
    <footer className={clsx('footer', 'footer--dark')}>
      <div className="container">
        <div className="row">
          <div className="col col--4">
            <h4>Docs</h4>
            <ul>
              <li><Link to="/docs/intro">Tutorial</Link></li>
              <li><Link to="/docs/welcome">Welcome</Link></li>
            </ul>
          </div>
          <div className="col col--4">
            <h4>Community</h4>
            <ul>
              <li><a href="https://stackoverflow.com/questions/tagged/docusaurus">Stack Overflow</a></li>
              <li><a href="https://discordapp.com/invite/docusaurus">Discord</a></li>
              <li><a href="https://x.com/docusaurus">X</a></li>
            </ul>
          </div>
          <div className="col col--4">
            <h4>More</h4>
            <ul>
              <li><Link to="/blog">Blog</Link></li>
              <li><a href="https://github.com/physical-ai-humanoid-book/physical-ai-humanoid-book">GitHub</a></li>
              <li>Powered by AI technologies</li>
            </ul>
          </div>
        </div>
        <div className="footer__copyright">
          Copyright © {new Date().getFullYear()} Physical AI & Humanoid Robotics Book. Built with Docusaurus.
        </div>
      </div>
    </footer>
  );
};

export default Footer;