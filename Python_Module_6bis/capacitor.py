from ex3 import Creature, TransformCapability, TransformCreatureFactory


def test_capability(label: str, creature: Creature) -> None:
    """describe, attack, transform, attack again, revert."""
    print(f" {label}:")
    print(creature.describe())
    print(creature.attack())
    if not isinstance(creature, TransformCapability):
        print(f"{creature.name} cannot transform.")
        return
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


if __name__ == "__main__":
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()
    test_capability("base", factory.create_base())
    test_capability("evolved", factory.create_evolved())
