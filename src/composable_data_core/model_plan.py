"""Model plan for a machine learning estimator."""

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from composable_data_core.model_role import ModelRole
from composable_data_core.rationale import Rationale


@dataclass(frozen=True, slots=True)
class ModelPlan:
    """Declare one estimator choice and why it was chosen."""

    estimator: str
    role: ModelRole
    rationale: Rationale
    parameters: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the model plan."""
        if not self.estimator.strip():
            raise ValueError("Estimator name must not be empty.")
