import pytest
from datetime import datetime, timezone
from uuid import uuid4
from src.models import Task
from src.repositories.InMemoryRepository import inMemoryRepository
from src.exceptions import DuplicateTaskId, TaskNotFound

def create_task():
    return Task(
        id = str(uuid4()),
        title = 'доделать дз',
        status = 'todo',
        created_at = datetime.now(timezone.utc),
        tags = ('python',)
    )

def test_save_task():
    repository = inMemoryRepository()
    task = create_task()
    repository.save(task)

def test_duplicate_task_id():
    repository = inMemoryRepository()
    task = create_task() 

    repository.save(task)

    with pytest.raises(DuplicateTaskId):
        repository.save(task)

def test_delete_task():
    repository = inMemoryRepository()
    task = create_task()

    repository.save(task)
    repository.delete(task.id) 

    with pytest.raises(TaskNotFound):
        repository.get(task.id)

def test_get_task():
    repository = inMemoryRepository()
    task = create_task() 

    repository.save(task)

    assert repository.get(task.id) == task

def test_get_unknown_task():
    repository = inMemoryRepository()

    with pytest.raises(TaskNotFound):
        repository.get('some_id')

def test_list_all_return_all_tasks():
    repository = inMemoryRepository()
    task_1 = create_task() 
    task_2 = create_task()

    repository.save(task_1)
    repository.save(task_2)

    assert len(repository.list_all()) == 2

