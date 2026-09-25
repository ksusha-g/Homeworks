# Исходный код
```
# ИСХОДНЫЙ ПРОЦЕДУРНЫЙ КОД (только для анализа)
# Игра «Камень-ножницы-бумага»

import random


def play_rock_paper_scissors_procedural():
    # Правила игры
    choices = ["камень", "ножницы", "бумага"]
    rules = {
        "камень": "ножницы",
        "ножницы": "бумага",
        "бумага": "камень",
    }
    
    # Начальное состояние
    player_score = 0
    computer_score = 0
    max_rounds = 3
    round_number = 0
    
    print("Добро пожаловать в игру «Камень-ножницы-бумага»!")
    print(f"Играем до {max_rounds} побед. Победитель определяется по большинству выигранных раундов.")
    
    # Основной цикл игры
    while player_score < max_rounds and computer_score < max_rounds:
        round_number += 1
        print(f"\n--- Раунд {round_number} ---")
        print(f"Счёт: Игрок {player_score} : {computer_score} Компьютер")
        
        # Ввод игрока
        try:
            player_choice = input("Ваш выбор (камень/ножницы/бумага): ").strip().lower()
        except KeyboardInterrupt:
            print("\nИгра прервана.")
            return
        
        # Проверка корректности ввода
        if player_choice not in choices:
            print("Неверный выбор! Попробуйте снова.")
            continue
        
        # Выбор компьютера
        computer_choice = random.choice(choices)
        print(f"Компьютер выбрал: {computer_choice}")
        
        # Определение победителя раунда
        if player_choice == computer_choice:
            print("Ничья!")
        elif rules[player_choice] == computer_choice:
            print("Вы выиграли раунд!")
            player_score += 1
        else:
            print("Вы проиграли раунд!")
            computer_score += 1
    
    # Итог игры
    print("\n=== Игра окончена ===")
    print(f"Финальный счёт: Игрок {player_score} : {computer_score} Компьютер")
    
    if player_score > computer_score:
        print("Поздравляем! Вы победили!")
    else:
        print("Увы! Компьютер победил. Попробуйте ещё раз.")


# Функция определена, готова к анализу
print("Функция play_rock_paper_scissors_procedural определена.")
```

# 1.1 Таблица анализа
| Что                    | Где в исходном коде            | Куда перенести       |
|------------------------|--------------------------------|----------------------|
| Правила игры           | rules = {...}, choices = [...] | Аттриут Game()       |
| Счет игрока            | player_score = 0               | Аттриут Player()     |
| Счет компьютера        | computer_score = 0             | Аттриут Game()       |
| Лимит побед            | max_rounds = 3                 | Аттриут Game()       |
| Номер раунда           | round_number = 0               | Аттриут Game()       |
| Выбор игрока           | input("Ваш выбор: ")           | Метод Player()       |
| Выбор компьютера       | random.choice(choices)         | Метод Game()         |
| Проверка ввода         | if player_choice not...        | Метод Player()       |
| Определение победителя | if player_choice == ...        | Метод Game()         |
| Начисление очков       | player/computer_score += 1,    | Метод Game()         |
| Вывод                  |  print(...)                    | Метод UI()           |
| Ввод                   | input(...)                     | Метод UI()           |

# 1.2
## 1. Какие классы вы выделите? Обоснуйте.
Я выделю классы: Game(), Player(), UI()
| Game()                                    | Player()            | UI()                     |
|-------------------------------------------|---------------------|------------------------- |
| Хранит состояние игры и управляет логикой | Хранит данные игрока| Отвечает за вывод и ввод |

## 2. Какие атрибуты будут приватными
- self.__score - чтобы нельзя было сменить счет
- self.__computer_score - чтобы нельзя было сменить счет компьютера
- self.__max_rounds - чтобы нельзя было сменить кол-во раундов
- self.__round_number - чтобы нельзя было сменить номер раунда
- self.__rules - чтобы нельзя было изменить правила

## 3. Какие методы будут публичными?
- game.run() - чтобы игру можно было запустить
- game.determine_winner() - определить победителя
- player.make_choice() - выбор игрока
- ui.show_message() - вывод
- ui.get_input() - ввод

## 4. Есть ли в исходном коде «God Object»?
Да, есть. Это функция **play_rock_paper_scissors_procedural()**.
В ней сосредоточена абсолютно вся логика. Она обрабытывает процесс игры, ввод и вывод, а также ошибки
