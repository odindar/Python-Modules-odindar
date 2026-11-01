from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class: the common interface of every processor."""

    name: str = "Data Processor"

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._total_processed: int = 0

    @property
    def total_processed(self) -> int:
        """How many items this processor has ingested so far."""
        return self._total_processed

    @property
    def remaining(self) -> int:
        """How many items are still waiting to be extracted."""
        return len(self._storage)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Tell whether `data` can be ingested by this processor."""

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process `data` and store it internally."""

    def _store(self, value: str) -> None:
        """Save one piece of data together with its processing rank."""
        self._storage.append((self._total_processed, value))
        self._total_processed += 1

    def output(self) -> tuple[int, str]:
        """Extract (and remove) the oldest stored piece with its rank."""
        if not self._storage:
            raise IndexError("No data available to output")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    """Handles int, float and lists of them (mixed lists included)."""

    name = "Numeric Processor"

    @staticmethod
    def _is_number(value: Any) -> bool:
        # bool is a subclass of int in Python: reject it explicitly.
        return (isinstance(value, (int, float))
                and not isinstance(value, bool))

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(self._is_number(item) for item in data)
        return self._is_number(data)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items: list[int | float] = (
            data if isinstance(data, list) else [data]
        )
        for item in items:
            self._store(str(item))


class TextProcessor(DataProcessor):
    """Handles str and lists of str."""

    name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items: list[str] = data if isinstance(data, list) else [data]
        for item in items:
            self._store(item)


class LogProcessor(DataProcessor):
    """Handles dict[str, str] and lists of such dicts."""

    name = "Log Processor"

    @staticmethod
    def _is_log(entry: Any) -> bool:
        return isinstance(entry, dict) and all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in entry.items()
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(self._is_log(entry) for entry in data)
        return self._is_log(data)

    @staticmethod
    def _to_string(entry: dict[str, str]) -> str:
        if "log_level" in entry and "log_message" in entry:
            return f"{entry['log_level']}: {entry['log_message']}"
        return ", ".join(f"{key}: {value}" for key, value in entry.items())

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        entries: list[dict[str, str]] = (
            data if isinstance(data, list) else [data]
        )
        for entry in entries:
            self._store(self._to_string(entry))


class DataStream:
    """Routes every element of a stream to a processor able to handle it."""

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def _find_processor(self, element: Any) -> DataProcessor | None:
        for proc in self._processors:
            if proc.validate(element):
                return proc
        return None

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            proc = self._find_processor(element)
            if proc is None:
                print("DataStream error - Can't process element in "
                      f"stream: {element}")
                continue
            try:
                proc.ingest(element)
            except ValueError as error:
                print(f"DataStream error - {error}: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(f"{proc.name}: total {proc.total_processed} items "
                  f"processed, remaining {proc.remaining} on processor")


def consume(proc: DataProcessor, count: int) -> None:
    """Extract `count` elements from a processor and throw them away."""
    for _ in range(count):
        proc.output()


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    numeric = NumericProcessor()
    stream.register_processor(numeric)

    batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"\nSend first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    consume(numeric, 3)
    consume(text, 2)
    consume(log, 1)
    stream.print_processors_stats()
