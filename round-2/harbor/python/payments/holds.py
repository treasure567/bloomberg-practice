from __future__ import annotations

from typing import Dict

from .models import Hold


class HoldBook:
    """Funds reserved against an account but not yet moved."""

    def __init__(self) -> None:
        self._holds: Dict[str, Hold] = {}

    def place(self, hold_id: str, account_id: str, amount_cents: int) -> None:
        self._holds[hold_id] = Hold(hold_id, account_id, amount_cents, active=True)

    def release(self, hold_id: str) -> None:
        pass

    def held(self, account_id: str) -> int:
        return sum(h.amount_cents for h in self._holds.values()
                   if h.active and h.account_id == account_id)
