# ADR-0003: Use Streamlit for the MVP Interface

- **Status:** Accepted
- **Date:** 2026-11-19

## Context

The initial product goal is to validate the PR-review workflow quickly with a small amount of frontend code.

## Decision

Use Streamlit for the MVP user interface.

## Alternatives considered

1. Streamlit for rapid Python-first prototyping.
2. A separate frontend application and backend API.
3. A desktop application.

## Consequences

### Positive

- Fast iteration with Python.
- Minimal frontend infrastructure.
- Suitable for validating the initial user workflow.

### Trade-offs

- UI and backend logic run within the same application process.
- Complex product UX or independent frontend deployment may eventually justify a separate API and frontend.
- The current choice should be revisited when real product requirements demand it.
