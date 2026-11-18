# Testing Strategy

## Goals

Tests should provide confidence in application behavior while remaining deterministic, fast, and independent of external AI availability.

## Test categories

### Unit tests

Test one class or function with its dependencies replaced by fakes or mocks.

Current example: `tests/test_review_service.py` injects a fake `AIProvider` into `PRReviewService`.

Current service test scenarios:
- Valid diff delegates to the provider and returns its review.
- Blank diff raises `ValueError` and does not call the provider.
- Provider failure propagates to the caller.

### Provider tests

Provider-specific tests should use a fake or mocked SDK client. They should cover:
- Successful parsed response.
- Fallback response parsing if supported.
- Retry on explicitly retryable errors.
- Moving to the next configured model after retry exhaustion.
- Propagation of non-retryable errors.

Do not call the live Gemini API in ordinary unit tests.

### Integration tests

Add integration tests only when a meaningful cross-component behavior needs verification. If a test calls a real external API, mark it clearly and keep it separate from the fast default test suite.

## Running tests

```bash
python -m pytest -v
```

## Test design

- Follow Arrange, Act, Assert.
- Test observable behavior, not private implementation details unless there is a strong reason.
- Keep tests independent of execution order.
- Avoid sleeps and network access in unit tests.
- Use descriptive test names.

## Change checklist

When changing behavior:
1. Add or update relevant tests.
2. Run the focused test file.
3. Run the full suite.
4. Update documentation if contracts or behavior changed.
