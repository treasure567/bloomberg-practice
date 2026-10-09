from __future__ import annotations

from .models import MeetingRequest


def score_request(request: MeetingRequest):
    """Rank key for a request. Larger sorts earlier (scheduled first).

    Intended policy (see spec in README): higher business tier is scheduled first; ties are
    broken in favour of the earlier submission.
    """
    return (request.submitted_at,)
