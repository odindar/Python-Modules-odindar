#!/usr/bin/env python3


class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def count_grow(self) -> None:
            self._grow_calls += 1

        def count_age(self) -> None:
            self._age_calls += 1

        def count_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

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

        self._stats: Plant._Stats = self._Stats()

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_stats(self) -> "Plant._Stats":
        return self._stats

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
        self._stats.count_grow()
        self.set_height(self._height + amount)

    def age(self, days: int = 1) -> None:
        self._stats.count_age()
        self.set_age(self._age + days)

    def show(self) -> None:
        self._stats.count_show()
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
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def count_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    _stats: "Tree._Stats"

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        self._stats.count_shade()
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


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name().capitalize()}]")
    plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    for days in [30, 400]:
        result: bool = Plant.is_older_than_a_year(days)
        print(f"Is {days} days more than a year? -> {result}")

    print("\n=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("\n=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("\n=== Seed")
    sunflower: Seed = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("\n=== Anonymous")
    anonymous: Plant = Plant.create_anonymous()
    anonymous.show()
    display_plant_stats(anonymous)
