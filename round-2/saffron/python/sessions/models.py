from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Session:
    sid: str
    expiry: int
    data: dict = field(default_factory=dict)
