from __future__ import annotations

from typing import Dict

from .accounts import AccountStore
from .holds import HoldBook
from .ledger import Ledger
from .models import AccountType
from .transfers import TransferService

EXTERNAL = "external"


class PaymentsService:
    def __init__(self) -> None:
        self.accounts = AccountStore()
        self.ledger = Ledger()
        self.holds = HoldBook()
        self.transfers = TransferService(self.accounts, self.ledger, self.holds)
        self.accounts.open(EXTERNAL, AccountType.EXTERNAL)

    def open_account(self, account_id: str):
        return self.accounts.open(account_id)

    def deposit(self, account_id: str, amount_cents: int) -> None:
        self.accounts.require(account_id)
        self.ledger.post(f"deposit:{account_id}:{amount_cents}", account_id, EXTERNAL, amount_cents)

    def place_hold(self, hold_id: str, account_id: str, amount_cents: int) -> None:
        self.accounts.require(account_id)
        self.holds.place(hold_id, account_id, amount_cents)

    def release_hold(self, hold_id: str) -> None:
        self.holds.release(hold_id)

    def transfer(self, transfer_id: str, src: str, dst: str, amount_cents: int) -> None:
        self.transfers.transfer(transfer_id, src, dst, amount_cents)

    def balance(self, account_id: str) -> int:
        return self.ledger.balance(account_id)

    def available(self, account_id: str) -> int:
        return self.transfers.available(account_id)

    def balances(self) -> Dict[str, int]:
        return self.ledger.balances()
