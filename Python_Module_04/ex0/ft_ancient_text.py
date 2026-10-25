import sys
from typing import IO


def main() -> None:
    args: list[str] = sys.argv[1:]
    if len(args) != 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = args[0]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file_obj: IO[str] | None = None
    try:
        file_obj = open(filename, 'r', encoding='utf-8')
        content: str = file_obj.read()

        print(content, end="")
        if content and not content.endswith('\n'):
            print()

        print(f"File '{filename}' closed.")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file_obj is not None:
            file_obj.close()


if __name__ == "__main__":
    main()
