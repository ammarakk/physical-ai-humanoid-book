// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'PHYSICAL AI & HUMANOID ROBOTICS',
  tagline: 'An AI/Spec-Driven Technical Publication',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://physical-ai-humanoid-book.vercel.app',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'physical-ai-humanoid-book', // Usually your GitHub org/user name.
  projectName: 'physical-ai-humanoid-book', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/physical-ai-humanoid-book/physical-ai-humanoid-book/tree/main/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/physical-ai-humanoid-book/physical-ai-humanoid-book/tree/main/',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  // TODO: T025 - Integrate PDF output generation here, potentially using an external tool or custom Docusaurus plugin.
  // Refer to the project's final phase tasks for more details.

  // TODO: T008 - Configure citation and plagiarism check tools here, or as Docusaurus plugins.
  // This will likely involve custom logic or integration with external services in a CI/CD pipeline.
  // Refer to the project's foundational phase tasks for more details.

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      colorMode: {
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'PANAVERSITY',
        logo: {
          alt: 'Physical AI Book Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Book',
          },
          {
            to: '/chatbot',
            label: 'AI Chatbot',
            position: 'left',
          },
          {
            type: 'html',
            position: 'right',
            value: '<div id="language-toggle-placeholder"></div>',
          },
          // {to: '/blog', label: 'Blog', position: 'left'},
          {
            to: '/login',
            label: 'Log In',
            position: 'right',
          },
          {
            to: '/signup',
            label: 'Sign Up',
            position: 'right',
          },
          {
            href: 'https://github.com/physical-ai-humanoid-book/physical-ai-humanoid-book',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Book Modules',
            items: [
              {
                label: 'Introduction',
                to: '/docs/intro',
              },
              {
                label: 'Physical AI Fundamentals',
                to: '/docs/physical-ai-fundamentals',
              },
              {
                label: 'Humanoid Robotics',
                to: '/docs/humanoid-robotics',
              },
              {
                label: 'Machine Learning in Robotics',
                to: '/docs/ml-robotics',
              },
            ],
          },
          {
            title: 'Resources',
            items: [
              {
                label: 'Official AI Documentation',
                href: 'https://ai.google.dev/',
              },
              {
                label: 'Robotics Standards',
                href: 'https://www.iso.org/standards/robotics.html',
              },
              {
                label: 'Research Papers',
                href: 'https://arxiv.org/list/cs.RO/recent',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/physical-ai-humanoid-book/physical-ai-humanoid-book',
              },
              {
                label: 'AI Technology Explained',
                href: 'https://deepmind.google/technologies/gemini/',
              },
              {
                label: 'Privacy Policy',
                to: '/privacy',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics Book. Built with Docusaurus. AI technology explained.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),

  // TODO: T026 - Configure site performance optimizations (image compression, lazy loading) here.
  // This might involve Docusaurus configuration options, custom plugins, or build-time scripts.
  // Refer to the project's final phase tasks for more details.

  // Expose environment variables to the client
  clientModules: [
    require.resolve('./src/clientModules/initAppConfig.js'),
  ],
};

// Expose client modules to the client
export default config;

// Add the client module to inject the language toggle
if (!config.customFields) {
  config.customFields = {};
}

// Add the client module
config.clientModules = [
  ...config.clientModules || [],
  require.resolve('./src/clientModules/languageToggle.js')
];
