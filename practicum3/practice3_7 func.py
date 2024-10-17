# # сложение 2х чисел
# def add(a, b):
#     return a + b
#
# result = add(5, 8)
# print(result)
#
# """Сложение 2х чисел"""
# def add(a, b):
#     return a + b
#
# def main():
#     number_a = int(input("Введите первое число \n"))
#     number_b = int(input("Введите первое число \n"))
#     result = add(number_a, number_b)
#     print(result)
#
# main()

"""Проверка на чет и нечет"""
# def is_even(num):
#     return num % 2 == 0
#
# print(is_even(4))
# print(is_even(5))

"""Проверка на четность"""

# def get_user_input():  # функция ввода
#     # while True:
#     num = int(input("Введите число\n"))
#     return num
#
# def is_even(num):  # проверка на четность
#     return num % 2 == 0
#
# def display_result(num, is_even_result):  # функция вывода результата
#     if is_even_result:
#         print(f"{num} является четным")
#     else:
#         print(f"{num} является нечетным")
#
# def main():
#     number = get_user_input()
#     result = is_even(number)
#     display_result(number, result)
#
# main()

"""5. Поиск максимального числа"""
# def find_max(numbers):
#     return max(numbers)
#
# print(find_max([1, 2, 3, 5, 6, 8, 4, 7]))

"""6. поиск максимального числа"""
# def get_user_input():  # ввод и преобразование в список
#     user_input = input("ВВедите числа через пробел\n")
#     numbers = user_input.split()
#
#     convert_numbers = []
#     for num in numbers:
#         convert_numbers.append(int(num))
#
#     return convert_numbers
#
# def find_max(numbers):  # функция сравнения
#     return max(numbers)
# def display_result(max_number):  # функция вывода результата
#     print(f"Максимальное число {max_number}")
#
# def main():
#     numbers = get_user_input()
#     max_number = find_max(numbers)
#     display_result(max_number)
#
# main()

"""7. посик площади квадрата"""
# def get_user_input():  # ввод и преобразование в список
#     side = float(input("Введите длину стороны квадрата\n"))
#     while float(side) <= 0:  # проверка на положительный ввод/ Если исп if то отработает 1 раз
#         side = input("Ошибка, введите корректное положительное значение\n")
#     return float(side)
#
# def calculate(side):  # вычисление площади квадрата
#     return side ** 2
#
# def display_area(side, area):
#     print(f"Площадь квадрата со стороной {side} равна {area}")
#
# def main():
#     side_lenght = get_user_input()
#     area = calculate(side_lenght)
#     display_area(side_lenght, area)
#
# main()

"""Конвертер температур"""
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
#
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9
#
# def main():
#     print("Конвертер температур")
#     print("1. Цельсий в Фаренгейт")
#     print("2. Фаренгейт в Цельсий")
#     choice = input("Выберите вариант 1 или 2\n")
#     if choice == '1':
#         celsius = float(input("Введите температуру в Цельсиях\n"))
#         print(f"{celsius} градусов Цельсия = {celsius_to_fahrenheit(celsius)} градусов по Фаренгейту")
#     elif choice == '2':
#         fahrenheit = float(input("Введите температуру в Фаренгейтах\n"))
#         print(f"{fahrenheit} градусов по Фаренгейту = {fahrenheit_to_celsius(fahrenheit)} градусов по Цельсию")
#     else:
#         print("Некорректный выбор")
#
# main()

""""""