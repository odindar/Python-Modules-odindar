from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (
    AggressiveStrategy,
    BattleStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    """Round-robin: every opponent faces every other one exactly once."""
    fighters = [
        (factory.create_base(), strategy) for factory, strategy in opponents
    ]
    summary = ", ".join(
        f"({creature.name}+{strategy.name})" for creature, strategy in fighters
    )
    print(f" [ {summary} ]")
    print("*** Tournament ***")
    print(f"{len(fighters)} opponents involved")

    try:
        for i in range(len(fighters)):
            for j in range(i + 1, len(fighters)):
                first, first_strategy = fighters[i]
                second, second_strategy = fighters[j]
                print("\n* Battle *")
                print(first.describe())
                print(" vs.")
                print(second.describe())
                print(" now fight!")
                for message in first_strategy.act(first):
                    print(message)
                for message in second_strategy.act(second):
                    print(message)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


if __name__ == "__main__":
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    battle([
        (flame_factory, normal),
        (transform_factory, aggressive),
    ])

    print("\nTournament 1 (error)")
    battle([
        (transform_factory, aggressive),
        (flame_factory, aggressive),
    ])
