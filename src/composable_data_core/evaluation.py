"""Recorded experiment evaluation evidence."""

from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class Evaluation:
    """Record metric results computed elsewhere."""

    model_id: str
    metrics: Mapping[str, float]

    def __post_init__(self) -> None:
        """After initialization validation on the dataclass fields."""
        if not self.model_id.strip():
            raise ValueError("model_id must not be empty.")
        if not self.metrics:
            raise ValueError("Evaluation must contain at least one metric.")
        object.__setattr__(self, "metrics", MappingProxyType(dict(self.metrics)))
