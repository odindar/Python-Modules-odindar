import sys
from typing import IO


def main() -> None:
    args: list[str] = sys.argv[1:]
    if len(args) != 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = args[0]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file_obj: IO[str] | None = None
    content: str = ""
    try:
        file_obj = open(filename, 'r', encoding='utf-8')
        content = file_obj.read()
        print(content, end="")
        if content and not content.endswith('\n'):
            print()
        print(f"File '{filename}' closed.")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        if file_obj is not None:
            file_obj.close()
        return

    if file_obj is not None:
        file_obj.close()

    print("Transform data:")
    lines: list[str] = content.splitlines()
    transformed_lines: list[str] = [f"{line}#" for line in lines]
    transformed_content: str = "\n".join(transformed_lines) + "\n"
    print(transformed_content, end="")

    new_filename: str = input("Enter new file name (or empty):\n")
    if not new_filename.strip():
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    out_file: IO[str] | None = None
    try:
        out_file = open(new_filename, 'w', encoding='utf-8')
        out_file.write(transformed_content)
        print(f"Data saved in file '{new_filename}'.")
    except OSError as e:
        print(f"Error opening file '{new_filename}': {e}")
        print("Data not saved.")
    finally:
        if out_file is not None:
            out_file.close()


if __name__ == "__main__":
    main()
