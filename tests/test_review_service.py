
import pytest

from providers.base import AIProvider
from schemas.review import PRReview
from services.review_service import PRReviewService


class FakeAIProvider(AIProvider):
    """A fake provider for testing without external API calls."""

    def __init__(self, review=None, error=None):
        self.review = review
        self.error = error
        self.call_count = 0
        self.received_diff = None

    def analyze(self, git_diff: str) -> PRReview:
        self.call_count += 1
        self.received_diff = git_diff

        if self.error is not None:
            raise self.error

        return self.review


def create_sample_review() -> PRReview:
    return PRReview(
        summary="No major risks identified.",
        overall_risk="LOW",
        findings=[],
        missing_tests=[],
    )


def test_analyze_returns_review_for_valid_diff():
    # Arrange
    expected_review = create_sample_review()
    fake_provider = FakeAIProvider(review=expected_review)
    service = PRReviewService(ai_provider=fake_provider)
    git_diff = "diff --git a/example.py b/example.py"

    # Act
    result = service.analyze(git_diff)

    # Assert
    assert result == expected_review
    assert fake_provider.call_count == 1
    assert fake_provider.received_diff == git_diff


def test_analyze_rejects_empty_diff():
    # Arrange
    fake_provider = FakeAIProvider(review=create_sample_review())
    service = PRReviewService(ai_provider=fake_provider)

    # Act and Assert
    with pytest.raises(ValueError, match="Git diff cannot be empty"):
        service.analyze("   ")

    # Provider should never be called for invalid input.
    assert fake_provider.call_count == 0


def test_analyze_propagates_provider_error():
    # Arrange
    fake_provider = FakeAIProvider(
        error=RuntimeError("AI provider unavailable")
    )
    service = PRReviewService(ai_provider=fake_provider)

    # Act and Assert
    with pytest.raises(RuntimeError, match="AI provider unavailable"):
        service.analyze("some git diff")

    assert fake_provider.call_count == 1
