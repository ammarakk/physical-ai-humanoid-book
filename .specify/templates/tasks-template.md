---

description: "Task list template for feature implementation"
---

# Tasks: [FEATURE NAME]

**Input**: Design documents from `/specs/[###-feature-name]/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Docusaurus project**:
  - `docs/`: Markdown content files for book chapters.
  - `src/components/`: Custom React components used in MDX.
  - `src/pages/`: Standalone React pages.
  - `docusaurus.config.js`: Main configuration file.
  - `sidebars.js`: Documentation sidebar configuration.
- Paths shown below assume this Docusaurus structure.

<!-- 
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.
  
  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/
  
  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment
  
  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic Docusaurus structure.

- [ ] T001 Initialize Docusaurus site using `npx create-docusaurus@latest`
- [ ] T002 Configure `docusaurus.config.js` with project title, theme, and GitHub pages deployment settings.
- [ ] T003 [P] Customize theme by editing files in `src/css/`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core book structure and shared components.

**⚠️ CRITICAL**: No chapter content work can begin until this phase is complete.

- [ ] T004 Define book structure in `sidebars.js`.
- [ ] T005 [P] Create placeholder Markdown files for each chapter in `docs/`.
- [ ] T006 [P] Develop a shared `Glossary` MDX component in `src/components/Glossary.js`.
- [ ] T007 Implement the `Fact-checking validator` plugin.
- [ ] T008 Configure citation and plagiarism check tools.

**Checkpoint**: Foundation ready - chapter writing can now begin.

---

## Phase 3: User Story 1 - Write Chapter 1 (Priority: P1) 🎯 MVP

**Goal**: Complete the first chapter of the book on "Physical AI Foundations".

**Independent Test**: The chapter renders correctly on the Docusaurus site and contains all required sections.

### Implementation for User Story 1

- [ ] T009 [US1] Write content for "Embodied intelligence" in `docs/chapter1/embodied-intelligence.md`.
- [ ] T010 [P] [US1] Create an interactive diagram as an MDX component in `src/components/HumanoidDiagram.js`.
- [ ] T011 [US1] Embed the `HumanoidDiagram` component in the relevant chapter file.
- [ ] T012 [US1] Add APA 7th edition citations for all claims.
- [ ] T013 [US1] Run content through plagiarism and fact-checking validators.

**Checkpoint**: Chapter 1 is complete, cited, and published on the site.

---

## Phase 4: User Story 2 - Implement Quiz Feature (Priority: P2)

**Goal**: Add a quiz generation plugin and implement a quiz for Chapter 1.

**Independent Test**: Quizzes can be created via a custom MDX tag and are rendered correctly.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T014 [P] [US2] Write a unit test for the quiz generation logic.

### Implementation for User Story 2

- [ ] T015 [US2] Develop the `docusaurus-quiz-generator` plugin.
- [ ] T016 [US2] Add a `<Quiz>` MDX component in `src/components/Quiz.js`.
- [ ] T017 [US2] Create quiz questions for Chapter 1 and add them to `docs/chapter1/summary.md` using the `<Quiz>` component.

**Checkpoint**: The quiz feature is functional and Chapter 1 has a quiz.

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect the entire book.

- [ ] TXXX [P] Review and edit all chapters for clarity and consistency.
- [ ] TXXX Generate final PDF output.
- [ ] TXXX Optimize site performance (image compression, lazy loading).
- [ ] TXXX Validate all links and cross-references.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for [endpoint] in tests/contract/test_[name].py"
Task: "Integration test for [user journey] in tests/integration/test_[name].py"

# Launch all models for User Story 1 together:
Task: "Create [Entity1] model in src/models/[entity1].py"
Task: "Create [Entity2] model in src/models/[entity2].py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
