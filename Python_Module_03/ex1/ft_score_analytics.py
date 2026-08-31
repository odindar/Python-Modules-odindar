import sys

def main() -> None:
    args: list[str] = sys.argv[1:]
    if not args:
        print("=== Player Score Analytics ===")
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2>")
        return

    scores: list[int] = []
    print("=== Player Score Analytics ===")
    
    for x in args:
        try:
            scores.append(int(x))
        except ValueError:
            print(f"Invalid parameter: '{x}'")

    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2>")
        return

    total: int = sum(scores)
    count: int = len(scores)
    
    print(f"Scores processed: {scores}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {total / count}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")

if __name__ == "__main__":
    main()