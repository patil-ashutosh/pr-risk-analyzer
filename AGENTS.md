# Repository Instructions for AI Coding Agents

## Project purpose

PR Risk Analyzer is a Python/Streamlit application that accepts a Git diff, delegates analysis to an AI provider, validates a structured review, and displays findings.

This repository is also a practical reference for maintainable AI application design. Keep explanations and diagrams aligned with the actual implementation.

## Read before significant changes

- `README.md`
- `docs/README.md`
- `docs/architecture/overview.md`
- Relevant engineering guides and ADRs

For class or runtime-flow changes, also inspect:
- `docs/architecture/class-diagrams.md`
- `docs/architecture/sequence-diagrams.md`

## Current module boundaries

- `app.py`: Streamlit bootstrap and composition root.
- `ui/`: presentation and Streamlit rendering.
- `services/`: application use-case orchestration.
- `providers/`: provider abstraction and external AI integrations.
- `schemas/`: shared Pydantic data contracts.
- `config/`: environment-backed configuration.
- `tests/`: automated tests.

## Engineering constraints

- Keep provider SDK calls out of the UI and application service.
- Keep `PRReviewService` dependent on `AIProvider`, not a concrete provider.
- Keep external provider responses validated against the shared schema.
- Prefer simple designs; do not add abstractions without a concrete need.
- Add type hints to public functions and methods.
- Do not introduce microservices, queues, databases, registries, or frameworks without a requirement.
- Never commit secrets or real `.env` contents.
- Do not log full Git diffs, API keys, or sensitive prompts.

## Change workflow

Before significant changes:
1. Inspect relevant code and tests.
2. Read relevant documentation and ADRs.
3. Identify affected modules, contracts, and dependency direction.
4. Explain the proposed design and trade-offs.
5. Implement incrementally.

After changes:
1. Add or update tests.
2. Run `python -m pytest -v`.
3. Run `python -m compileall config schemas providers services ui app.py` when relevant.
4. Update affected diagrams, ADRs, README, and guides.
5. Clearly state what was tested and what was not.

## AI output and security

Treat Git diffs and model-generated findings as untrusted. Schema validation checks structure, not factual correctness. Do not claim findings are verified without evidence.
