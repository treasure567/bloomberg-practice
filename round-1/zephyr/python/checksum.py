from __future__ import annotations


def check_digit(body: str) -> int:
    return sum(int(c) for c in body) % 10
