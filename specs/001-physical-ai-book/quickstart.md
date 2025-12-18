# Quickstart Guide

This guide explains how to set up the development environment for the "Physical AI & Humanoid Robotics Book" and contribute content.

## Prerequisites

-   [Node.js](https://nodejs.org/) (v16.14 or later)
-   [Yarn](https://yarnpkg.com/) (v1 or v2)
-   [Git](https://git-scm.com/)

## Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies**:
    ```bash
    yarn install
    ```

## Running the Development Server

To start a local development server with live reloading, run:

```bash
yarn start
```

This command will start a local development server and open up a browser window. Most changes are reflected live without having to restart the server.

## Building the Website

To generate a static production build of the website, run:

```bash
yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## Content Contribution

-   All book content is located in the `docs/` directory.
-   Content is written in Markdown (`.md`) or MDX (`.mdx`) for interactive components.
-   Follow the existing directory structure for parts and chapters.
-   Ensure all claims are supported by citations, following the APA 7th edition format.
-   All contributions must adhere to the principles outlined in the project's constitution.
