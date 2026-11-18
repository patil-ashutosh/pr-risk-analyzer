
import streamlit as st

from config.settings import settings
from providers.gemini_provider import GeminiProvider
from services.review_service import PRReviewService
from ui.review_page import render_review_page


@st.cache_resource
def get_review_service() -> PRReviewService:
    """Create and cache application dependencies."""

    ai_provider = GeminiProvider(settings=settings)

    return PRReviewService(
        ai_provider=ai_provider
    )


def main() -> None:
    st.set_page_config(
        page_title="PR Risk Analyzer",
        page_icon="🔍",
        layout="wide",
    )

    review_service = get_review_service()

    render_review_page(review_service)


if __name__ == "__main__":
    main()
