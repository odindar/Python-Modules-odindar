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


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name.capitalize()} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self, amount: float) -> None:
        super().grow(amount)
        self.nutritional_value += 1

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato: Vegetable = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(10):
        tomato.grow(4.2)
        tomato.age(2)
    tomato.show()
