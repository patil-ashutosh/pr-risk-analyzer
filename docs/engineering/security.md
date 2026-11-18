# Security Considerations

## Source-code privacy

Git diffs can contain proprietary source code, secrets, customer data, or other sensitive information. The application sends the supplied diff to an external AI provider for analysis.

Before using the application with private repositories:
- Confirm that the provider is approved by the organization.
- Review provider data handling, retention, and training policies.
- Follow internal source-code and data-classification policies.
- Remove secrets and unrelated sensitive content from diffs.
- Avoid using production credentials or customer data in examples.

## API keys

- Store API keys in environment variables.
- Keep `.env` out of version control.
- Commit only a placeholder `.env.example`.
- Never print or log API keys.
- Rotate credentials if they are accidentally exposed.

## Prompt injection

A Git diff is untrusted input. It may contain comments or strings that attempt to instruct the model to ignore review instructions or reveal information.

Prompt wording that treats the diff as untrusted data is a useful mitigation, but it is not a complete security boundary. Do not give the model access to tools or secrets it does not need. Validate output and require human review.

## AI output

Pydantic validation checks the response structure and types. It does not prove that findings are correct. Treat findings as recommendations requiring developer verification.

## Logging

Do not log full Git diffs, full prompts, credentials, or sensitive response content by default. Prefer operational metadata such as model identifier, elapsed time, retry count, and sanitized error category.
