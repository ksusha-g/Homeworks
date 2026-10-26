from ..models import Task
from ..filters import TaskFilter
from ..exceptions import DuplicateTaskId, TaskNotFound


class inMemoryRepository():

     
    def __init__(self) -> None:
        self.tasks: dict[str, Task] = {}


    def save(self, task: Task) -> None:
        if task.id in self.tasks:
            raise DuplicateTaskId(task.id)

        self.tasks[task.id] = task


    def delete(self, task_id: str) -> None:
        if task_id not in self.tasks:
            raise TaskNotFound(task_id)

        del self.tasks[task_id]


    def get(self, task_id: str) -> Task:
        if task_id not in self.tasks:
            raise TaskNotFound(task_id)

        return self.tasks[task_id]


    def list_all(self, filter: TaskFilter | None = None) -> list[Task]:

        filter_tasks = list(self.tasks.values())

        if filter is None:
            return filter_tasks

        result = []

        for task in filter_tasks:

            if filter.status is not None and task.status != filter.status:
                continue

            if filter.tag is not None and filter.tag not in task.tags:
                continue

            if filter.min_priority is not None and task.priority < filter.min_priority:
                continue

            result.append(task)

        return result