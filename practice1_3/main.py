"""Точка входа в игру."""

from src.game import Game
from src.ui import UI


def main() -> None:
    ui = UI()
    game = Game(max_rounds=5, ui=ui)
    game.run()


if __name__ == "__main__":
    main()