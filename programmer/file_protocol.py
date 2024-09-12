from typing import Protocol


class FileSystem(Protocol):
    def write_file(self, path: str, content: str) -> None: ...
    def read_file(self, path: str) -> str: ...