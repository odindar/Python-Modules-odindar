import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {players}")

    capitalized_all: list[str] = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {capitalized_all}")

    capitalized_only: list[str] = [p for p in players if p[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}")

    scores: dict[str, int] = {
        p: random.randint(0, 1000) for p in capitalized_all
    }
    print(f"Score dict: {scores}")

    avg_score: float = sum(scores.values()) / len(scores) if scores else 0.0
    print(f"Score average is {round(avg_score, 2)}")

    high_scores: dict[str, int] = {
        k: v for k, v in scores.items() if v > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
