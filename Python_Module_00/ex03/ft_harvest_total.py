def ft_harvest_total() -> None:
    d1: int = int(input("Day 1 harvest: "))
    d2: int = int(input("Day 2 harvest: "))
    d3: int = int(input("Day 3 harvest: "))

    total: int = d1 + d2 + d3

    print(f"Total harvest: {total}")
