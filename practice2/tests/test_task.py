import pytest
from datetime import datetime, timezone
from uuid import uuid4
from src.models import Task

def create_task():
    return Task(
        id = str(uuid4()),
        title = 'доделать дз',
        status = 'todo',
        created_at = datetime.now(timezone.utc),
        tags = ('python',)
    )

def test_create_valid_task():
    task = create_task()

    assert task.title == 'доделать дз'
    assert task.status == 'todo'
    assert task.priority == 3

def test_valid_uuid():
    with pytest.raises(ValueError):
        Task(
                id="not-a-uuid",
                title="Изучить Python",
                status="todo",
                created_at=datetime.now(timezone.utc),
                tags=(),
            )

def test_invalid_priority():
    with pytest.raises(ValueError):
        Task(
            id="uuid",
            title="Изучить Python",
            status="todo",
            created_at=datetime.now(timezone.utc),
            tags=(),
            priority = 7
        )




    