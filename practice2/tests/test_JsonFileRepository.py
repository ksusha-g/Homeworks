import pytest
from datetime import datetime, timezone
from uuid import uuid4
from src.models import Task
from src.repositories.JsonRepository import JsonFileRepository
from src.exceptions import DuplicateTaskId, TaskNotFound

def create_task():
    return Task(
        id = str(uuid4()),
        title = 'доделать дз',
        status = 'todo',
        created_at = datetime.now(timezone.utc),
        tags = ('python',)
    )


def test_save_task(tmp_path):
    repository = JsonFileRepository(tmp_path / 'tasks.json')
    task = create_task()

    repository.save(task)

def test_get_task(tmp_path):
    repository = JsonFileRepository(tmp_path / 'tasks.json')
    task = create_task()
    
    repository.save(task)

    assert repository.get(task.id) == task

def test_duplicate_task_id(tmp_path):
    repository = JsonFileRepository(tmp_path / 'tasks.json')
    task = create_task()
    
    repository.save(task)

    with pytest.raises(DuplicateTaskId):
        repository.save(task)

def test_delete_task(tmp_path):
    repository = JsonFileRepository(tmp_path / 'tasks.json')
    task = create_task()
    
    repository.save(task)
    repository.delete(task.id)

    with pytest.raises(TaskNotFound):
        repository.get(task.id)

def test_list_all(tmp_path):
    repository = JsonFileRepository(tmp_path / 'tasks.json')
    task1 = create_task()
    task2 = create_task()
    
    repository.save(task1)
    repository.save(task2)

    assert len(repository.list_all()) == 2