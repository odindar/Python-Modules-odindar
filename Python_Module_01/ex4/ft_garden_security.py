#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height: float = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age: int = 0
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(
                f"{self._name}: Error, height can't be negative\n"
                "Height update rejected"
            )
        else:
            self._height = round(new_height, 1)

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(
                f"{self._name}: Error, age can't be negative\n"
                "Age update rejected"
            )
        else:
            self._age = new_age

    def grow(self, amount: float) -> None:
        self.set_height(self._height + amount)

    def age(self, days: int = 1) -> None:
        self.set_age(self._age + days)

    def show(self) -> None:
        print(
            f"{self._name.capitalize()}: {self._height:.1f}cm, "
            f"{self._age} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")

    safe_plant: Plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    safe_plant.show()
    print()

    safe_plant.set_height(25.0)
    print(f"Height updated: {safe_plant.get_height():.0f}cm")
    safe_plant.set_age(30)
    print(f"Age updated: {safe_plant.get_age()} days")
    print()

    safe_plant.set_height(-5.0)
    safe_plant.set_age(-10)
    print()

    print("Current state: ", end="")
    safe_plant.show()
