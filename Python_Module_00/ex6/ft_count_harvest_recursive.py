def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def helper(current_day: int, target_day: int) -> None:
        if current_day > target_day:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        helper(current_day + 1, target_day)

    helper(1, days)
