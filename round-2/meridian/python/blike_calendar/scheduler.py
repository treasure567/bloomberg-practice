from __future__ import annotations

from typing import List

from .models import CalendarEvent, MeetingRequest
from .scorer import score_request


def _overlaps(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    # Half-open intervals: [start, end). Back-to-back meetings do not conflict.
    return a_start < b_end and b_start < a_end


def schedule_batch(requests: List[MeetingRequest], events: List[CalendarEvent]) -> List[MeetingRequest]:
    """Greedily schedule pending requests around existing commitments.

    Requests are considered in priority order. A request is accepted only if it does not overlap
    an already-accepted request or a protected calendar event.
    """
    ordered = sorted(requests, key=score_request, reverse=True)
    booked: List[tuple] = []
    scheduled: List[MeetingRequest] = []
    for r in ordered:
        conflict = any(_overlaps(r.start, r.end, s, e) for (s, e) in booked)
        if conflict:
            continue
        booked.append((r.start, r.end))
        scheduled.append(r)
    return scheduled
