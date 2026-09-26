import random


ACHIEVEMENTS: list[str] = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "Hidden Path Finder", "First Steps", "Collector Supreme",
    "Untouchable", "Sharp Mind", "Boss Slayer"
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(3, len(ACHIEVEMENTS) - 3)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    all_distinct: set[str] = set()
    for p, ach in players.items():
        print(f"Player {p}: {ach}")
        all_distinct = all_distinct.union(ach)

    print(f"All distinct achievements: {all_distinct}")

    common: set[str] = set(all_distinct)
    for ach in players.values():
        common = common.intersection(ach)
    print(f"Common achievements: {common}")

    for p, ach in players.items():
        others: set[str] = set()
        for other_p, other_ach in players.items():
            if p != other_p:
                others = others.union(other_ach)
        only_player: set[str] = ach.difference(others)
        print(f"Only {p} has: {only_player}")

    for p, ach in players.items():
        missing: set[str] = all_distinct.difference(ach)
        print(f"{p} is missing: {missing}")


if __name__ == "__main__":
    main()
