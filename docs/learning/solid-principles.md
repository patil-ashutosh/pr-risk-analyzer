# SOLID Principles Through This Project

SOLID is a set of design principles, not a checklist requiring extra classes in every application.

## S — Single Responsibility Principle

A module or class should have one cohesive reason to change.

Examples:
- `GeminiProvider` changes when Gemini integration behavior changes.
- `PRReviewService` changes when review-use-case orchestration changes.
- `review_page.py` changes when presentation behavior changes.

## O — Open/Closed Principle

Software should be open to useful extension without requiring repeated modification of stable core logic.

The provider contract allows another provider implementation to be added while keeping the service dependent on the same abstraction. This does not mean no existing file ever changes; application wiring and tests may still need updates.

## L — Liskov Substitution Principle

A concrete implementation should be usable wherever its abstraction is expected.

A new `AIProvider` implementation must honor the same input, output, and failure expectations as `GeminiProvider`.

## I — Interface Segregation Principle

Clients should not depend on methods they do not use.

The current provider contract is intentionally small. Avoid adding unrelated capabilities to it.

## D — Dependency Inversion Principle

High-level policy should depend on abstractions rather than low-level implementation details.

`PRReviewService` depends on `AIProvider`, while `GeminiProvider` implements that contract.

## Practical caution

Do not claim a principle is satisfied merely because an interface or class exists. Evaluate whether the design actually reduces coupling and improves changeability.
