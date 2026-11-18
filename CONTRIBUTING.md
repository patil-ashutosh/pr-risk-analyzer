# Contributing

Thank you for considering a contribution.

## Before making changes

1. Read `README.md`.
2. Read `AGENTS.md` and relevant architecture documentation.
3. Check existing issues and open pull requests to avoid duplicated work.
4. For significant design changes, describe the problem and proposed approach before implementation.

## Development setup

```bash
python -m venv venv
# Git Bash on Windows:
source venv/Scripts/activate
# macOS/Linux:
source venv/bin/activate

python -m pip install -r requirements.txt
cp .env.example .env
```

Add your own Gemini API key to `.env`. Never commit this file.

## Tests

```bash
python -m pytest -v
```

Unit tests should not require a live AI API call. Use fake or mocked provider clients.

## Pull requests

A good pull request should:
- Explain the problem and solution.
- Keep changes focused.
- Include tests for behavior changes.
- Update documentation and diagrams when needed.
- Mention known limitations and follow-up work.

## Architecture changes

For changes to module responsibilities, dependencies, contracts, or runtime flows:
- Update relevant Mermaid diagrams.
- Add an ADR for significant decisions.
- Keep current-state documentation separate from future proposals.

## Security

Do not submit real API keys, secrets, proprietary source code, or customer data in issues or test fixtures.
