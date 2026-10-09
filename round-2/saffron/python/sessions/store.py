from __future__ import annotations

from typing import Dict, Iterator, Optional

from .models import Session


class SessionStore:
    def __init__(self) -> None:
        self._sessions: Dict[str, Session] = {}

    def put(self, session: Session) -> None:
        self._sessions[session.sid] = session

    def get(self, sid: str) -> Optional[Session]:
        return self._sessions.get(sid)

    def delete(self, sid: str) -> None:
        self._sessions.pop(sid, None)

    def all(self) -> Iterator[Session]:
        return list(self._sessions.values())

    def size(self) -> int:
        return len(self._sessions)
