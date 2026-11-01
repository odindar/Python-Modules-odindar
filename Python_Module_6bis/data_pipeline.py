from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    """Anything that has a matching `process_output` is an export plugin."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    """Export plugin: one CSV line containing every value."""

    @staticmethod
    def _escape(value: str) -> str:
        # RFC 4180: quote a field containing a comma, a quote or a
        # line break, and double any quote inside it.
        if any(char in value for char in (",", '"', "\n", "\r")):
            return '"' + value.replace('"', '""') + '"'
        return value

    def process_output(self, data: list[tuple[int, str]]) -> None:
        line = ",".join(self._escape(value) for _, value in data)
        print("CSV Output:")
        print(line)


class JSONExportPlugin:
    """Export plugin: one JSON object {"item_<rank>": "<value>", ...}."""

    @staticmethod
    def _escape(value: str) -> str:
        return (value.replace("\\", "\\\\")
                     .replace('"', '\\"')
                     .replace("\n", "\\n")
                     .replace("\r", "\\r")
                     .replace("\t", "\\t"))

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs = ", ".join(
            f'"item_{rank}": "{self._escape(value)}"'
            for rank, value in data
        )
        print("JSON Output:")
        print("{" + pairs + "}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Consume up to `nb` items per processor and export them."""
        for proc in self._processors:
            batch: list[tuple[int, str]] = []
            for _ in range(min(nb, proc.remaining)):
                batch.append(proc.output())
            if batch:
                plugin.process_output(batch)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch_one: list[Any] = [
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
    print(f"\nSend first batch of data on stream: {batch_one}\n")
    stream.process_stream(batch_one)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    print()
    stream.print_processors_stats()

    batch_two: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"\nSend another batch of data: {batch_two}\n")
    stream.process_stream(batch_two)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    print()
    stream.print_processors_stats()
