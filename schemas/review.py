
from typing import Literal

from pydantic import BaseModel, Field


class Finding(BaseModel):
    category: Literal[
        "BUG",
        "SECURITY",
        "PERFORMANCE",
        "MAINTAINABILITY",
    ]

    severity: Literal[
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
    ]

    confidence: Literal["LOW", "MEDIUM", "HIGH"]

    file: str | None = None
    line: int | None = None

    title: str
    description: str
    impact: str
    recommendation: str


class MissingTest(BaseModel):
    description: str

    priority: Literal[
        "LOW",
        "MEDIUM",
        "HIGH",
    ]


class PRReview(BaseModel):
    summary: str

    overall_risk: Literal[
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
    ]

    findings: list[Finding] = Field(default_factory=list)

    missing_tests: list[MissingTest] = Field(
        default_factory=list
    )
