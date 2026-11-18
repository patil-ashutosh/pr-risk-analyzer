# Adding a New AI Provider

## Goal

Add a provider implementation without coupling the application service or UI to provider-specific SDK details.

## Current contract

Review `providers/base.py`. The `AIProvider` abstraction defines the analysis operation and its return type.

A new provider should:
1. Implement `AIProvider`.
2. Accept its required configuration and client dependencies through construction.
3. Return the shared `PRReview` schema.
4. Keep SDK-specific request and response handling inside the provider.
5. Raise clear errors when analysis cannot be completed.

## Implementation checklist

- [ ] Add provider-specific configuration without exposing secrets.
- [ ] Implement the `AIProvider` contract.
- [ ] Validate provider responses into `PRReview`.
- [ ] Add unit tests using a fake or mocked SDK client.
- [ ] Test success, malformed output, and relevant failure paths.
- [ ] Wire the provider in the application composition root if it is selected.
- [ ] Update class and component diagrams.
- [ ] Update this guide if the provider contract changes.
- [ ] Add an ADR if the choice introduces a significant architectural trade-off.

## Avoid

- Calling provider SDKs from the UI.
- Adding provider-specific conditionals throughout `PRReviewService`.
- Returning unvalidated raw text as if it were a valid review.
- Adding a registry or plugin framework before provider selection requires one.
