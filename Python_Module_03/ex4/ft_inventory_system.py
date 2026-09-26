import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    args: list[str] = sys.argv[1:]
    inventory: dict[str, int] = {}

    for arg in args:
        if ":" not in arg:
            print(f"Error invalid parameter '{arg}'")
            continue

        parts: list[str] = arg.split(":", 1)
        item: str = parts[0]
        qty_str: str = parts[1]

        if item in inventory:
            print(f"Redundant item '{item}' discarding")
            continue

        try:
            qty: int = int(qty_str)
            inventory[item] = qty
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")

    print(f"Got inventory: {inventory}")

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty: int = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total_qty}")

    if total_qty > 0:
        for item, qty in inventory.items():
            pct: float = (qty / total_qty) * 100
            print(f"Item {item} represents {round(pct, 1)}%")

    if inventory:
        most_abundant: str = ""
        least_abundant: str = ""
        for k, v in inventory.items():
            if not most_abundant or v > inventory[most_abundant]:
                most_abundant = k
            if not least_abundant or v < inventory[least_abundant]:
                least_abundant = k

        print(
            f"Item most abundant: {most_abundant} "
            f"with quantity {inventory[most_abundant]}"
        )
        print(
            f"Item least abundant: {least_abundant} "
            f"with quantity {inventory[least_abundant]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
