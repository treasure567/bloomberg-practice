from __future__ import annotations

from .models import Callback
from .router import Router
from .subscriptions import SubscriptionRegistry
from .topics import TopicMatcher


class MessageBus:
    def __init__(self) -> None:
        self.registry = SubscriptionRegistry()
        self.router = Router(self.registry, TopicMatcher())

    def subscribe(self, pattern: str, callback: Callback) -> int:
        return self.registry.add(pattern, callback)

    def unsubscribe(self, token: int) -> None:
        self.registry.remove(token)

    def publish(self, topic: str, message: object) -> None:
        self.router.publish(topic, message)
