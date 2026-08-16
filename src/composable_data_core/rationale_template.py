"""Shared rationale types."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class RationaleTemplate(Protocol):
    """Protocol for structured or canonical rationale objects."""

    def render(self) -> str:
        """Return a human-readable explanation."""
