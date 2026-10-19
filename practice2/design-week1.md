## Перечень методов хранилища
|Метод   |Возвращает|Поведение|
|--------|----------|---------|
|save    |None      |Сохраняет задачу|
|get     |Task()    |Возвращает задачу или TaskNotFound|
|delete  |None      |Удаляет задачу или TaskNotFound|
|list_all|list[Task]|Возвращет все задачи, подходящие под фильтр|

## Инварианты Task()
- id: str, UUID4
- title: str, 1–200 символов
- status: todo / in_progress / done
- created_at: datetime, UTC, timezone-aware
- tags: list[str]
- priority: int, 1–5

## Идемпотентные операции
Повторение ID: выдаем ошибку DuplicateTaskId
Неверное название task: TaskNotFound
Проблемы с подклечением к базе данных: StorageError

## filter=None
list_all(filter=None) возвращает все задачи