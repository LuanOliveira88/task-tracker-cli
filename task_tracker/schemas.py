from dataclasses import asdict, dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class TaskStatus(Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in-progress'
    DONE = 'done'


@dataclass
class UserTask:
    description: str
    status: TaskStatus
    created_at: datetime
    updated_at: Optional[datetime] = field(default=None)

    def copy(self) -> 'UserTask':
        return UserTask(
            description=self.description,
            status=self.status,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def as_dict(self):
        return asdict(self)
