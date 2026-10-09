from __future__ import annotations

from checksum import check_digit

PREFIX = "ORD"


def format_code(seq: int) -> str:
    body = str(seq)
    return f"{PREFIX}-{body}-{check_digit(body)}"


def is_valid(code: str) -> bool:
    return code.startswith(PREFIX + "-")
