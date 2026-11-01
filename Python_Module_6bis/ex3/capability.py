from abc import ABC, abstractmethod


class TransformCapability(ABC):
    """An ability that a type may have. Deliberately NOT a Creature."""

    def __init__(self) -> None:
        super().__init__()
        self._transformed: bool = False

    @property
    def is_transformed(self) -> bool:
        return self._transformed

    @abstractmethod
    def transform(self) -> str:
        """Enter the transformed state and return a message."""

    @abstractmethod
    def revert(self) -> str:
        """Go back to the normal state and return a message."""
