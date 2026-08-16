"""Rationale text type."""

from dataclasses import dataclass

from composable_data_core.rationale_template import RationaleTemplate

type Rationale = str | RationaleTemplate


@dataclass(frozen=True, slots=True)
class RationaleText:
    """Structured wrapper for free-form rationale text."""

    text: str

    def __post_init__(self) -> None:
        """After initialization validation on the dataclass fields."""
        if not self.text.strip():
            raise ValueError("Rationale text must not be empty.")

    def render(self) -> str:
        """Return a human-readable explanation."""
        return self.text
