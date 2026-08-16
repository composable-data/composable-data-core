"""Machine-learning learning mode."""

from enum import StrEnum


class LearningMode(StrEnum):
    """Declare whether learning uses a target."""

    SUPERVISED = "supervised"
    UNSUPERVISED = "unsupervised"
