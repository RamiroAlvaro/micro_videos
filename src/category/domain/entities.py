import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from src.__seedwork.domain.value_objects import UniqueEntityId


@dataclass(kw_only=True, frozen=True)
class Category:
    id: UniqueEntityId = field(default_factory=lambda: UniqueEntityId(id=str(uuid.uuid4())))
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(default_factory=lambda: datetime.now())
