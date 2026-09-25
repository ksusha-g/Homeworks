"""Игрок."""

from .ui import UI

class Player:
    def __init__(self, name: str, ui: UI):
        self.name = name
        self.__score = 0
        self._ui = ui

    def make_choice(self) -> str:
        """Запросить у игрока ход (камень/ножницы/бумага).
        
        Повторяет запрос при неверном вводе.
        """
        while True:
            try:
                raw = self._ui.get_input("Ваш выбор (камень/ножницы/бумага): ")
                return raw.lower()
            except ValueError:
                self._ui.show_message("Введите целое число!")

    def add_point(self) -> None:
        """Добавить очко игроку."""
        self.__score += 1

    def get_score(self) -> int:
        """Получить количество очков игрока."""
        return self.__score
    