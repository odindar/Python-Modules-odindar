from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class of every entity of the combat sandbox."""

    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__()
        self.name: str = name
        self.creature_type: str = creature_type

    @abstractmethod
    def attack(self) -> str:
        """Return the message describing this creature's attack."""

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"
