# Камень-ножницы-бумага
## Описание
Текстовая игра "Камень, ножницы, бумага", переписанная с процедурного кода на ООП.

## Установка
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск
```bash
python main.py
```

## Тесты
```bash
pytest -v
```

## Архитектура
- `Game()` - управление правилами и ходом игры
- `Player()` - хранение данных игрока и его счета
- `UI()` - абстракция над ввводом/выводом.
## Диаграмма классов
Cм. `docs/adr_002_diagram.md`

## Решения
- [ADR-001: Разделение Game и UI](docs/adr_001_ui.md)

## Структура
```
practice1_3/
├── src/           # исходный код
├── tests/         # тесты
├── docs/          # документация
└── main.py        # точка входа
```
