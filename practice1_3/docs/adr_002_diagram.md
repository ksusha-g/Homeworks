```mermaid
classDiagram
    class Game {
        -rules: dict
        -choices: list
        -max_rounds: int
        -round_number: int
        -computer_score: int
        -ui: UI
        -player: Player
        +run(): void
        +computer_choice(): str
        +determine_winner(player_choice: str, computer_choice: str): str
        +award_point(winner: str): void
        +show_results(): void
    }

    class Player {
        -name: str
        -score: int
        -ui: UI
        +make_choice(): str
        +add_point(): void
        +name: str
        +score: int
    }

    class UI {
        +show_message(message: str): void
        +get_input(prompt: str): str
    }

    Game --> UI : uses
    Game --> Player : creates
    Player --> UI : uses
```

## 1. Есть ли у вас наследование
Нет

## 2. Есть ли композиция? Что чем владеет?
Композиция есть. Game создаёт Player
Game владеет rules, choices, max_rounds, round_number, computer_score, ui, player
Player владеет name, score, ui
UI не владеет ничем

## 3. Есть ли циклические зависимости?
Нет