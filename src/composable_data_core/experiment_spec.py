"""Experiment specification declaration."""

from dataclasses import dataclass

from composable_data_core.grain import Grain
from composable_data_core.learning_mode import LearningMode
from composable_data_core.model_plan import ModelPlan
from composable_data_core.problem_type import ProblemType
from composable_data_core.rationale import Rationale
from composable_data_core.resolution import Resolution
from composable_data_core.split_plan import SplitPlan


@dataclass(frozen=True, slots=True)
class ExperimentSpec[DatasetRefT]:
    """Declare a complete analytical experiment before execution."""

    dataset: DatasetRefT

    grain: Grain
    learning_mode: LearningMode
    problem_type: ProblemType

    target: str
    selected_features: tuple[str, ...]
    feature_rationale: Rationale

    resolution: Resolution
    split: SplitPlan

    baseline_id: str
    baseline: ModelPlan

    candidate_id: str
    candidate: ModelPlan

    def __post_init__(self) -> None:
        """Validate the experiment specification."""
        if not self.target.strip():
            raise ValueError("Target must not be empty.")

        if not self.selected_features:
            raise ValueError("Selected features must not be empty.")

        if self.target in self.selected_features:
            raise ValueError("Target must not also appear in selected features.")

        if not self.baseline_id.strip():
            raise ValueError("Baseline ID must not be empty.")

        if not self.candidate_id.strip():
            raise ValueError("Candidate ID must not be empty.")

        if self.baseline_id == self.candidate_id:
            raise ValueError("Baseline and candidate IDs must be different.")
