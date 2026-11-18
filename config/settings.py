import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    """
    Centralized application configuration.
    """

    gemini_api_key: str
    model_fallbacks: tuple[str, ...]
    max_retries: int
    request_timeout_ms: int

    @classmethod
    def from_environment(cls) -> "Settings":
        """
        Load application settings from environment variables.
        """

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        return cls(
            gemini_api_key=api_key,
            model_fallbacks=(
                "gemini-3.5-flash-lite",
                "gemini-3.7-flash",
                "gemini-3.8-flash",
            ),
            max_retries=2,
            request_timeout_ms=20_000,
        )

settings = Settings.from_environment()
