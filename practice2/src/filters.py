from dataclasses import dataclass
from .models import task_status

@dataclass(frozen=True)
class TaskFilter:
    status: task_status | None = None
    tag: str | None = None
    min_priority: int | None = None
    