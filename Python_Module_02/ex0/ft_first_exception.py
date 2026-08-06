
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    test_inputs: list[str] = ["25", "abc"]

    for data in test_inputs:
        try:
            temp = input_temperature(data)
            print(f"Input data is '{data}'")
            print(f"Temperature is now {temp}°C\n")
        except Exception as e:
            print(f"Input data is '{data}'")
            print(f"Caught input_temperature error: {e}\n")

    print("All tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()
