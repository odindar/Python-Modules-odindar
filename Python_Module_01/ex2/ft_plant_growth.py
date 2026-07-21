#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.current_age: int = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.current_age} days old")

    def grow(self, amount: float) -> None:
        self.height = round(self.height + amount, 1)

    def age(self, days: int = 1) -> None:
        self.current_age += days

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    my_rose: Plant = Plant("Rose", 25.0, 30)
    my_rose.show()
    
    start_height: float = my_rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        my_rose.grow(0.8)
        my_rose.age(1)
        my_rose.show()
    
    growth_amount: float = round(my_rose.height - start_height, 1)
    print(f"Growth this week: {growth_amount}cm")