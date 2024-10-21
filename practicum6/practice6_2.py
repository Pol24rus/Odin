"""Проверка надежности пароля"""
import random
import string

def check_password_streinght(password):
    errors = []

    if len(password) < 8:
        errors.append("Пароль должен содержать не менее 8 символов")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    # special_characters = "'!@#$%^&*()}{[]|\:;?/>.<,"
    special_characters = '!@#$%^&*()_-+={[<,.>/?`~№%:;"]}'


    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if not has_upper:
        errors.append("Пароль должен соджержать заглавную букву")
    if not has_lower:
        errors.append("Пароль должен содержать строчную букву")
    if not has_digit:
        errors.append("Пароль должен содержать цифру")
    if not has_special:
        errors.append("Пароль должен содержать спецсимвол")

    return errors

def display_errors(errors):
    print("Пароль небезопасен, ошибка")
    for error in errors:
        print(f" - {error}")

def generate_random_password(lenght):
    if lenght < 8:
        return "Длина пароля меньше 8 символов"
    special_characters = "'!@#$%^&*()}{[]|\:;?/>.<,"
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(special_characters)
    ]
    all_characters = string.ascii_letters + string.digits + special_characters
    for i in range(lenght-4):  # тк 4 условиям уже есть в строках выше
        password.append(random.choice(all_characters))

    random.shuffle(password)  # перемешиваем внутри пароля
    return ''.join(password)  # приводим список к строке

def maun():
    password = input("Введите пароль\n")
    errors = check_password_streinght(password)
    if not errors:
        print("Паролдь безопасен")
    else:
        display_errors(errors)
        random_password = generate_random_password(8)
        print(f"Сгенерированный безопасный пароль {random_password}")

maun()