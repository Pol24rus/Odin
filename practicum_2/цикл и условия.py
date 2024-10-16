"""1. Проверка четности числа"""
# num = int(input("Введите число: \n"))
# if num % 2 == 0:
#     print(f"Число {num} четное")
# else:
#     print(f"Число {num} нечетное")

"""2. проверка положительности числа"""
# num = int(input("Введите число: \n"))
# if num > 0:
#     print(f"Число {num} положительное")
# else:
#     print(f"Число {num} отрицательное")

"""3. Проверка числа на кратность пяти"""
# num = int(input("Введите число: \n"))
# if num % 5 == 0:  # остаток от деления равен нулю
#     print(f"Число {num} кратно пяти")
# else:
#     print(f"Число {num} некратно пяти")

"""Проверка числа на отрицательность"""
# num1 = int(input("Введите первое число: \n"))
# num2 = int(input("Введите второе число: \n"))
# if num1 > num2:
#     print(f"Наибольшее число {num1}")
# else:
#     print(f"Наибольшеее число {num2}")

"""Сравнение 3х чисел"""
# num1 = int(input("Введите первое число: \n"))
# num2 = int(input("Введите второе число: \n"))
# num3 = int(input("Введите третье число: \n"))
# if num1 > num2 and num1 > num3:
#     print(f"Наибольшее число {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f"Наибольшее число  {num2}")
# else:
#     print(f"Наибольшее число {num3}")

"""Проверка диапазона от 10 до 20"""
# num = int(input("Введите число: \n"))
# if 10 <= num <= 20:
#     print(f"Число {num} находится в требуемом диапазоне от 10 до 20")
# else:
#     print(f"Число {num} вне диапазона")

"""7 проверка на скорость"""
# speed = float(input("Введите скорость БПЛА: \n"))
# max_speed = 50
# if speed > max_speed:
#     print("Скорость превышена")
# else:
#     print("Скорость в пределах нормы")

"""Проверка высоты"""
# alt = float(input("Введите высоту БПЛА: \n"))
# if 100 <= alt <= 500:
#     print("Высота в пределах нормы")
# else:
#     print("Высота вне предлелов нормы")

"""ВЫбор  направления движения"""
# direction = input("Введите направление движения\n").lower()
# if direction == "север":
#     print(F"Двигаемся на {direction}")
# elif direction == "юг":
#     print(F"Двигаемся на {direction}")
# elif direction == "запад":
#     print(F"Двигаемся на {direction}")
# elif direction == "восток":
#     print(F"Двигаемся на {direction}")
# else:
#     print("Некорректное направление")

""" 10 Определить время полёта"""
# speed = float(input("Введите скорость\n"))
# distance = float(input("Введите расстояние\n"))
# time = distance / speed
# print("Время полета составляет -", time)
# if time > 3:
#     print("Полет отменен")
# else:
#     print("Полёт разрешен")

"""11. Определение времени работы аккумулятора"""
# battery_percent = float(input("Введите % заряда аккумулятора\n"))
# max_flying_time = 2
# flight_time = (battery_percent / 100) * max_flying_time
# print(f"Время полета составляет {flight_time} часов")

"""12. Вывод чисел от 1 до 10"""
# for i in range(5):  # От 0 до 4
#     print(i)
# for i in range(1, 5):  # от 1 до 4
#     print(i)

""" 13. сумма от 1 до 100"""
# total = 0
# for i in range(1, 101):
#     total += i
#     # print(f"Сумма чисел от 1 до 100 равняется {total}")  #если указать внутри цикла, то будет распечатан каждый шаг
# print(f"Сумма чисел от 1 до 100 равняется {total}")  # распечатан только итог

"""14 Вывод четных чисел от 1 до 20"""
# for i in range(2, 21, 2):
#     print(i)

"""15 Обратный отсчет"""
# for i in range(10, 0 , -1):
#     print(i)

"""16 Подсчет кол-ва положительных чисел (5)"""
# positive_count = 0
# for i in range(5):
#     num = int(input("Введите число\n"))
#     if num > 0:
#         positive_count += 1
# print(f"Количестов положительных чисел {positive_count}")

"""17 Таблица умножения на 5"""
# for i in range(1,11):
#     print(f"5 * {i} = {5*i}")

"""18 Вывод всех цифр числа"""
# num = input("Введите число\n")
# for i in num:
#     print(i)

"""19 Найти сумму всех цифр числа"""
# num = input("Введите число\n")
# total = 0
# for i in num:
#     total += int(i)
# print("Сумма цифр числа равна ", total)

""" 20 Найти миниммальное число из 5 чисел"""
# min_num = float('inf')  # inf - бесконечность, те любое введенное число будет меньше
# for i in range(5):
#     num = int(input("Введите число\n"))
#     if num < min_num:  # любое введенное число меньше бесколнечности
#         min_num = num  # и тогда минимальным становится введенное число
# print(f"Минимальное число {min_num}")

""" 21 Подсчет положительных и отрицательных чисел из 5"""
# negative_count = 0
# positive_count = 0
# for i in range(5):
#     num = int(input("Введите число\n"))
#     if num > 0:
#         positive_count += 1
#     else:
#         negative_count += 1
# print(f"кол-во положительных чисел {positive_count}, кол-во отрицательных чисел {negative_count}")

""" 22 Проверка наличия цифры 7"""
# number = input("Введите число \n")
# if "7" in number:
#     print("Число содержит цифру 7")
# else:
#     print("Число не содержит цифру 7")

""" 23 Проверка диапазона значений от 50 до 300"""
# alts = []
# out_of_range = []
# while True:
#     alt = int(input("Введите высоту (или 0 для завершения)\n"))
#     if alt == 0:
#         break
#     alts.append(alt)
#
#     if alt < 50 or alt > 300:
#         out_of_range.append(alt)
#
# if len(out_of_range) == 0:
#     print("Все высоты в допустимом диапазоне")
# else:
#     print("Некоторые высоты вне допустимого диапазона", out_of_range)

""" 24 Таблица умножения """
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")
#     print()

""" 25 кол-во гласных и согласных"""
# vowels = "ёйуеыаоэяию"
# vowels_count = 0
# consanant_count = 0
# text = input("ВВедите строку\n").lower()
# for char in text:
#     if char.isalpha():  # проверка буква ли это
#         if char in vowels:
#             vowels_count += 1
#         else:
#             consanant_count += 1
# print(f"Кол-во гласных равно {vowels_count}, кол-во согласных {consanant_count}")

""" 26 создание списка четных чисел от 1 до 100"""
# even_numbers = []
# for numb in range(1, 101):
#     if numb % 2 == 0:
#         even_numbers.append(numb)
# print(even_numbers)

"""27 подсчет четных чисел в списке"""
# numbers = input("Введите числа с пробелом\n").split()
# print(type(numbers))
# even_count = 0
# for num in numbers:
#     if int(num) % 2 == 0:
#         even_count += 1
# print(f"Кол-во четных чисел равно {even_count}")

""" 28 Удаление дубликатов из списка"""
# numbers = input("Введите числа с пробелом\n").split()
# unique_num = []
# for num in numbers:
#     if num not in unique_num:
#         unique_num.append(num)
# print(" Список без дубликатов ", unique_num)

""" 29 Удаление дубликатов из списка"""
# numbers = input("Введите числа с пробелом\n").split()
# unique_num = list(set(numbers))
# print(unique_num)

"""30 проверка строки на наличие чисел """
# input_string = input("Введите строку\n")
# contains_digit = False
# for char in input_string:
#     if char.isdigit():
#         contains_digit = True
#         break
# if contains_digit:
#     print("Строка содержит цифры")
# else:
#     print("Строка не содержит цифры")

""" 31 удалить все цифры из строки"""
# input_string = input("Введите строку\n")
# output_string = ' '
# for char in input_string:
#     if not char.isdigit():
#         output_string += char
# print(f"Строка из чисел {output_string}")

""" 32 Разделение строки на слова"""
# input_string = input("Введите строку\n")
# words = input_string.split()
# print(words)
# for word in words:
#     print(word)

""" 33 подсчет кол-ва положительных чисел"""
# input_list = input("Введите числа через пробелы\n")
# numbers = []
# positive_count = 0
# for num in input_list.split():
#     numbers.append(int(num))
# print(numbers)
# for num in numbers:
#     if num > 0:
#         positive_count += 1
# print(f"Кол-во положительных чисел {positive_count}")

"""" 34 нахождение разницы между мин и макс числом в списке """
# input_list = input("Введите числа через пробелы\n")
# numbers = []
# positive_count = 0
# for num in input_list.split():
#     numbers.append(int(num))
# min_num = min(numbers)
# max_num = max(numbers)
# print(min_num, max_num)
# print(f"Разница между {min_num} и {max_num} равна {max_num - min_num}")

"""35 проверка что все числа списка  положительны"""
# input_list = input("Введите числа через пробелы\n")
# numbers = []
# all_positive = True
# negative_numbers = []
# for num in input_list.split():
#     numbers.append(int(num))
#
# for num in numbers:
#     if num <= 0:
#         all_positive = False
#         negative_numbers.append(num)
# if all_positive:
#     print("Все числа положительные")
# else:
#     print("В списке есть отрицательные числа или ноль", negative_numbers)

"""36 Подсчет оставшегося заряда аккумулыятора"""
# intial_charge = float(input("ВВедите начальный заряд аккумулятора\n"))
# distance = float(input("Введите дальность полета\n"))
# consumption_rate = float(input("Введите расход на 1 км\n"))
# remaining_charge = intial_charge - (distance * consumption_rate)
# if remaining_charge < 0:
#     remaining_charge = 0
# print("Оставшийся заряд ", remaining_charge)

"""37 Поиск минимальной скорости"""
# num_speeds = int(input("Введите кол-во показателей скороксти\n"))
# speeds = []
#
# for i in range(num_speeds):
#     speed = float(input("Введите скорость БПЛА\n"))
#     speeds.append(speed)
# min_speeds = min(speeds)
# print(f"Минимальная скорость среди {num_speeds} {speeds} : {min_speeds}")

"""38 Определить высоту полета через n минут (каждые 1 мин подъем на 10 метров)"""
# n = int(input("Введи те кол-во минут\n"))
# alt = 0
# for i in range(n):
#     alt += 10
# print(f"Высота через {n} минут составит {alt} метров")

"""39 Отслеживание урвня заряда (в минутут теряет 1%)"""
# battery = 100
# minutes = 0
# while battery > 20:
#     battery -= 1.5
#     minutes += 1
# print(f"Батарея достигнет заряд 20% через {minutes} минут")

""" 40 Расчет времени на полный круг"""
# pi = 3.14
# diametr = 500
# speed = 10
# circumference = pi * diametr
# time = circumference / speed
# print(f"Время на полный круг {int(time)} сек ")

"""41 Вывод полетов, которые длились более 30 минут"""
# flights_input = input("Введите продолжительность полетов через пробел\n")
# flights = []
# for i in flights_input.split():
#     flights.append(int(i))
#
# for flight in flights:
#     if flight > 30:
#         print(f"Полет длился {flight} минут")

""" 42 Подсчет полетов с перегрузкой ,jktt 30 ru"""
weights_input = input("Введите массу груза через пробел\n")
weights = []
overload_flights = 0
for i in weights_input.split():
    weights.append(int(i))

for weight in weights:
    if weight > 30:
        overload_flights += 1

print(f"Кол-во полетов с перегрузкой  - {overload_flights}")