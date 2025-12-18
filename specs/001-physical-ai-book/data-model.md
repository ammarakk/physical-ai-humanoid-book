# Data Model: Physical AI & Humanoid Robotics Book

This document outlines the key data entities for the book content.

-   **Book**: The top-level entity representing the entire publication.
    -   **Attributes**:
        -   `title`: The main title of the book.
        -   `subtitle`: The subtitle of the book.
        -   `version`: The version of the book.
        -   `authors`: A list of authors.
    -   **Relationships**:
        -   Has many `Parts`.

-   **Part**: A major section of the book, equivalent to a module.
    -   **Attributes**:
        -   `title`: The title of the part (e.g., "Physical AI Foundations").
        -   `order`: The numerical order of the part within the book.
    -   **Relationships**:
        -   Belongs to a `Book`.
        -   Has many `Chapters`.

-   **Chapter**: A single content file within a Part.
    -   **Attributes**:
        -   `title`: The title of the chapter.
        -   `order`: The numerical order of the chapter within the part.
        -   `content`: The Markdown/MDX content of the chapter.
        -   `summary`: A brief summary of the chapter.
        -   `learning_objectives`: A list of learning objectives.
    -   **Relationships**:
        -   Belongs to a `Part`.
        -   Has many `Diagrams`, `Code Examples`, and `Citations`.

-   **Diagram**: An architectural or workflow illustration.
    -   **Attributes**:
        -   `title`: The title of the diagram.
        -   `filename`: The image file name (e.g., `ros2-graph.png`).
        -   `caption`: A descriptive caption for the diagram.
    -   **Relationships**:
        -   Belongs to a `Chapter`.

-   **Code Example**: A reproducible block of code.
    -   **Attributes**:
        -   `title`: The title of the code example.
        -   `language`: The programming language (e.g., `python`).
        -   `code`: The code content.
    -   **Relationships**:
        -   Belongs to a `Chapter`.

-   **Citation**: A reference to an external source.
    -   **Attributes**:
        -   `key`: A unique key for the citation (e.g., `[Smith2021]`).
        -   `full_citation`: The full APA 7th edition citation text.
    -   **Relationships**:
        -   Belongs to a `Chapter`.
