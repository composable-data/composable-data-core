"""Machine-learning problem type."""

from enum import StrEnum


class ProblemType(StrEnum):
    """Supported supervised prediction problem types."""

    CLASSIFICATION = "classification"
    REGRESSION = "regression"
