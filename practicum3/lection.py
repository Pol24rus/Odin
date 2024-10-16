"""Импорт библиотеки"""
import math
# print(math.pi)
import os
import requests
import numpy as np
import my_module as mm
"""Импорт модуля (конкретной ф-ции) из библиотеки"""
# from math import sqrt
# print(sqrt(16))
"""импорт модуля с псевдонимом"""
# import datetime as dt
# current_time = dt.datetime.now()
# print(current_time)
# formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date)
"""работа с директорией os"""
# current_directory = os.getcwd()  # просмотр текущей директории
# print(current_directory)
"""Работа с запросами requests"""
# url = "https://github.com/Pol24rus/Odin/tree/master/practicum_2"
# responce = requests.get(url)
# print(responce)
# # data = responce.text
# data = responce.json()
# print(data)
"""ВЫполнение мат операций с массивом"""
# array = np.array([1, 2, 3, 4, 5])
# print(array)
# result = np.square(array)
# print(result)
"""Функции"""

# def greet():
#     print("Hello world")
#
#
# greet()  # приветствие
#
#
# def add_number(a, b):
#     return a + b
#
#
# result = add_number(4, 5)
# print(result)
#
#
# def power(base, exponent=2):
#     return base ** exponent
#
#
# result = power(3)
# print(result)  # вернет 3 во 2-й степени, тк 2 уже определено
# result = power(3, 3)  # вернет 3 в 3-й степени

"""ВЫзов по имени"""
# def students(name, age):
#     print(f"Имя: {name}, возраст {age}")
#
# students("John", 20)

"""Рекурсия"""
# def add(a, b):
#     if b == 0:  # базовый случай. при нем рекурсия завершит вызов самой себя
#         return a
#     return add(a + 1, b - 1)
# print(add(6, 4))  # будет цикл, пока b не станет равным нулю

"""импорт из файла, в данном случае my_module"""
a = int(input("Введите первое число\n"))
b = int(input("Введите второе число\n"))
result = mm.sum(a, b)
print(f"Сумма {a} и {b} равна {result}")