from abc import ABC, abstractmethod
from difflib import SequenceMatcher
from typing import Iterator


class DBBackend(ABC):
    @abstractmethod
    def search_in_db(self, word, lang, fulltext: bool = None) -> Iterator[str] | None:
        """The only mandatory method that provides a database search and that must return a result iterator or None."""

    def search_sorted(self, word, lang, fulltext: bool = None) -> list | str:
        results_with_matchratio = []
        results = self.search_in_db(word, lang, fulltext)
        if not results:
            return "No results found."
        for result in results:
            ratio = SequenceMatcher(None, result[lang], word).ratio()
            results_with_matchratio.append([result, ratio])
        sorted_results_with_ratio = sorted(
            results_with_matchratio, key=lambda x: x[1], reverse=True
        )
        return [
            x for x, _ in sorted_results_with_ratio
        ]  # return list of results without ratio
