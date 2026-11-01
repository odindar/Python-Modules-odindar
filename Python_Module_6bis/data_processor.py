from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class: the common interface of every processor."""

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._total_processed: int = 0

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

    @staticmethod
    def _is_number(value: Any) -> bool:
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


def test_numeric() -> None:
    print("Testing Numeric Processor...")
    proc = NumericProcessor()
    print(f" Trying to validate input '42': {proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {proc.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior "
          "validation:")
    try:
        proc.ingest("foo")
    except ValueError as error:
        print(f" Got exception: {error}")
    data = [1, 2, 3, 4, 5]
    print(f" Processing data: {data}")
    proc.ingest(data)
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = proc.output()
        print(f" Numeric value {rank}: {value}")


def test_text() -> None:
    print("\nTesting Text Processor...")
    proc = TextProcessor()
    print(f" Trying to validate input '42': {proc.validate(42)}")
    data = ["Hello", "Nexus", "World"]
    print(f" Processing data: {data}")
    proc.ingest(data)
    print(" Extracting 1 value...")
    rank, value = proc.output()
    print(f" Text value {rank}: {value}")


def test_log() -> None:
    print("\nTesting Log Processor...")
    proc = LogProcessor()
    print(f" Trying to validate input 'Hello': {proc.validate('Hello')}")
    data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f" Processing data: {data}")
    proc.ingest(data)
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = proc.output()
        print(f" Log entry {rank}: {value}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    test_numeric()
    test_text()
    test_log()
