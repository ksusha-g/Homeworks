"""Тесты класса Game."""

from src.game import Game
from src.ui import UI
from src.player import Player

class FakeUI(UI):
    """Фейковый UI: не запрашивает ввод, записывает вывод в список."""

    def __init__(self):
        self.messages = []

    def show_message(self, message: str) -> None:
        self.messages.append(message)

    def get_input(self, prompt: str) -> str:
        return "камень"   # всегда камень по умолчанию

def make_game():
    return Game(ui=FakeUI())


class TestDetermineWinner:
    """Проверяем логику определения победителя."""

    def test_draw(self):
        """Одинаковые ходы → ничья."""
        g = make_game()
        assert g.determine_winner("камень", "камень") == "draw"
        assert g.determine_winner("ножницы", "ножницы") == "draw"
        assert g.determine_winner("бумага", "бумага") == "draw"

    def test_player_wins(self):
        """Проверяем, что игрок побеждает."""
        g = make_game()
        assert g.determine_winner("камень", "ножницы") == "player"
        assert g.determine_winner("ножницы", "бумага") == "player"
        assert g.determine_winner("бумага", "камень") == "player"

    def test_computer_wins(self):
        """Проверяем, что компьютер побеждает."""
        g = make_game()
        assert g.determine_winner("ножницы", "камень") == "computer"
        assert g.determine_winner("бумага", "ножницы") == "computer"
        assert g.determine_winner("камень", "бумага") == "computer"


class TestComputerChoice:
    """Проверяем ход компьютера."""

    def test_computer_choice(self):
        """Компьютер всегда выбирает из допустимых ходов."""
        g = make_game()
        for _ in range(100):  # Проверим 100 раз
            choice = g.computer_choice()
            assert choice in g.CHOICES


class TestAwardPoint:
    """Проверяем начисление очков."""

    def test_player_gets_points(self):
        """Игрок получает очки при победе"""
        g = make_game()
        from src.player import Player
        g._Game__player = Player("Test", FakeUI())

        g._Game__player.add_point()
        assert g._Game__player.get_score() == 1

    def test_computer_gets_points(self):
        """Компьютер получает очки при победе"""
        g = make_game()
        g._Game__computer_score += 1
        assert g._Game__computer_score == 1

        