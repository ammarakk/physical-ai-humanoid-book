<!--
---
Sync Impact Report
---
- Version change: 0.0.0 → 1.0.0
- Modified principles: All principles are new.
- Added sections:
    - Core Principles
    - Standards
    - Constraints
    - Required Book Coverage
    - Docusaurus Engineering Requirements
    - Reusable Intelligence Components (RI Skills)
    - Agent-Optimized Storage Requirements
    - Success Criteria
    - Governance
- Removed sections: All placeholder sections are removed.
- Templates requiring updates:
    - ✅ .specify/templates/plan-template.md
    - ✅ .specify/templates/spec-template.md
    - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None.
-->

# Physical AI Humanoid Book — An AI/Spec-Driven Technical Publication

## Purpose
Define the governing principles, standards, constraints, workflows, and success requirements for producing a rigorous, reproducible, academically sound book on Physical AI and Humanoid Systems using Docusaurus, Spec-Kit Plus, Claude Code, and agentic tooling.

## 1. Core Principles

### 1.1 Accuracy
- All claims validated through primary sources.
- Technical explanations grounded in verified robotics, AI, and engineering research.

### 1.2 Clarity
- Target audience: computer science, robotics, AI engineering.
- Writing level: Flesch-Kincaid grade 10–12.
- Use precise, unambiguous terminology.

### 1.3 Reproducibility
- All code, diagrams, and processes must be replicable.
- Each claim must have direct traceability (claim → citation → implementation).

### 1.4 Rigor
- Prefer peer-reviewed sources, academic standards, and official documentation.
- All statements must meet academic and engineering correctness.

## 2. Standards

### 2.1 Citation Requirements
- Format: APA 7th edition.
- Minimum 15 total sources.
- Minimum 50% peer-reviewed.
- Every technical, scientific, historical, or numerical claim must include a citation.

### 2.2 Plagiarism
- 0% tolerance.
- All chapters must pass plagiarism checks.

### 2.3 Writing Standards
- Consistent terminology.
- Use diagrams, tables, and code blocks where appropriate.
- Uniform style across all chapters.

## 3. Constraints

### 3.1 Word Count
- Final manuscript: 5,000–7,000 words.

### 3.2 Output Format
- Primary: Docusaurus website.
- Secondary: PDF with embedded citations.
- Hosting: GitHub Pages.

### 3.3 Tooling
- Mandatory Spec-Kit Plus workflow:
  /sp.constitution
  /sp.specification
  /sp.clarify
  /sp.plan
  /sp.implement
- All content managed using Claude Code, MCP tools, Docusaurus plugins, and agent-based file operations.

## 4. Required Book Coverage

### 4.1 Physical AI Foundations
- Embodied intelligence
- Sensors, actuators, locomotion
- Bio-inspired humanoid design
- Motion planning and control systems
- Cognitive architectures for embodied AI

### 4.2 Humanoid Agent Systems
- Autonomous decision-making
- Physical action planning
- LLM-driven controllers
- Perception, vision, and affordance modeling
- Safety constraints and compliance

### 4.3 Software & Engineering Stack
- Simulation pipelines
- ROS2 and real-time control
- Embedded microcontrollers
- Cloud robotics and distributed agents

### 4.4 AI/Spec-Driven Authoring Architecture
- Transforming Docusaurus into an intelligent learning platform
- TypeScript plugin engineering
- Build-time analysis and automation
- MDX interactive components
- Intelligent content validation

## 5. Docusaurus Engineering Requirements

### 5.1 Custom Plugins
- Summary generator
- Cross-reference detector
- Consistency checker
- Quiz generator
- Fact-checking validator

### 5.2 MDX Components
- Interactive humanoid diagrams
- Live robotics code blocks
- Motion simulation embeds
- Glossary and terminology components
- Flashcard generators

### 5.3 Build-Time Intelligence
- Auto-generated indexes
- Metadata extraction
- Automated learning objectives
- Content validation and linting

### 5.4 Theme & UI
- Custom Physical AI theme
- High-performance build: caching, lazy loading, code splitting

## 6. Reusable Intelligence Components (RI Skills)

### 6.1 Validation Skills
- Factual verification
- Citation completeness
- Pedagogical clarity checks

### 6.2 Summarization Skills
- Auto chapter summaries
- Key concept extraction

### 6.3 Assessment Skills
- Multiple-choice generation
- Concept comprehension questions

### 6.4 Cross-Reference Skills
- Detect redundant explanations
- Suggest linking sections
- Ensure conceptual coherence

### 6.5 Consistency Skills
- Style uniformity
- Terminology enforcement
- Unit and notation consistency

## 7. Agent-Optimized Storage Requirements

### 7.1 Content-Addressable Storage
- Hash-based versioning and deduplication.

### 7.2 Metadata Indexing
- Concepts, citations, figures, and examples indexed.

### 7.3 Transactional Editing
- Multi-file atomic changes.

### 7.4 Cloud Integration
- Cloudflare R2 or S3 for scalable storage.

### 7.5 Agent-Friendly APIs
- Simplified read/write/search operations.
- Compatible with LLM-aware tooling.

## 8. Success Criteria

### 8.1 Academic Quality
- All claims verified with reliable sources.
- 0% plagiarism.
- APA citation compliance.
- Passes fact-checking review.

### 8.2 Technical Quality
- Docusaurus builds without errors.
- All custom plugins functional.
- Interactive components stable and responsive.

### 8.3 Workflow Compliance
- All chapters produced through Spec-Kit Plus workflow.
- Reusable intelligence components implemented.
- Storage layer fully functional.

### 8.4 Educational Quality
- Readers obtain foundational and advanced understanding of Physical AI and humanoid systems.
- Interactive components enhance learning outcomes.

## Governance
This Constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All PRs and reviews must verify compliance with this constitution.

**Version**: 1.0.0 | **Ratified**: 2025-12-07 | **Last Amended**: 2025-12-07