# Implementation Plan: Book Platform UI, Chatbot, and Authentication System

**Branch**: `002-book-platform-ui-auth` | **Date**: Tuesday, December 16, 2025 | **Spec**: [link to spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-book-platform-ui-auth/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This feature implements UI enhancements, a RAG-based AI chatbot, and JWT authentication for the existing Docusaurus-based book platform. The implementation includes a robotic-themed landing page with animated hero section, a chatbot using Qwen embeddings and Google Gemini for responses, and a JWT-based authentication system. The solution maintains existing book content and Docusaurus routes while adding new functionality.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: TypeScript/JavaScript for frontend, Python 3.10+ for backend
**Primary Dependencies**: Docusaurus, React, MDX, FastAPI, Qwen embeddings, Google Gemini API, JWT authentication
**Storage**: Vector database for RAG system, JWT-based authentication storage
**Testing**: Jest for frontend, pytest for backend
**Target Platform**: Docusaurus / GitHub Pages with backend API
**Project Type**: Web application with AI chatbot integration
**Performance Goals**: Lightweight animations that don't affect page performance, fast chatbot response times (<3 seconds)
**Constraints**: Must not modify existing Docusaurus routes or markdown book content
**Scale/Scope**: Docusaurus website with robotic-themed UI components, RAG-based chatbot, and JWT authentication system

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **1.1 Accuracy**: All claims are validated through primary sources.
- [x] **1.2 Clarity**: Content is written for the target audience (CS/robotics/AI engineering) at a Flesch-Kincaid grade level of 10-12.
- [x] **1.3 Reproducibility**: All code, diagrams, and processes are replicable.
- [x] **1.4 Rigor**: All statements meet academic and engineering standards of correctness, preferring peer-reviewed sources.
- [x] **2.1 Citation Requirements**: Adheres to APA 7th edition, with at least 15 sources (50% peer-reviewed).
- [x] **2.2 Plagiarism**: Passes plagiarism checks (0% tolerance).
- [x] **3.3 Tooling**: Follows the mandatory Spec-Kit Plus workflow (`/sp.constitution`, `/sp.specify`, etc.).
- [x] **8.0 Success Criteria**: The plan aligns with the book's academic, technical, workflow, and educational success criteria.

## Project Structure

### Documentation (this feature)

```text
specs/002-book-platform-ui-auth/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: The structure below is a recommendation for a Docusaurus project.
  Expand it with the real paths for this feature.
-->

```text
# Docusaurus Project Structure
.
├── docs/                  # Book content in Markdown/MDX
│   └── ...
├── src/
│   ├── components/        # Custom React components for MDX
│   │   ├── LandingPage/
│   │   │   ├── HeroSection.jsx
│   │   │   └── AnimatedRobot.jsx
│   │   ├── Chatbot/
│   │   │   ├── ChatbotInterface.jsx
│   │   │   ├── FloatingChatIcon.jsx
│   │   │   └── ChatbotPage.jsx
│   │   ├── Auth/
│   │   │   ├── Login.jsx
│   │   │   ├── Signup.jsx
│   │   │   └── ProtectedRoute.jsx
│   │   └── Layout/
│   │       ├── Header.jsx
│   │       └── Footer.jsx
│   ├── pages/             # Custom standalone pages
│   │   └── chatbot.jsx    # Dedicated chatbot page
│   └── css/               # Custom styling
│       └── custom.css     # Robotic/AI themed styles
├── blog/                  # Blog posts
│   └── ...
├── static/                # Static assets (images, etc.)
│   └── img/
├── docusaurus.config.js   # Main Docusaurus configuration
├── sidebars.js            # Sidebar configuration for docs
├── backend/               # FastAPI backend
│   ├── main.py
│   ├── auth/
│   ├── models/
│   ├── api/
│   └── requirements.txt
└── package.json           # Project dependencies
```

**Structure Decision**: The existing Docusaurus structure is extended with new components for the landing page hero section, chatbot interface, and authentication system. The backend API is implemented in a separate directory using FastAPI to handle authentication and chatbot functionality. All new UI components follow the robotic/AI theme with dark backgrounds and accent colors.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
