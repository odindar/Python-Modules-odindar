#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose: Plant = Plant("rose", 25.0, 30)
    sunflower: Plant = Plant("sunflower", 80.0, 45)
    cactus: Plant = Plant("cactus", 15.0, 120)

    rose.show()
    sunflower.show()
    cactus.show()