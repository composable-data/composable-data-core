"""Data-problem resolution action."""

from enum import StrEnum


class ResolutionAction(StrEnum):
    """Common analyst responses to identified data problems."""

    DROP = "drop"
    RECODE = "recode"
    IMPUTE = "impute"
    FLAG = "flag"
