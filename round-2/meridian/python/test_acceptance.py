import sqlite3

import pytest

from blike_calendar.database import CalendarDatabase
from blike_calendar.models import BusinessTier, CalendarEvent, MeetingRequest, RequestStatus
from blike_calendar.scheduler import schedule_batch
from blike_calendar.service import SchedulingService


def req(rid, start, end, tier=BusinessTier.STANDARD, submitted_at=0, requester="u1", idem=None):
    return MeetingRequest(rid, requester, "e1", "s", start, end, tier, submitted_at,
                          idem or rid, RequestStatus.PENDING)


def test_db_enforces_idempotency_uniqueness():
    db = CalendarDatabase()
    db.insert_request(req("r1", 600, 660, requester="u1", idem="K"))
    with pytest.raises(sqlite3.IntegrityError):
        db.insert_request(req("r2", 600, 660, requester="u1", idem="K"))


def test_scheduler_respects_protected_events():
    events = [CalendarEvent("ev1", "1:1", 600, 660, protected=True)]
    assert schedule_batch([req("a", 600, 660)], events) == []


def test_scorer_prioritises_business_tier():
    execu = req("exec", 600, 660, tier=BusinessTier.EXECUTIVE, submitted_at=1)
    std = req("std", 600, 660, tier=BusinessTier.STANDARD, submitted_at=5)
    assert [r.request_id for r in schedule_batch([std, execu], [])] == ["exec"]


def test_rejected_request_cannot_be_accepted():
    svc = SchedulingService(CalendarDatabase())
    r = svc.submit_request(requester_key="u1", employee_id="e1", subject="s", start=600, end=660,
                           business_tier=BusinessTier.STANDARD, idempotency_key="K", submitted_at=1)
    svc.reject(r.request_id)
    with pytest.raises(ValueError):
        svc.accept(r.request_id)
