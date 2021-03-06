from abc import ABC, abstractmethod
from typing import List


class BaseSummarizer(ABC):

    def __init__(self, language: str = "english") -> None:
        self._language = language

    @property
    def language(self) -> str:
        return self._language

    @abstractmethod
    def summarize(self, text: str, summary_length: int) -> List[str]:
        pass
