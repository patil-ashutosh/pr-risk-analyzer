# Sequence Diagrams

## 1. Successful review

```mermaid
sequenceDiagram
    actor Developer
    participant UI as review_page.py
    participant Service as PRReviewService
    participant Provider as GeminiProvider
    participant SDK as Google Gen AI SDK
    participant API as Gemini API

    Developer->>UI: Paste diff and click Analyze
    UI->>Service: analyze(git_diff)
    Service->>Service: Validate non-empty input
    Service->>Provider: analyze(git_diff)
    Provider->>Provider: Build prompt
    Provider->>SDK: generate_content(...)
    SDK->>API: HTTPS inference request
    API-->>SDK: Generated response
    SDK-->>Provider: Response object
    Provider->>Provider: Parse / validate PRReview
    Provider-->>Service: PRReview
    Service-->>UI: PRReview
    UI-->>Developer: Render summary and findings
```

## 2. Empty input

```mermaid
sequenceDiagram
    actor Developer
    participant UI as Review Page
    participant Service as PRReviewService
    participant Provider as AIProvider

    Developer->>UI: Click Analyze with empty input
    UI->>UI: Check input for blank content
    Note over UI: Current UI warns and returns
    UI-->>Developer: Show validation warning

    Note over Service,Provider: Service also validates input when called directly
```

The UI currently performs a blank-input check before invoking the service. The service repeats validation as a use-case boundary so callers other than the UI cannot bypass it.

## 3. Provider failure

```mermaid
sequenceDiagram
    participant UI as Review Page
    participant Service as PRReviewService
    participant Provider as GeminiProvider
    participant API as Gemini API

    UI->>Service: analyze(git_diff)
    Service->>Provider: analyze(git_diff)
    Provider->>API: Generate content
    API-->>Provider: Error / timeout
    Provider-->>Service: Raise exception
    Service-->>UI: Exception propagates
    UI->>UI: Log exception and show safe message
```

Exact retry and fallback behavior is implemented in the provider and may change. Keep this diagram synchronized with the actual exception-handling implementation.
