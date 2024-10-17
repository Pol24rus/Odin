"""Камень ножницы бумага"""
import random

print("Играем в камень - ножницы - бумага")
user_choice = ''  #изначально у игрока ничего, пустая строка
comp_choice = ''
user_score = 0  #счет игрока
comp_score = 0
variants = ['камень', 'ножницы', 'бумага']
rounds = int(input("Введите кол-во раундов\n"))
for round in range(rounds):
    print(f"Текущий раунд - {round+1}")
    while True:
        user_choice = input("Введите камень, ножницы или бумага\n").lower()
        if user_choice == 'камень' or user_choice == 'ножницы' or user_choice == 'бумага':
            break
        else:
            print("Некорректный ввод\n")
    comp_choice = random.choice(variants)
    # print(comp_choice)
    if user_choice == comp_choice:
        print("Ничья")
        print(f"Ваш выбор {user_choice}, выбор компа {comp_choice}")
    elif user_choice == 'камень' and comp_choice == 'ножницы':
        print("Ты выиграл!")
        print(f"Ваш выбор {user_choice}, выбор компа {comp_choice}")
        user_score += 1
    elif user_choice == 'ножницы' and comp_choice == 'бумага':
        print("Ты выиграл!")
        print(f"Ваш выбор {user_choice}, выбор компа {comp_choice}")
        user_score += 1
    elif user_choice == 'бумага' and comp_choice == 'камень':
        print("Ты выиграл!")
        print(f"Ваш выбор {user_choice}, выбор компа {comp_choice}")
        user_score += 1
    elif user_choice == 'камень' and comp_choice == 'бумага':
        print("Ты проиграл!")
        print(f"Ваш выбор {user_choice}, выбор компа {comp_choice}")
        comp_score += 1
    elif user_choice == 'ножницы' and comp_choice == 'камень':
        print("Ты проиграл!")
        print(f"Ваш выбор {user_choice}, выбор компа {comp_choice}")
        comp_score += 1
    elif user_choice == 'бумага' and comp_choice == 'ножницы':
        print("Ты проиграл!")
        print(f"Ваш выбор {user_choice}, выбор компа {comp_choice}")
        comp_score += 1

if user_score > comp_score:
    print(f"Ты победил в игре со счетом {user_score} : {comp_score}")
elif user_score < comp_score:
    print(f"Ты проиграл в игре со счетом {user_score} : {comp_score}")
else:
    print("Ничья")