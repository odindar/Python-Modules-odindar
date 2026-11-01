from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    """Build the base then the evolved creature; describe and attack."""
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory_a: CreatureFactory,
                factory_b: CreatureFactory) -> None:
    """Make the base creatures of two factories fight."""
    print("Testing battle")
    fighter_a = factory_a.create_base()
    fighter_b = factory_b.create_base()
    print(fighter_a.describe())
    print(" vs.")
    print(fighter_b.describe())
    print(" fight!")
    print(fighter_a.attack())
    print(fighter_b.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    test_factory(flame_factory)
    print()
    test_factory(transform_factory)
    print()
    test_battle(flame_factory, transform_factory)
