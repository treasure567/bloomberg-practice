from __future__ import annotations

from typing import Dict, List

from .models import LedgerEntry


class Ledger:
    """Append-only double-entry ledger. balance = sum of debits minus sum of credits."""

    def __init__(self) -> None:
        self._entries: List[LedgerEntry] = []
        self._balances: Dict[str, int] = {}

    def post(self, txn_id: str, debit_account: str, credit_account: str, amount_cents: int) -> None:
        self._entries.append(LedgerEntry(txn_id, debit_account, credit_account, amount_cents))
        b = self._balances
        b[debit_account] = b.get(debit_account, 0) + amount_cents
        b[credit_account] = b.get(credit_account, 0) + amount_cents

    def balance(self, account_id: str) -> int:
        return self._balances.get(account_id, 0)

    def balances(self) -> Dict[str, int]:
        return dict(self._balances)
