"""Игра в кости"""
import random

def roll_dice():  #бросок кубика
    return random.randint(1, 6)

def play_round():
    input("\nНажмите Enter чтобы бросить кости\n")
    player_roll = roll_dice()
    comp_roll = roll_dice()

    print(f"Ваш результат {player_roll}")
    print(f"Результат компьютера {comp_roll}")

    return player_roll, comp_roll

def winner(player_roll, comp_roll):
    if player_roll > comp_roll:
        return "player"
    elif player_roll < comp_roll:
        return "comp"
    else:
        return "tie"

def main():
    player_score = 0
    comp_score = 0

    print(" Добро пожаловать в игру Кости")
    rounds = int(input("Введите кол-во раундов\n"))

    for rounds in range(rounds):
        player_roll, comp_roll = play_round()
        # comp_roll = play_round()
        game_winner = winner(player_roll, comp_roll)

        if game_winner == 'player':
            print("Вы победили в этом раунде")
            player_score += 1
        elif game_winner == 'comp':
            print("Комп победил в этом раунде")
            comp_score += 1
        else:
            print("Ничья")
    print(f"\nИтоги: Ваши очки {player_score}, Компьютера очки {comp_score}")
    if player_score > comp_score:
        print("Вы победили")
    elif player_score < comp_score:
        print("Вы проиграли")
    else:
        print("Ничья")

main()