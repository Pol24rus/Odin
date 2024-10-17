"""Гороскоп"""
import random

def get_zodiak_signs():
    return["овен", "телец", "близнецы", "рак", "лев", "дева", "весы", "скорпион", "стрелец", "козерог", "водолей", "рыбы"]

def get_first_part():
    first = [
        "Будет хороший день ",
        "Принесет много денег ",
        "будет хорошая погода ",
        "будет непогода ",
        "будет туман ",
        "приготовьтесь, будет хорошо "
    ]
    return random.choice(first)

def get_second_part():
    second = [
        "Заботы близких станут олтвлекать от ",
        "вероятны споры про ",
        "Помните, что нельзя забывать про ",
        "те кто должен много денег должны помнить про ",
        "Мысли материальны, поэтому в течении дня думайте про "
    ]
    return random.choice(second)

def get_third_part():
    third = [
        "отношения с друзьями и близкими ",
        "работу и деловые вопросы ",
        "полезные для работы навыки ",
        "отдых, чтобы не помереть "
    ]
    return random.choice(third)

def generate_goroscope(zodiak_sign):
    horoscope = (
        f"Гороскоп для {zodiak_sign}:\n"
        f"{get_first_part()}"
        f"{get_second_part()}"
        f"{get_third_part()}"
    )
    return horoscope
def main():
    zodiak_sign = get_zodiak_signs()

    user_input = input("Введите свой знак зодиака\n")
    if user_input in zodiak_sign:
        print(generate_goroscope(user_input))
    else:
        print("Нет такого знака\n")

main()
