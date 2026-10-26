from typing import Protocol
from .models import Task
from .filters import TaskFilter

class TaskRepository(Protocol):

    def save(self, task: Task) -> None:
        ...


    def delete(self, task_id: str) -> None:
        ...


    def get(self, task_id: str) -> Task:
        ...


    def list_all(self, filter: TaskFilter | None = None) -> list[Task]:
        ...