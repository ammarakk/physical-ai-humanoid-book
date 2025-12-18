import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '5ff'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '5ba'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'a2b'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'c3c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '156'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '88c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '000'),
    exact: true
  },
  {
    path: '/blog',
    component: ComponentCreator('/blog', 'b2f'),
    exact: true
  },
  {
    path: '/blog/archive',
    component: ComponentCreator('/blog/archive', '182'),
    exact: true
  },
  {
    path: '/blog/authors',
    component: ComponentCreator('/blog/authors', '0b7'),
    exact: true
  },
  {
    path: '/blog/authors/all-sebastien-lorber-articles',
    component: ComponentCreator('/blog/authors/all-sebastien-lorber-articles', '4a1'),
    exact: true
  },
  {
    path: '/blog/authors/yangshun',
    component: ComponentCreator('/blog/authors/yangshun', 'a68'),
    exact: true
  },
  {
    path: '/blog/first-blog-post',
    component: ComponentCreator('/blog/first-blog-post', '89a'),
    exact: true
  },
  {
    path: '/blog/long-blog-post',
    component: ComponentCreator('/blog/long-blog-post', '9ad'),
    exact: true
  },
  {
    path: '/blog/mdx-blog-post',
    component: ComponentCreator('/blog/mdx-blog-post', 'e9f'),
    exact: true
  },
  {
    path: '/blog/tags',
    component: ComponentCreator('/blog/tags', '287'),
    exact: true
  },
  {
    path: '/blog/tags/docusaurus',
    component: ComponentCreator('/blog/tags/docusaurus', '704'),
    exact: true
  },
  {
    path: '/blog/tags/facebook',
    component: ComponentCreator('/blog/tags/facebook', '858'),
    exact: true
  },
  {
    path: '/blog/tags/hello',
    component: ComponentCreator('/blog/tags/hello', '299'),
    exact: true
  },
  {
    path: '/blog/tags/hola',
    component: ComponentCreator('/blog/tags/hola', '00d'),
    exact: true
  },
  {
    path: '/blog/welcome',
    component: ComponentCreator('/blog/welcome', 'd2b'),
    exact: true
  },
  {
    path: '/chatbot',
    component: ComponentCreator('/chatbot', 'b9a'),
    exact: true
  },
  {
    path: '/LayoutWrapper',
    component: ComponentCreator('/LayoutWrapper', '4fe'),
    exact: true
  },
  {
    path: '/login',
    component: ComponentCreator('/login', 'f20'),
    exact: true
  },
  {
    path: '/markdown-page',
    component: ComponentCreator('/markdown-page', '3d7'),
    exact: true
  },
  {
    path: '/signup',
    component: ComponentCreator('/signup', 'e7f'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', 'be4'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', '1ec'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', '0e0'),
            routes: [
              {
                path: '/docs/intro',
                component: ComponentCreator('/docs/intro', '853'),
                exact: true
              },
              {
                path: '/docs/part1/chapter1-embodied-intelligence',
                component: ComponentCreator('/docs/part1/chapter1-embodied-intelligence', '344'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part1/chapter2-sensors-actuators-locomotion',
                component: ComponentCreator('/docs/part1/chapter2-sensors-actuators-locomotion', '359'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part1/chapter3-bio-inspired-humanoid-design',
                component: ComponentCreator('/docs/part1/chapter3-bio-inspired-humanoid-design', 'b3e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part1/chapter4-motion-planning-control',
                component: ComponentCreator('/docs/part1/chapter4-motion-planning-control', '60d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part1/chapter5-cognitive-architectures',
                component: ComponentCreator('/docs/part1/chapter5-cognitive-architectures', 'c2e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part2/chapter10-safety-constraints-compliance',
                component: ComponentCreator('/docs/part2/chapter10-safety-constraints-compliance', '1f9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part2/chapter6-autonomous-decision-making',
                component: ComponentCreator('/docs/part2/chapter6-autonomous-decision-making', '26a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part2/chapter7-physical-action-planning',
                component: ComponentCreator('/docs/part2/chapter7-physical-action-planning', 'de7'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part2/chapter8-llm-driven-controllers',
                component: ComponentCreator('/docs/part2/chapter8-llm-driven-controllers', '64d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part2/chapter9-perception-vision-affordance',
                component: ComponentCreator('/docs/part2/chapter9-perception-vision-affordance', '624'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part3/chapter11-simulation-pipelines',
                component: ComponentCreator('/docs/part3/chapter11-simulation-pipelines', '54e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part3/chapter12-ros2-realtime-control',
                component: ComponentCreator('/docs/part3/chapter12-ros2-realtime-control', '51f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part3/chapter13-embedded-microcontrollers',
                component: ComponentCreator('/docs/part3/chapter13-embedded-microcontrollers', '2a7'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part3/chapter14-cloud-robotics',
                component: ComponentCreator('/docs/part3/chapter14-cloud-robotics', '47b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part4/chapter15-intelligent-learning-platform',
                component: ComponentCreator('/docs/part4/chapter15-intelligent-learning-platform', '1f3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part4/chapter16-typescript-plugin-engineering',
                component: ComponentCreator('/docs/part4/chapter16-typescript-plugin-engineering', 'e9c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part4/chapter17-build-time-automation',
                component: ComponentCreator('/docs/part4/chapter17-build-time-automation', 'b9a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part4/chapter18-mdx-interactive-components',
                component: ComponentCreator('/docs/part4/chapter18-mdx-interactive-components', '9d3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/part4/chapter19-intelligent-content-validation',
                component: ComponentCreator('/docs/part4/chapter19-intelligent-content-validation', '2fd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/welcome',
                component: ComponentCreator('/docs/welcome', 'a2c'),
                exact: true
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/',
    component: ComponentCreator('/', '2e1'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
