from __future__ import annotations

from typing import Optional

from .expiry import ExpiryPolicy
from .models import Session
from .store import SessionStore


class SessionService:
    def __init__(self) -> None:
        self.store = SessionStore()
        self.expiry = ExpiryPolicy()

    def create(self, sid: str, now: int, ttl: int) -> None:
        self.store.put(Session(sid, expiry=now + ttl))

    def get(self, sid: str, now: int) -> Optional[dict]:
        session = self.store.get(sid)
        if session is None:
            return None
        if self.expiry.is_expired(session, now):
            return None
        return session.data

    def touch(self, sid: str, now: int, ttl: int) -> None:
        pass

    def cleanup(self, now: int) -> None:
        pass

    def size(self) -> int:
        return self.store.size()
