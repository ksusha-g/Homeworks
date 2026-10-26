from typing import Literal
from dataclasses import dataclass
from datetime import datetime, timezone
import uuid

task_status = Literal['todo', 'in_progress', 'done']

@dataclass(frozen=True)
class Task():
    id: str
    title: str
    status: task_status
    created_at: datetime
    tags: tuple[str, ...] = ()
    priority: int=3


    def __post_init__(self) -> None:
        #check id
        if not isinstance(self.id, str):
            raise ValueError('id must be a string')

        try:
            test_id = uuid.UUID(self.id)
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
        if not isinstance(self.status, str):
            raise ValueError('status must be a string')
        
        if self.status not in ('todo', 'in_progress', 'done'):
            raise ValueError('invalid task status')

        #check created_at
        if not isinstance(self.created_at, datetime):
            raise ValueError('created_at must be a datetime')

        if self.created_at.tzinfo != timezone.utc:
            raise ValueError('created_at must be uts')

        #check tags
        if not isinstance(self.tags, tuple):
            raise ValueError('tags must be a tuple')

        #check priority
        if type(self.priority) is not int:
            raise ValueError('priority should be a number')

        if not 1 <= self.priority <= 5: 
            raise ValueError('priority should be 1-5') 
