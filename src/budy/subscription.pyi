from typing import Any, Dict

from .base import Base

class Subscription(Base):
    pass

class SubscriptionAPI:
    def create_subscription(self, payload: Dict[str, Any]) -> Any: ...
