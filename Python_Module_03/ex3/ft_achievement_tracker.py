import random


ACHIEVEMENTS: list[str] = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "Hidden Path Finder", "First Steps", "Collector Supreme",
    "Untouchable", "Sharp Mind", "Boss Slayer", "Night Owl",
    "Lucky Strike", "Dragon Tamer", "Mountain Climber", "Deep Diver",
    "Quest Master", "Silent Hunter", "Gold Hoarder", "Pixel Perfect",
    "Combo King", "Iron Will", "Star Collector", "Bug Hunter",
    "Time Traveler", "Legend Born", "Last Stand", "Sky Walker",
    "Map Maker", "Rune Reader", "Trap Dodger", "Loot Goblin",
    "Team Player", "Lone Wolf", "Fast Learner", "Berserker",
    "Peacemaker",
]


def gen_player_achievements() -> set[str]:
    low: int = len(ACHIEVEMENTS) * 2 // 5
    high: int = len(ACHIEVEMENTS) * 3 // 5
    count: int = random.randint(low, high)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    players: list[tuple[str, set[str]]] = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements()),
    ]

    for name, achievements in players:
        print(f"Player {name}: {achievements}")
    print()

    all_distinct: set[str] = set()
    for name, achievements in players:
        all_distinct = all_distinct.union(achievements)
    print(f"All distinct achievements: {all_distinct}")
    print()

    common: set[str] = set(all_distinct)
    for name, achievements in players:
        common = common.intersection(achievements)
    print(f"Common achievements: {common}")
    print()

    for name, achievements in players:
        others: set[str] = set()
        for other_name, other_achievements in players:
            if other_name != name:
                others = others.union(other_achievements)
        only_player: set[str] = achievements.difference(others)
        print(f"Only {name} has: {only_player}")
    print()

    every_achievement: set[str] = set(ACHIEVEMENTS)
    for name, achievements in players:
        missing: set[str] = every_achievement.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
