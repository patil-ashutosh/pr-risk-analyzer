# ADR-0002: Use Pydantic for the Review Response Contract

- **Status:** Accepted
- **Date:** 2026-11-19

## Context

The application needs a predictable structure for AI-generated review results. Unstructured text makes rendering, testing, and future integrations harder.

## Decision

Define `PRReview`, `Finding`, and `MissingTest` as Pydantic models in `schemas/review.py`. Configure the Gemini response to use the review schema and validate parsed output before returning it to the application.

## Alternatives considered

1. Return raw model-generated text.
2. Parse arbitrary JSON manually.
3. Use typed Pydantic models as the shared response contract.

## Consequences

### Positive

- A clear contract is shared by provider, service, UI, and tests.
- Invalid data shapes can be rejected early.
- The UI can render typed fields rather than manually navigating arbitrary dictionaries.

### Trade-offs

- Schema changes require coordinated prompt, provider, UI, test, and documentation updates.
- Structural validation does not guarantee that a finding is true or well-supported.
