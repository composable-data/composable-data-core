"""Train/test split plan declaration."""

from dataclasses import dataclass

from composable_data_core.rationale import Rationale
from composable_data_core.split_method import SplitMethod


@dataclass(frozen=True, slots=True)
class SplitPlan:
    """Declare how training and test observations should be separated."""

    method: SplitMethod
    test_size: float
    rationale: Rationale
    seed: int | None = None
    group_field: str | None = None
    time_field: str | None = None

    def __post_init__(self) -> None:
        """After initialization validation on the dataclass fields."""
        if not 0.0 < self.test_size < 1.0:
            raise ValueError("test_size must be between 0 and 1.")
        if self.method is SplitMethod.GROUPED and not self.group_field:
            raise ValueError("Grouped splits require group_field.")
        if self.method is SplitMethod.TIME_ORDERED and not self.time_field:
            raise ValueError("Time-ordered splits require time_field.")
