---
id: 3
title: Create Implementation Plan for Physical AI Book
stage: plan
date: 2025-12-07
surface: agent
model: Gemini
feature: 001-physical-ai-book
branch: 001-physical-ai-book
user: User
command: /sp.plan
labels: ["plan", "architecture"]
links:
  spec: specs/001-physical-ai-book/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-physical-ai-book/plan.md
  - specs/001-physical-ai-book/research.md
  - specs/001-physical-ai-book/data-model.md
  - specs/001-physical-ai-book/contracts/README.md
  - specs/001-physical-ai-book/quickstart.md
tests:
  - null
---

## Prompt

---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType gemini`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

## Response snapshot

I have successfully generated the implementation plan and associated design artifacts for the "Physical AI & Humanoid Robotics Book" feature.

**Generated Artifacts**:
-   **Implementation Plan**: `specs/001-physical-ai-book/plan.md`
-   **Research Strategy**: `specs/001-physical-ai-book/research.md`
-   **Data Model**: `specs/001-physical-ai-book/data-model.md`
-   **API Contracts**: `specs/001-physical-ai-book/contracts/README.md` (placeholder)
-   **Quickstart Guide**: `specs/001-physical-ai-book/quickstart.md`

**Agent Context**: The agent's context has been updated with the technologies specified in the plan.

The project is now ready for the task generation phase.

**Suggested Next Command**: `/sp.tasks`

## Outcome

- ✅ Impact: The implementation plan is now complete, providing a clear roadmap for the development of the book.
- 🧪 Tests: No tests were run.
- 📁 Files: 5 files were created.
- 🔁 Next prompts: `/sp.tasks`
- 🧠 Reflection: The planning phase was successful in breaking down the high-level specification into a concrete set of design artifacts, setting the stage for task generation.
