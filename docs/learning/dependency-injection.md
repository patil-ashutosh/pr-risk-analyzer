# Dependency Injection

## What is a dependency?

`PRReviewService` needs an AI provider to analyze a Git diff. That provider is a dependency of the service.

## Constructor injection in this project

```python
class PRReviewService:
    def __init__(self, ai_provider: AIProvider):
        self.ai_provider = ai_provider
```

The service does not construct `GeminiProvider` internally. The caller supplies the dependency.

## Composition root

`app.py` creates the concrete objects and connects them:

```python
ai_provider = GeminiProvider(settings=settings)
review_service = PRReviewService(ai_provider=ai_provider)
```

This is the composition root: the place where concrete dependencies are assembled.

## Why it helps

Production wiring can inject `GeminiProvider`. A unit test can inject a fake provider. The service code remains unchanged.

## Dependency Inversion versus Dependency Injection

- Dependency Inversion is a design principle about depending on abstractions.
- Dependency Injection is a technique for supplying dependencies from outside an object.

They are related but not synonymous.
