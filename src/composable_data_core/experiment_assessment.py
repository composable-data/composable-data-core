"""Experiment assessment declaration."""

from dataclasses import dataclass

from composable_data_core.rationale import Rationale


@dataclass(frozen=True, slots=True)
class ExperimentAssessment:
    """Record the conclusion drawn from comparable experiment evidence."""

    comparison: str
    conclusion: str
    rationale: Rationale
    winner_model_id: str | None = None
    baseline_beaten: bool | None = None

    def __post_init__(self) -> None:
        """After initialization validation on the dataclass fields."""
        if not self.comparison.strip():
            raise ValueError("Comparison description must not be empty.")
        if not self.conclusion.strip():
            raise ValueError("Conclusion must not be empty.")
