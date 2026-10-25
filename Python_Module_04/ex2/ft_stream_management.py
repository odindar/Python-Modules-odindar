import sys
from typing import IO


def get_input(prompt: str) -> str:
    sys.stdout.write(prompt)
    sys.stdout.flush()
    user_input: str = sys.stdin.readline()
    return user_input.strip("\n")


def main() -> None:
    args: list[str] = sys.argv[1:]
    if len(args) != 1:
        sys.stdout.write(f"Usage: {sys.argv[0]} <file>\n")
        return

    filename: str = args[0]
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{filename}'\n")

    file_obj: IO[str] | None = None
    content: str = ""
    try:
        file_obj = open(filename, 'r', encoding='utf-8')
        content = file_obj.read()
        sys.stdout.write(content)
        if content and not content.endswith('\n'):
            sys.stdout.write("\n")
        sys.stdout.write(f"File '{filename}' closed.\n")
    except OSError as e:
        err_msg: str = f"[STDERR] Error opening file '{filename}': {e}\n"
        sys.stderr.write(err_msg)
        if file_obj is not None:
            file_obj.close()
        return

    if file_obj is not None:
        file_obj.close()

    sys.stdout.write("Transform data:\n")
    lines: list[str] = content.splitlines()
    transformed_lines: list[str] = [f"{line}#" for line in lines]
    transformed_content: str = "\n".join(transformed_lines) + "\n"
    sys.stdout.write(transformed_content)

    new_filename: str = get_input("Enter new file name (or empty):\n")
    if not new_filename.strip():
        sys.stdout.write("Not saving data.\n")
        return

    sys.stdout.write(f"Saving data to '{new_filename}'\n")
    out_file: IO[str] | None = None
    try:
        out_file = open(new_filename, 'w', encoding='utf-8')
        out_file.write(transformed_content)
        sys.stdout.write(f"Data saved in file '{new_filename}'.\n")
    except OSError as e:
        err_msg = f"[STDERR] Error opening file '{new_filename}': {e}\n"
        sys.stderr.write(err_msg)
        sys.stdout.write("Data not saved.\n")
    finally:
        if out_file is not None:
            out_file.close()


if __name__ == "__main__":
    main()
