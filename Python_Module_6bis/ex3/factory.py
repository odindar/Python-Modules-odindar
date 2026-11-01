from abc import ABC, abstractmethod

from ._entities import Flameling, Morphagon, Pyrodon, Shiftling
from .creature import Creature


class CreatureFactory(ABC):
    """Abstract factory: builds one family of related creatures."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Build the base (first stage) creature of the family."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Build the evolved (second stage) creature of the family."""


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
