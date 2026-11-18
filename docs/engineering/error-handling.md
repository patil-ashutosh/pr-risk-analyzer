# Error Handling

## Goals

The application should fail clearly, preserve useful diagnostic information, and avoid presenting failures as successful reviews.

## Current boundaries

- The UI checks for blank input and displays a warning.
- `PRReviewService` validates blank input as a use-case boundary.
- `GeminiProvider` handles its configured retry and model fallback behavior.
- Provider failures propagate to the UI.
- The UI logs unexpected failures and shows a generic user-facing message.

## Principles

- Do not return an empty `PRReview` merely because the AI provider failed.
- Distinguish invalid user input from provider unavailability and malformed provider output.
- Retry only errors that are deliberately classified as transient.
- Keep retry count and timeout bounded.
- Preserve the original exception when raising a higher-level error.
- Avoid logging secrets, full prompts, or raw diffs.

## Future improvement areas

Provider-specific tests and more precise error classification may be added as requirements emerge. Do not assume every HTTP error is retryable. Rate limits, authentication failures, invalid requests, timeouts, and server errors require different handling.

The exact retry policy must match the current implementation and tests.
