import sys


def main() -> None:
    print("=== Command Quest ===")
    program_name: str = sys.argv[0]
    print(f"Program name: {program_name}")

    args: list[str] = sys.argv[1:]

    if not args:
        print("No arguments provided!")
        print("Total arguments: 1")
    else:
        count: int = len(args)
        print(f"Arguments received: {count}")
        for i in range(count):
            print(f"Argument {i + 1}: {args[i]}")
        print(f"Total arguments: {count + 1}")


if __name__ == "__main__":
    main()
