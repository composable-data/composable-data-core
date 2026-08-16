"""Experiment plan declaration."""

from dataclasses import dataclass

from composable_data_core.problem_type import ProblemType
from composable_data_core.rationale import Rationale


@dataclass(frozen=True, slots=True)
class ExperimentPlan[DatasetRefT]:
    """Declare the analytical experiment."""

    dataset: DatasetRefT
    target: str
    available_features: tuple[str, ...]
    selected_features: tuple[str, ...]
    problem_type: ProblemType
    feature_rationale: Rationale

    def __post_init__(self) -> None:
        """After initialization validation on the dataclass fields."""
        if not self.target.strip():
            raise ValueError("Target must not be empty.")
        if not self.available_features:
            raise ValueError("Available features must not be empty.")
        if not self.selected_features:
            raise ValueError("Selected features must not be empty.")

        unknown = set(self.selected_features) - set(self.available_features)
        if unknown:
            raise ValueError(f"Selected features are not available: {sorted(unknown)}")

        if self.target in self.selected_features:
            raise ValueError("Target must not also appear in selected features.")
