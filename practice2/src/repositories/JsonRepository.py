import json
from pathlib import Path
from datetime import datetime

from ..models import Task
from ..filters import TaskFilter
from ..exceptions import DuplicateTaskId, TaskNotFound, StorageError


class JsonFileRepository():

    def __init__(self, file_path: Path) -> None:
        self.file_path = Path(file_path)

    def read_tasks(self) -> list[Task]:
        if not self.file_path.exists():
            return []
        
        with self.file_path.open() as file:
            data = json.load(file)

        tasks = []

        for item in data:
            task = Task(
                id = item['id'],
                title = item['title'],
                status = item['status'],
                created_at = datetime.fromisoformat(item['created_at']),
                tags = tuple(item['tags']),
                priority = item['priority'],
            )
            tasks.append(task)

        return tasks


    def write_tasks(self, tasks: list[Task]) -> None:
        data = []

        for task in tasks:
            item = {
                "id": task.id,
                "title": task.title,
                "status": task.status,
                "created_at": task.created_at.isoformat(),
                "tags": task.tags,
                "priority": task.priority,
            }
            data.append(item)

        with self.file_path.open('w') as file:
            json.dump(data, file)


    def save(self, task: Task) -> None:
        tasks = self.read_tasks()

        for item in tasks:
            if item.id == task.id:
                raise DuplicateTaskId(task.id)

        tasks.append(task)
        self.write_tasks(tasks)


    def delete(self, task_id: str) -> None:
        tasks = self.read_tasks()

        for task in tasks:
            if task.id == task_id:
                tasks.remove(task)
                self.write_tasks(tasks)
                return
        raise TaskNotFound(task_id)

    def get(self, task_id: str) -> Task:
        tasks = self.read_tasks()

        for task in tasks:
            if task.id == task_id:
                return task
        raise TaskNotFound(task_id)


    def list_all(self, filter: TaskFilter | None = None) -> list[Task]:
        tasks = self.read_tasks()

        if filter is None:
            return tasks

        result = []

        for task in tasks:
            if filter.status is not None and task.status != filter.status:
                continue

            if filter.tag is not None and filter.tag not in task.tags:
                continue

            if filter.min_priority is not None and task.priority < filter.min_priority:
                continue

            result.append(task)

        return result