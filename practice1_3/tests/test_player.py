"""Тесты класса Player."""

from unittest.mock import Mock
from src.player import Player

class TestPlayer:
    """Проверяем начальное состояние игрока."""

    def test_initial_score(self):
        """Новый игрок имеет 0 очков."""
        p = Player("Test", Mock())
        assert p.get_score() == 0

    def test_name_is_set(self):
        """Имя игрока сохраняется."""
        p = Player("Иван", Mock())
        assert p.name == "Иван"


class TestMakeChoice:
    """Проверяем ввод игрока."""

    def test_valid_choice(self):
        """Корректный ввод возвращается как строка в нижнем регистре."""
        ui = Mock()
        ui.get_input.return_value = "Камень"
        p = Player("Test", ui)
        assert p.make_choice() == "камень"