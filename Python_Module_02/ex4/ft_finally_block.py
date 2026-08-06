
class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message: str = message
        super().__init__(self.message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    try:
        print("Opening watering system")
        plants0: list[str] = ["Tomato", "Lettuce", "Carrots"]
        for plant in plants0:
            water_plant(plant)
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    try:
        print("Opening watering system")
        plants1: list[str] = ["Tomato", "lettuce", "Carrots"]
        for plant in plants1:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
