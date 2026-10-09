from __future__ import annotations

from .models import Session


class ExpiryPolicy:
    """A session is expired once the clock reaches its expiry tick (now >= expiry)."""

    def is_expired(self, session: Session, now: int) -> bool:
        return now > session.expiry
