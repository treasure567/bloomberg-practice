from __future__ import annotations

import sqlite3
from typing import List, Optional

from .models import BusinessTier, CalendarEvent, MeetingRequest, RequestStatus


class CalendarDatabase:
    def __init__(self, path: str = ":memory:") -> None:
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row
        self.ensure_schema()

    def ensure_schema(self) -> None:
        self.connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS requests (
                request_id TEXT PRIMARY KEY,
                requester_key TEXT NOT NULL,
                employee_id TEXT NOT NULL,
                subject TEXT NOT NULL,
                start INTEGER NOT NULL,
                end INTEGER NOT NULL,
                business_tier INTEGER NOT NULL,
                submitted_at INTEGER NOT NULL,
                idempotency_key TEXT NOT NULL,
                status TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS events (
                event_id TEXT PRIMARY KEY,
                subject TEXT NOT NULL,
                start INTEGER NOT NULL,
                end INTEGER NOT NULL,
                protected INTEGER NOT NULL
            );
            """
        )

    def insert_request(self, r: MeetingRequest) -> None:
        self.connection.execute(
            "INSERT INTO requests VALUES (?,?,?,?,?,?,?,?,?,?)",
            (r.request_id, r.requester_key, r.employee_id, r.subject, r.start, r.end,
             int(r.business_tier), r.submitted_at, r.idempotency_key, r.status.value),
        )
        self.connection.commit()

    def find_by_idempotency_key(self, requester_key: str, idempotency_key: str) -> Optional[MeetingRequest]:
        row = self.connection.execute(
            "SELECT * FROM requests WHERE requester_key=? AND idempotency_key=?",
            (requester_key, idempotency_key),
        ).fetchone()
        return self._row_to_request(row) if row else None

    def count_requests(self) -> int:
        return self.connection.execute("SELECT COUNT(*) AS c FROM requests").fetchone()["c"]

    def list_pending(self) -> List[MeetingRequest]:
        rows = self.connection.execute(
            "SELECT * FROM requests WHERE status=?", (RequestStatus.PENDING.value,)
        ).fetchall()
        return [self._row_to_request(r) for r in rows]

    def update_status(self, request_id: str, status: RequestStatus) -> None:
        self.connection.execute(
            "UPDATE requests SET status=? WHERE request_id=?", (status.value, request_id)
        )
        self.connection.commit()

    def insert_event(self, e: CalendarEvent) -> None:
        self.connection.execute(
            "INSERT INTO events VALUES (?,?,?,?,?)",
            (e.event_id, e.subject, e.start, e.end, int(e.protected)),
        )
        self.connection.commit()

    def list_events(self) -> List[CalendarEvent]:
        rows = self.connection.execute("SELECT * FROM events").fetchall()
        return [CalendarEvent(r["event_id"], r["subject"], r["start"], r["end"], bool(r["protected"]))
                for r in rows]

    @staticmethod
    def _row_to_request(row: sqlite3.Row) -> MeetingRequest:
        return MeetingRequest(
            request_id=row["request_id"],
            requester_key=row["requester_key"],
            employee_id=row["employee_id"],
            subject=row["subject"],
            start=row["start"],
            end=row["end"],
            business_tier=BusinessTier(row["business_tier"]),
            submitted_at=row["submitted_at"],
            idempotency_key=row["idempotency_key"],
            status=RequestStatus(row["status"]),
        )
