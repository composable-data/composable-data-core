"""Model role declaration."""

from enum import StrEnum


class ModelRole(StrEnum):
    """Role played by a model in an experiment."""

    BASELINE = "baseline"
    CANDIDATE = "candidate"
