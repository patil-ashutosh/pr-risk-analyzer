# Coding Standards

These standards aim to keep the code readable and maintainable without imposing ceremony on a small application.

## General

- Prefer clear, descriptive names.
- Keep functions focused on one understandable task.
- Add type hints to public functions and methods.
- Use docstrings to explain purpose, constraints, and non-obvious behavior.
- Avoid comments that merely restate the next line of code.
- Prefer the simplest design that meets a demonstrated requirement.

## Module boundaries

- UI code belongs in `ui/`.
- Use-case orchestration belongs in `services/`.
- External AI SDK and network integration belongs in `providers/`.
- Shared review contracts belong in `schemas/`.
- Runtime configuration belongs in `config/`.

## Object-oriented design

- Use classes where they represent meaningful state, behavior, or a replaceable boundary.
- Do not create a class for every function.
- Prefer composition and constructor injection where they improve replaceability or testability.
- Keep abstractions small and based on actual shared behavior.

## Error handling

- Validate input at the appropriate boundary.
- Do not silently convert provider failures into successful empty reviews.
- Preserve diagnostic context for developers.
- Show safe, useful messages to end users.
- Do not expose API keys, full prompts, or proprietary diffs in logs.

## Dependencies

- Declare directly imported third-party packages in `requirements.txt`.
- Avoid adding dependencies without a concrete need.
- Keep secrets in environment variables, never source code.

## Documentation

Update relevant architecture diagrams, ADRs, and guides when behavior or design changes.
