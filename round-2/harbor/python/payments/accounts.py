from __future__ import annotations

from typing import Dict

from .errors import UnknownAccount
from .models import Account, AccountType


class AccountStore:
    def __init__(self) -> None:
        self._accounts: Dict[str, Account] = {}

    def open(self, account_id: str, type: AccountType = AccountType.ASSET) -> Account:
        if account_id in self._accounts:
            return self._accounts[account_id]
        account = Account(account_id, type)
        self._accounts[account_id] = account
        return account

    def exists(self, account_id: str) -> bool:
        return account_id in self._accounts

    def require(self, account_id: str) -> None:
        if account_id not in self._accounts:
            raise UnknownAccount(account_id)
