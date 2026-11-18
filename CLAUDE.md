# Claude Code Instructions

Read `AGENTS.md` first and follow its repository-wide engineering rules.

For architecture work, read:
- `docs/architecture/overview.md`
- `docs/architecture/class-diagrams.md`
- `docs/architecture/sequence-diagrams.md`

For design choices, inspect `docs/design-decisions/`.

Before changing architecture:
1. Explain the affected modules and dependency direction.
2. Identify whether a class, interface, or simpler function is appropriate.
3. Describe the runtime/data flow.
4. State trade-offs and alternatives.

After changing code:
- Add or update tests.
- Run the relevant test suite.
- Update diagrams and documentation when the design changes.
- Do not claim unimplemented capabilities are implemented.
