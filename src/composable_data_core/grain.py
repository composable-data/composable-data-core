"""Observation grain declaration."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Grain:
    """Declare what one observation represents."""

    observation: str

    def __post_init__(self) -> None:
        """After initialization validation on the dataclass fields."""
        if not self.observation.strip():
            raise ValueError("Grain observation must not be empty.")
