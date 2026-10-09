from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

Callback = Callable[[object], None]


@dataclass
class Subscription:
    token: int
    pattern: str
    callback: Callback
