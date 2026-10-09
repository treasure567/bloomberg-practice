from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Callable


@dataclass
class Entry:
    participant: str
    code: str


class CodeIssuer:
    """Issues 5-digit entry codes and scores matches against a winning code."""

    def __init__(self, random_source: Callable[[], float] | None = None) -> None:
        self._rand = random_source if random_source is not None else random.random

    def issue(self, participant: str) -> Entry:
        number = int(self._rand() * 100000)
        return Entry(participant, str(number))

    @staticmethod
    def match_count(code: str, winning: str) -> int:
        return len(set(code) & set(winning))
