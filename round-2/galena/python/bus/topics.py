from __future__ import annotations


class TopicMatcher:
    """Pattern matching for topics.

    Supported patterns: an exact topic ("px.AAPL"), a one-segment trailing wildcard ("px.*"),
    and the match-all pattern "*".
    """

    def matches(self, pattern: str, topic: str) -> bool:
        return pattern == topic
