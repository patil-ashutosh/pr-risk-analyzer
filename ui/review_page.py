
import streamlit as st

from services.review_service import PRReviewService


def render_review_page(review_service: PRReviewService) -> None:
    """Render the PR review page and handle user interactions."""

    st.title("🔍 PR Risk Analyzer")
    st.caption("AI-powered code review assistant")

    git_diff = st.text_area(
        "Git Diff",
        height=350,
        placeholder="Paste your Git diff here...",
    )

    if st.button("🔍 Analyze PR", type="primary"):
        if not git_diff.strip():
            st.warning("Please paste a Git diff.")
            return

        try:
            with st.spinner("AI is reviewing your code..."):
                review = review_service.analyze(git_diff)

            st.success("Code review completed!")

            _render_review(review)

        except Exception as error:
            st.error(f"Analysis failed: {error}")


def _render_review(review) -> None:
    """Render the structured PR review result."""

    st.subheader("PR Summary")
    st.write(review.summary)

    st.subheader("Overall Risk")
    st.write(review.overall_risk)

    st.subheader("Findings")
    st.write(f"Total findings: {len(review.findings)}")

    for finding in review.findings:
        with st.expander(finding.title):
            st.write("Category:", finding.category)
            st.write("Severity:", finding.severity)
            st.write("Confidence:", finding.confidence)
            st.write("File:", finding.file or "Not identified")
            st.write("Line:", finding.line or "Not identified")

            st.write("Description:")
            st.write(finding.description)

            st.write("Impact:")
            st.write(finding.impact)

            st.write("Recommendation:")
            st.write(finding.recommendation)

    st.subheader("Missing Tests")

    if not review.missing_tests:
        st.write("No missing tests identified.")
    else:
        for test in review.missing_tests:
            st.write(f"- [{test.priority}] {test.description}")

    with st.expander("View raw JSON"):
        st.json(review.model_dump())
