from __future__ import annotations

import enum
from dataclasses import dataclass


class AccountType(enum.Enum):
    ASSET = "asset"
    EXTERNAL = "external"


@dataclass
class Account:
    account_id: str
    type: AccountType


@dataclass(frozen=True)
class LedgerEntry:
    txn_id: str
    debit_account: str
    credit_account: str
    amount_cents: int


@dataclass
class Hold:
    hold_id: str
    account_id: str
    amount_cents: int
    active: bool = True
