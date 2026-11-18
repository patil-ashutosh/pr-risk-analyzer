# Object-Oriented Design in PR Risk Analyzer

## Why OOP here?

OOP is useful when objects represent meaningful responsibilities, state, or replaceable collaborators. It is not a requirement to turn every function or module into a class.

## Current classes

- `AIProvider`: abstract contract for an AI analysis provider.
- `GeminiProvider`: concrete provider implementation.
- `PRReviewService`: coordinates the review use case and holds an injected provider.
- `Settings`: immutable configuration data.
- `PRReview`, `Finding`, `MissingTest`: structured response models.

## Inheritance and polymorphism

`GeminiProvider` implements `AIProvider`. The service invokes the provider through the shared `analyze()` contract. This is polymorphism: the caller uses a common interface without needing to know the concrete implementation.

## Composition and dependency

`PRReviewService` receives an `AIProvider` object through its constructor and stores a reference to it. This is a has-a relationship and constructor dependency injection. It is not necessary to make the service inherit from the provider.

## Data model relationships

`PRReview` contains a list of `Finding` objects and a list of `MissingTest` objects. These are structured data relationships represented by Pydantic models.

## Design principle

Use inheritance for a genuine substitutable contract. Use composition to collaborate with other objects. Use plain functions and modules when a class would add no meaningful value.
