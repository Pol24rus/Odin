"""игра виселица"""
import random

words = ["камень", "ножницы", "бумага", "игра", "разум", "забвение"]
secret_word = random.choice(words)

guessed_letters = []  # список используемых букв
attemps = int(input("За сколько попыток угадаешь?\n"))  # кол-во попыток

print("Начинаем игру Виселица")

display = ''  # строка, где вводятся буквы
for letter in secret_word:
    display += '_ '  # кол-во букв в загаданном слове
print(display)

while attemps > 0:
    guess = input("Введите букву:\n").lower()

    if guess.isalpha() and len(guess) == 1:
        if guess in guessed_letters:
            print(f"Вы вводили  букву {guess}\n")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attemps -= 1
            print(f"Неверно, у вас осталось {attemps} попыток")
        else:
            print(f"Буква {guess} есть в слове")

        display = ''  # дисплей очищаем
        for letter in secret_word:
            if letter in guessed_letters:  # проверяем, есть ли в списке угаданных
                display += letter + ''  # добавляем букву в строку и пробел
            else:
                display += "_ "  # увеличиваем строку на прочерк нижний
        print(display)
        if '_ ' not in display:
            print(f"Поздравляем! Вы угадали слово {secret_word}")
            break
    else:
        print("Некорректный ввод")