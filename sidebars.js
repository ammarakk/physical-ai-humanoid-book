// @ts-check

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.

 @type {import('@docusaurus/plugin-content-docs').SidebarsConfig}
 */
const sidebars = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Part 1 — Physical AI Foundations',
      items: [
        'part1/intro', // Placeholder chapter
      ],
    },
    {
      type: 'category',
      label: 'Part 2 — ROS 2: The Robotic Nervous System',
      items: [
        'part2/intro', // Placeholder chapter
      ],
    },
    {
      type: 'category',
      label: 'Part 3 — The Digital Twin',
      items: [
        'part3/intro', // Placeholder chapter
      ],
    },
    {
      type: 'category',
      label: 'Part 4 — The AI-Robot Brain (NVIDIA Isaac)',
      items: [
        'part4/intro', // Placeholder chapter
      ],
    },
    {
      type: 'category',
      label: 'Part 5 — Vision-Language-Action Robotics',
      items: [
        'part5/intro', // Placeholder chapter
      ],
    },
  ],

  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    'intro',
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
   */
};

export default sidebars;
