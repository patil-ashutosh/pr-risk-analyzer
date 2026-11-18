# Project Documentation

Welcome to the PR Risk Analyzer documentation.

This documentation describes the **current implementation** and records the reasoning behind important engineering decisions. Planned capabilities are explicitly labelled as future work.

## Start here

1. [Architecture Overview](architecture/overview.md)
2. [System Context](architecture/system-context.md)
3. [Component Design](architecture/component-design.md)
4. [Class Diagrams](architecture/class-diagrams.md)
5. [Sequence Diagrams](architecture/sequence-diagrams.md)
6. [Data Flow](architecture/data-flow.md)

## Architecture

- [Overview](architecture/overview.md)
- [System Context](architecture/system-context.md)
- [Container Design](architecture/container-design.md)
- [Component Design](architecture/component-design.md)
- [Class Diagrams](architecture/class-diagrams.md)
- [Sequence Diagrams](architecture/sequence-diagrams.md)
- [Data Flow](architecture/data-flow.md)

## Design decisions

- [ADR-0001: Provider Abstraction](design-decisions/0001-use-provider-abstraction.md)
- [ADR-0002: Pydantic Review Schema](design-decisions/0002-use-pydantic-for-review-schema.md)
- [ADR-0003: Streamlit for the MVP](design-decisions/0003-use-streamlit-for-mvp.md)

## Engineering guides

- [Coding Standards](engineering/coding-standards.md)
- [Testing Strategy](engineering/testing-strategy.md)
- [Error Handling](engineering/error-handling.md)
- [Security](engineering/security.md)
- [Adding an AI Provider](engineering/adding-a-new-provider.md)

## Learning resources

- [Object-Oriented Design](learning/object-oriented-design.md)
- [SOLID Principles](learning/solid-principles.md)
- [Dependency Injection](learning/dependency-injection.md)
- [Clean Architecture](learning/clean-architecture.md)

## Keeping documentation accurate

When code changes alter responsibilities, dependencies, runtime flows, contracts, security assumptions, or setup steps, update the relevant documentation in the same change.

Mermaid source in Markdown is the canonical editable form for diagrams. Exported images may be added for presentations, but should not become the only source of truth.
