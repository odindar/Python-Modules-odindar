import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    args: list[str] = sys.argv[1:]
    scores: list[int] = []

    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print(
            "No scores provided. Usage: "
            f"python3 {sys.argv[0]} <score1> <score2>"
        )
        return

    total_players: int = len(scores)
    total_score: int = sum(scores)
    avg: float = total_score / total_players
    high: int = max(scores)
    low: int = min(scores)
    score_range: int = high - low

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {avg}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
