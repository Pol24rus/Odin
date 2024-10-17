"""Угадать число, загаданное компьютером"""
import random

attempts = 0  #для кол-ва попыток
while True:
    finite_number = int(input("Введите до какого числа загадывать (не менее 20)\n"))
    if finite_number <= 20:
        print("Загаданное число менее 20")
    else:
        break

comp_number = random.randint(1, finite_number)

while True:
    user_number = int(input(f"ВВедите число от 1 до {finite_number}. Для окончания введи 0\n"))
    attempts += 1
    if user_number == 0:
        print(f"Загаданное число было {comp_number}")
        break
    elif user_number > comp_number:
        print("Введи число меньше")
    elif user_number < comp_number:
        print("Введи число больше")
    else:
        print(f"Вы угадали за {attempts + 1} попыток, это число {comp_number}")
        break



