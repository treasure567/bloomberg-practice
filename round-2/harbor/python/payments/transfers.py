from __future__ import annotations

from .accounts import AccountStore
from .errors import InsufficientFunds, ValidationError
from .holds import HoldBook
from .ledger import Ledger


class TransferService:
    def __init__(self, accounts: AccountStore, ledger: Ledger, holds: HoldBook) -> None:
        self.accounts = accounts
        self.ledger = ledger
        self.holds = holds
        self._seen: set = set()

    def available(self, account_id: str) -> int:
        return self.ledger.balance(account_id) - self.holds.held(account_id)

    def transfer(self, transfer_id: str, src: str, dst: str, amount_cents: int) -> None:
        if amount_cents <= 0:
            raise ValidationError("amount must be positive")
        self.accounts.require(src)
        self.accounts.require(dst)
        self.ledger.post(transfer_id, dst, src, amount_cents)
