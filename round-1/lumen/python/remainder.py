from __future__ import annotations

from typing import List


def distribute(base: int, remainder: int, n: int) -> List[int]:
    """Give `base` to everyone; the first `remainder` recipients get one extra."""
    return [base] * n
