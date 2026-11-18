# Class Diagrams

## Purpose

This document explains actual Python classes and their relationships. A module or file is not automatically a class; module-level functions such as `main()` are shown in component diagrams rather than misrepresented as classes.

## Provider abstraction and service

```mermaid
classDiagram
    class AIProvider {
        <<abstract>>
        +analyze(git_diff: str) PRReview
    }

    class GeminiProvider {
        -settings: Settings
        -client
        +analyze(git_diff: str) PRReview
        -_build_prompt(git_diff: str) str
    }

    class PRReviewService {
        -ai_provider: AIProvider
        +analyze(git_diff: str) PRReview
    }

    AIProvider <|-- GeminiProvider : inheritance / implementation
    PRReviewService --> AIProvider : dependency held by constructor
```

### Relationships

- **Inheritance / implementation:** `GeminiProvider` is a concrete implementation of the abstract `AIProvider` contract.
- **Dependency / has-a reference:** `PRReviewService` receives and stores an `AIProvider` reference through its constructor.
- **Polymorphism:** The service calls `analyze()` through the abstraction without needing to know which concrete provider is supplied.

The service-to-provider relationship is often described informally as composition in application discussions, but the precise UML relationship here is a directed association/dependency: the service holds a reference to an injected provider. The provider is not necessarily owned exclusively by the service.

## Review data model

```mermaid
classDiagram
    class PRReview {
        +summary: str
        +overall_risk: Risk
        +findings: list[Finding]
        +missing_tests: list[MissingTest]
    }

    class Finding {
        +category: Category
        +severity: Severity
        +confidence: Confidence
        +file: str?
        +line: int?
        +title: str
        +description: str
        +impact: str
        +recommendation: str
    }

    class MissingTest {
        +description: str
        +priority: Priority
    }

    PRReview "1" *-- "0..*" Finding : contains
    PRReview "1" *-- "0..*" MissingTest : contains
```

The `PRReview` model contains collections of findings and missing-test suggestions. The composition notation communicates containment in the response object; it does not imply database lifecycle management.

## Configuration relationship

```mermaid
classDiagram
    class Settings {
        +gemini_api_key: str
        +model_fallbacks: tuple
        +max_retries: int
        +request_timeout_ms: int
        +from_environment() Settings
    }

    class GeminiProvider {
        -settings: Settings
    }

    GeminiProvider --> Settings : uses
```

## Module functions

`app.py` contains module-level functions such as `main()` and `get_review_service()`. `ui/review_page.py` contains functions such as `render_review_page()` and `_render_review()`. They are functions, not classes, and are therefore documented in the component and sequence diagrams.

## Design questions to revisit

If a new evidence model, repository context model, or review policy model is added, update these diagrams to reflect the actual schema and relationships. Do not add planned classes to the current-state diagram before they exist in code.
