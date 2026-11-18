# ADR-0001: Introduce an AI Provider Abstraction

- **Status:** Accepted
- **Date:** 2026-11-19

## Context

The first implementation called the Gemini SDK directly from the AI service. This coupled application behavior to one provider and made isolated service testing harder.

## Decision

Introduce an `AIProvider` abstract base class with an `analyze(git_diff)` contract. `GeminiProvider` implements the contract. `PRReviewService` receives an `AIProvider` through constructor injection.

## Alternatives considered

1. Keep Gemini-specific calls directly in the application service.
2. Introduce a provider interface and inject a concrete implementation.
3. Introduce a provider registry/plugin system immediately.

## Consequences

### Positive

- The service depends on a stable contract rather than Gemini-specific code.
- Tests can inject a fake provider without network access.
- Another provider can be added behind the same contract.

### Trade-offs

- Adds an abstraction and additional files to a small MVP.
- The abstraction must remain small and reflect actual shared behavior.
- A provider registry or factory is not justified until provider selection requirements emerge.

## References

- `providers/base.py`
- `providers/gemini_provider.py`
- `services/review_service.py`
- `tests/test_review_service.py`
