import random
from typing import Generator


PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run", "eat", "sleep", "grab", "move",
    "climb", "swim", "use", "release"
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    event_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while event_list:
        idx: int = random.randrange(len(event_list))
        yield event_list.pop(idx)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_stream: Generator[tuple[str, str], None, None] = gen_event()

    for i in range(1000):
        event: tuple[str, str] = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        ten_events.append(next(event_stream))

    print(f"Built list of 10 events: {ten_events}")

    for ev in consume_event(ten_events):
        print(f"Got event from list: {ev}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
