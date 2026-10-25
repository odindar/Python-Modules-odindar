def secure_archive(
    filename: str,
    action: str = 'read',
    content: str = ""
) -> tuple[bool, str]:
    if action == 'read':
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                file_content: str = f.read()
                return (True, file_content)
        except OSError as e:
            return (False, str(e))
    elif action == 'write':
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
                return (True, 'Content successfully written to file')
        except OSError as e:
            return (False, str(e))

    return (False, "Invalid action specified.")


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    res_no_exist: tuple[bool, str] = secure_archive(
        '/not/existing/file', 'read'
    )
    print(res_no_exist)

    print("Using 'secure_archive' to read from an inaccessible file:")
    res_no_perm: tuple[bool, str] = secure_archive(
        '/etc/master.passwd', 'read'
    )
    print(res_no_perm)

    print("Using 'secure_archive' to write content to a new file:")
    test_content: str = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
    )
    res_write: tuple[bool, str] = secure_archive(
        'test_archive.txt', 'write', test_content
    )
    print(res_write)

    print("Using 'secure_archive' to read from a regular file:")
    res_read: tuple[bool, str] = secure_archive('test_archive.txt', 'read')
    print(res_read)


if __name__ == "__main__":
    main()
