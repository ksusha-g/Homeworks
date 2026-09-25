"""Игра «Камень-ножницы-бумага»."""

import random
from .ui import UI
from .player import Player

class Game:
    """Управляет игровым циклом «Камень-ножницы-бумага»."""

    RULES = {
        "камень": "ножницы",
        "ножницы": "бумага",
        "бумага": "камень",
    }

    CHOICES = ["камень", "ножницы", "бумага"]

    def __init__(self, ui: UI, max_rounds: int = 5) -> None:
        self._ui = ui
        self.__max_rounds = max_rounds
        self.__round_number = 0
        self.__computer_score = 0
        self.__player = None

    def run(self) -> None:
        """Запустить игровой цикл."""
        self._ui.show_message("Добро пожаловать в игру «Камень-ножницы-бумага»!")
        self._ui.show_message(f"Играем до {self.__max_rounds} побед. Победитель — по большинству очков.")
        self.__player = Player("Игрок", self._ui)

        while (
            self.__player.get_score() < self.__max_rounds
            and self.__computer_score < self.__max_rounds
        ):
            self.__round_number += 1
            self._ui.show_message(f"--- Раунд {self.__round_number} ---")
            self._ui.show_message(
                f"Счёт: Игрок {self.__player.get_score()} : "
                f"{self.__computer_score} Компьютер"
            )

            #если игрок ввел не то, что мы хотели
            player_choice = self.__player.make_choice()
            if player_choice not in self.CHOICES:
                self._ui.show_message("Неверный выбор! Попробуйте снова.")
                self.__round_number -= 1
                continue

            #ход компьютера
            computer_choice = self.computer_choice()
            self._ui.show_message(f"Компьютер выбрал: {computer_choice}")

            #определяем победителя
            winner = self.determine_winner(player_choice, computer_choice)

            if winner == "player":
                self._ui.show_message("Вы победили в этом раунде!")
                self.__player.add_point()
            elif winner == "computer":
                self._ui.show_message("Компьютер победил в этом раунде!")
                self.__computer_score += 1
            elif winner == "draw":
                self._ui.show_message("Ничья!")

        self.show_results()

    def computer_choice(self) -> str:
        """Случайный выбор компьютера."""
        return random.choice(self.CHOICES)

    def determine_winner(self, player_choice: str, computer_choice: str) -> str:
        """Определить победителя раунда."""

        if player_choice == computer_choice:
            return "draw"
        elif self.RULES[player_choice] == computer_choice:
            return "player"
        else:
            return "computer"

    def show_results(self) -> None:
        """Показать результаты игры."""
        if self.__player.get_score() > self.__computer_score:
            self._ui.show_message("Поздравляем! Вы победили!")
        elif self.__player.get_score() < self.__computer_score:
            self._ui.show_message("Компьютер победил!")