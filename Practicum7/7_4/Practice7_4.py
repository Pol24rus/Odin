import json

def load_cities():
    with open('russia.json', 'r', encoding='utf-8') as file:
        return json.loads(file.read())

def display_intro():
    print("Добро пожаловать в игру города. Пиши в одном сообщении й город. Если хочешь закончить, то напиши стоп. 1й город - Москва")

def first_letter(user_input, letter):
    return user_input.lower()[0] == letter

def check_city(file, user_input):
    for city in file:
        if city['city'].lower() == user_input.lower():
            return city
    return None

def remove_city(file, city_to_remove):
    for i in range(len(file)):
        if file[i]['city'].lower() == city_to_remove.lower():
            del file[i]
            return

def last_letter(city_name):
    last_char = city_name[-1].lower()
    if last_char in ('ы', 'ъ', 'ь'):
        return city_name[-2].lower()
    return last_char

def find_next_city(file, letter):
    for city in file:
        if city['city'].lower().startswith(letter):
            return city
    return None

def main():
    file = load_cities()
    display_intro()
    letter = 'a'

    while True:
        user_input = input("ВВедите город\n")

        if user_input.lower() == 'стоп':
            print("Игра окончена")
            break

        if not first_letter(user_input, letter):
            print(letter)
            print("Перввая буква не свпадает с последней в названном городе")
            continue

        city = check_city(file, user_input)

        if city is None:
            print("Такого города нет или его уже называли")
            continue

        remove_city(file, user_input)

        letter = last_letter(user_input)
        next_city = find_next_city(file, letter)

        if next_city:
            print((next_city['city']))
            remove_city(file, next_city['city'])
            letter = last_letter(next_city['city'])
        else:
            print("Ты победил")
            return

main()
