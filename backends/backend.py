from abc import ABC, abstractmethod
from typing import Iterator


class DBBackend(ABC):
    @abstractmethod
    def search_in_db(self, word, lang) -> Iterator[str] | None:
        """The only mandatory method that provides a database search and that must return a result iterator or None."""
