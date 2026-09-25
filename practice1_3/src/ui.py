"""Интерфейс пользователя."""


class UI:
    """Абстракция над вводом/выводом"""

    def show_message(self, message: str) -> None:
        """Показать сообщение пользователю."""
        print(message)

    def get_input(self, prompt: str) -> str:
        """Получить ввод от пользователя."""
        return input(prompt)
