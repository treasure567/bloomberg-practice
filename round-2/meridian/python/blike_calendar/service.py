from __future__ import annotations

import itertools

from .database import CalendarDatabase
from .models import BusinessTier, MeetingRequest, RequestStatus

_ids = itertools.count(1)


class SchedulingService:
    def __init__(self, db: CalendarDatabase) -> None:
        self.db = db

    def submit_request(self, *, requester_key: str, employee_id: str, subject: str,
                       start: int, end: int, business_tier: BusinessTier,
                       idempotency_key: str, submitted_at: int) -> MeetingRequest:
        existing = self.db.find_by_idempotency_key(requester_key, idempotency_key)
        if existing is not None:
            return existing
        request = MeetingRequest(
            request_id=f"req-{next(_ids)}",
            requester_key=requester_key,
            employee_id=employee_id,
            subject=subject,
            start=start,
            end=end,
            business_tier=business_tier,
            submitted_at=submitted_at,
            idempotency_key=idempotency_key,
            status=RequestStatus.PENDING,
        )
        self.db.insert_request(request)
        return request

    def reject(self, request_id: str) -> None:
        self.db.update_status(request_id, RequestStatus.REJECTED)

    def accept(self, request_id: str) -> None:
        self.db.update_status(request_id, RequestStatus.ACCEPTED)
