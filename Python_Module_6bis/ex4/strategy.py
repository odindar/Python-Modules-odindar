from abc import ABC, abstractmethod

from ex3 import Creature, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy is asked to act on an unsuitable entity."""


class BattleStrategy(ABC):
    """Abstract strategy: decides HOW an entity behaves during a battle."""

    name: str = "Battle"

    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        """Tell whether `entity` is suitable for this strategy."""

    @abstractmethod
    def act(self, entity: Creature) -> list[str]:
        """Make `entity` act; return the messages of what happened."""

    def _invalid(self, entity: Creature) -> InvalidStrategyError:
        return InvalidStrategyError(
            f"Invalid Creature '{entity.name}' for this "
            f"{self.name.lower()} strategy"
        )


class NormalStrategy(BattleStrategy):
    """Suitable for any entity: it simply attacks."""

    name = "Normal"

    def is_valid(self, entity: Creature) -> bool:
        return True

    def act(self, entity: Creature) -> list[str]:
        if not self.is_valid(entity):
            raise self._invalid(entity)
        return [entity.attack()]


class AggressiveStrategy(BattleStrategy):
    """Suitable for transformable entities: transform, attack, revert."""

    name = "Aggressive"

    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)

    def act(self, entity: Creature) -> list[str]:
        # The isinstance check is repeated here (and not only through
        # is_valid) so that mypy narrows the type of `entity`.
        if not isinstance(entity, TransformCapability):
            raise self._invalid(entity)
        return [entity.transform(), entity.attack(), entity.revert()]
