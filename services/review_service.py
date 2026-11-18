
from providers.base import AIProvider
from schemas.review import PRReview


class PRReviewService:
    """
    Application service responsible for PR review orchestration.
    """

    def __init__(self, ai_provider: AIProvider):
        self.ai_provider = ai_provider

    def analyze(self, git_diff: str) -> PRReview:
        """
        Analyze a Git diff and return a validated PR review.
        """

        if not git_diff or not git_diff.strip():
            raise ValueError("Git diff cannot be empty.")

        return self.ai_provider.analyze(git_diff)
