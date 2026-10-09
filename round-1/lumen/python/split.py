from __future__ import annotations

from typing import List

from remainder import distribute


def split_amount(total_cents: int, n: int) -> List[int]:
    base = int(total_cents / n)
    rem = total_cents - base * n
    return distribute(base, rem, n)
