def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    formatted_seed = seed_type.capitalize()

    if unit == "packets":
        print(f"{formatted_seed} seeds: {quantity} packets available.")
    elif unit == "grams":
        print(f"{formatted_seed} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{formatted_seed} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
