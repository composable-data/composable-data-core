"""Train/test split method."""

from enum import StrEnum


class SplitMethod(StrEnum):
    """Common train/test partition strategies."""

    RANDOM = "random"
    STRATIFIED = "stratified"
    GROUPED = "grouped"
    TIME_ORDERED = "time_ordered"
