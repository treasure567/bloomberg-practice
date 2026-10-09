from __future__ import annotations

from .subscriptions import SubscriptionRegistry
from .topics import TopicMatcher


class Router:
    def __init__(self, registry: SubscriptionRegistry, matcher: TopicMatcher) -> None:
        self.registry = registry
        self.matcher = matcher

    def publish(self, topic: str, message: object) -> None:
        for sub in self.registry.all():
            if self.matcher.matches(sub.pattern, topic):
                sub.callback(message)
