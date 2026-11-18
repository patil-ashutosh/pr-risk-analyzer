
from abc import ABC, abstractmethod

from schemas.review import PRReview


class AIProvider(ABC):
    """
    Contract for AI providers.

    All AI provider implementations must support
    analyzing a Git diff and returning a PRReview.
    """

    @abstractmethod
    def analyze(self, git_diff: str) -> PRReview:
        pass
