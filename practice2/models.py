from typing import Protocol
from typing import Literal
from dataclasses import dataclass
import datetime
import uuid
from exceptions import DuplicateTaskId, StorageError, TaskNotFound
import json
from pathlib import Path

task_status = Literal['todo', 'in_progress', 'done']

@dataclass(frozen=True)
class Task():
    id: str
    title: str
    status: task_status
    created_at: datetime
    tags:list[str]
    priority: int=3

    def __post_init__(self):
        #check id
        if not isinstance(self.id, str):
            raise ValueError('id must be a string')

        try:
            test_id = uuid(self.id)
        except ValueError as e:
            raise ValueError('id must be a valid uuid') from e

        if test_id.version != 4:
            raise ValueError('if must be uuid4')
        
        #check title
        if not isinstance(self.title, str):
            raise ValueError('title must be a string')

        if not 1 <= len(self.title) <= 200:
            raise ValueError('title must contain 1-200 characters')

        #check status
        if isinstance(self.status, str):
            raise ValueError('status must be a string')
        
        if self.status not in task_status:
            raise ValueError('invalid task status')

        #check created at
        if not isinstance(self.created_at, datetime):
            raise ValueError('created_at must be a datetime')

        #check tags
        if not isinstance(self.tags, list):
            raise ValueError('tags must be a list')

        #check priority
        if not isinstance(self.priority, int):
            raise ValueError('priority should be a number')

        if 1 <= self.priority <= 5: 
            raise ValueError('priority should be 1-5') 


class Kernel(Protocol):

    def save(self, task):
        ...

    def delete(self, task_id):
        ...

    def get(self, task_id):
        ...

    def list_all(self, filter):
        ...


@dataclass(frozen=True)
class TaskFilter:
    status: task_status
    tag: str
    min_priority: int

class inMemoryRepository():
     
    def __init__(self):
        self.tasks = {}

    def save(self, task):
        if task.id in self.tasks:
            raise DuplicateTaskId(task.id)

        self.tasks[task.id] = task

    def delete(self, task_id):
        if task_id not in self.tasks:
            raise TaskNotFound(task_id)

        del self.tasks[task_id]

    def get(self, task_id):
        if task_id not in self.tasks:
            raise TaskNotFound(task_id)

        return self.tasks[task_id]

    def list_all(self, filter: TaskFilter):

        filter_tasks = list(self.tasks.values())

        if filter == None:
            return filter_tasks

        result = []

        for task in filter_tasks:

            if filter.status != None and task.status != filter.status:
                continue

            if filter.tag != None and filter.tag not in task.tags:
                continue

            if filter.min_priority != None and task.priority < filter.min_priority:
                continue

            result.append(task)

        return result


class JsonFileRepository():

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def save(self, task):
        pass

    def delete(self, task_id):
        pass

    def get(self, task_id):
        pass

    def list_all(self, filter):
        pass
