"""Data-problem resolution declaration."""

from dataclasses import dataclass
from typing import Any

from composable_data_core.rationale import Rationale
from composable_data_core.resolution_action import ResolutionAction


@dataclass(frozen=True, slots=True)
class Resolution:
    """Declare what to do about a data problem and why."""

    problem: str
    action: ResolutionAction
    rationale: Rationale
    field: str | None = None
    original_value: Any | None = None
    resolved_value: Any | None = None

    def __post_init__(self) -> None:
        """After initialization validation on the dataclass fields."""
        if not self.problem.strip():
            raise ValueError("Problem description must not be empty.")
        if self.action is ResolutionAction.RECODE and self.resolved_value is None:
            raise ValueError("RECODE resolutions require resolved_value.")
