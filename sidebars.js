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
      label: 'Part I: Physical AI Foundations',
      items: [
        'part1/chapter1-embodied-intelligence',
        'part1/chapter2-sensors-actuators-locomotion',
        'part1/chapter3-bio-inspired-humanoid-design',
        'part1/chapter4-motion-planning-control',
        'part1/chapter5-cognitive-architectures',
      ],
    },
    {
      type: 'category',
      label: 'Part II: Humanoid Agent Systems',
      items: [
        'part2/chapter6-autonomous-decision-making',
        'part2/chapter7-physical-action-planning',
        'part2/chapter8-llm-driven-controllers',
        'part2/chapter9-perception-vision-affordance',
        'part2/chapter10-safety-constraints-compliance',
      ],
    },
    {
      type: 'category',
      label: 'Part III: Software & Engineering Stack',
      items: [
        'part3/chapter11-simulation-pipelines',
        'part3/chapter12-ros2-realtime-control',
        'part3/chapter13-embedded-microcontrollers',
        'part3/chapter14-cloud-robotics',
      ],
    },
    {
      type: 'category',
      label: 'Part IV: AI/Spec-Driven Authoring Architecture',
      items: [
        'part4/chapter15-intelligent-learning-platform',
        'part4/chapter16-typescript-plugin-engineering',
        'part4/chapter17-build-time-automation',
        'part4/chapter18-mdx-interactive-components',
        'part4/chapter19-intelligent-content-validation',
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
