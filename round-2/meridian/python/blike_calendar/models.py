from __future__ import annotations

import enum
from dataclasses import dataclass


class BusinessTier(enum.IntEnum):
    STANDARD = 1
    PRIORITY = 2
    EXECUTIVE = 3


class RequestStatus(str, enum.Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"


@dataclass
class MeetingRequest:
    request_id: str
    requester_key: str
    employee_id: str
    subject: str
    start: int            # minutes since midnight (kept as int for simplicity)
    end: int
    business_tier: BusinessTier
    submitted_at: int     # monotonic submission counter; lower = earlier
    idempotency_key: str
    status: RequestStatus = RequestStatus.PENDING


@dataclass
class CalendarEvent:
    event_id: str
    subject: str
    start: int
    end: int
    protected: bool
