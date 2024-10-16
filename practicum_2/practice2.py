# 1. Проверка четности числа
# num = int(input("Введите число: \n"))
# if num % 2 == 0:
#     print(f"{num} четное")
# else:
#     print(f"{num} нечетное")

# 2. Проверка положительности числа
# num = int(input("Введите число: \n"))
# if num > 0:
#     print(f"{num} - положительное")
# else:
#     print(f"{num} - отрицательное")

# 3. Проверка числа на кратность 5
# num = int(input("Введите число: \n"))
# if num % 5 == 0:
#     print(f"{num} кратно 5")
# else:
#     print(f"{num} не кратно 5")

# 4. Проверка числа на отрицательность
# num1 = int(input("Введите первое число: \n"))
# num2 = int(input("Введите второе число: \n"))
# if num1 > num2:
#     print(f"Наибольшее число первое {num1}")
# else:
#     print(f"Наибольшее число второе {num2}")

# 5. Сравнение 3 чисел
# num1 = int(input("Введите первое число: \n"))
# num2 = int(input("Введите второе число: \n"))
# num3 = int(input("Введите третье число: \n"))
# if num1 > num2 and num1 > num3:
#     print(f"Наибольшее число: {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f"Наибольшее число {num2}")
# else:
#     print(f"Наибольшее число {num3}")

# 6. Проверка диапазона от 10 до 20
# num = int(input("Введите число: \n"))
# if 10 <= num <= 20:
#     print("Число находится в диапазоне")
# else:
#     print("Число вне диапазона")

# 7. Проверка скорости (50 км/ч допустимая)
# speed = float(input("Введите скорость БПЛА\n"))
# max_speed = 50
# if speed > max_speed:
#     print("Скорость превышена")
# else:
#     print("Скорость в пределах нормы")

# 8. Проверка высоты (от 100 до 500)
# alt = float(input("Введите высоту\n"))
# if 100 <= alt <= 500:
#     print("Высота в пределах допустимого значения")
# else:
#     print("Высота вне допустимого значения")

# 9. Выбор направления движения
# direction = input("Введите направление движения\n").lower()
# if direction == "север":
#     print(f"Двигаемся на {direction}")
# elif direction == "юг":
#     print(f"Двигаемся на {direction}")
# elif direction == "запад":
#     print(f"Двигаемся на {direction}")
# elif direction == "восток":
#     print(f"Двигаемся на {direction}")
# else:
#     print("Неизвестное направление")

# 10. Определение времени полета
# speed = float(input("Введите скорость\n"))
# distance = float(input("Введите расстояние\n"))
# time = distance/speed
# print("Время полета", time)
# if time > 3:
#     print("Полет отменен")
# else:
#     print("Полет разрешен")

# 11. Определение времени работы аккумулятора
# battery_percent = float(input("Введите процент заряда аккумулятора\n"))
# max_flight_time = 2
# flight_time = (battery_percent / 100) * max_flight_time
# print(f"Предполагаемое время полета {flight_time} часов")

# 12. Вывод чисел от 1 до 10
# for i in range(1,11):
#     print(i)

# 13. Сумма чисел от 1 до 100
# total = 0
# for i in range(1,101):
#     total += i
# print("Сумма чисел от 1 до 100 равна",total)

# 14. Вывод четных чисел от 1 до 20
# for i in range(2,21,2):
#     print(i)

# 15. Обратный отсчет
# for i in range(10, 0, -1):
#     print(i)

# 16. Подсчет количества положительных чисел (5)
# positive_count = 0
# for i in range(5):
#     num = int(input("Введите число\n"))
#     if num > 0:
#         positive_count += 1
# print(f"Количество положительных чисел: {positive_count}")

# 17. Таблица умножения на 5
# for i in range(1, 11):
#     print(f"5 * {i} = {5 * i}")

# 18. Вывод всех цифр числа
# num = input("Введите число\n")
# for digit in num:
#     print(digit)

# 19. Сумма всех цифр числа
# num = input("Введите число\n")
# total = 0
# for digit in num:
#     total += int(digit)
# print("Сумма цифр равна",total)

# 20. Поиск минимального числа из 5 чисел
# min_num = float('inf')
# for i in range(5):
#     num = int(input("Введите число\n"))
#     if num < min_num:
#         min_num = num
# print(f"Минимальное число {min_num}")

# 21. Подсчет положительных и отрицательных чисел из 5
# negative_count = 0
# positive_count = 0
# for i in range(5):
#     num = int(input("Введите число\n"))
#     if num > 0:
#         positive_count += 1
#     else:
#         negative_count +=1
# print(f"Количество положительных чисел {positive_count}. Отрицательных {negative_count}")

# 22. Проверка наличия цифры 7
# number = input("Введите число\n")
# if '7' in number:
#     print("Число содержит цифру 7")
# else:
#     print("Число не содержит цифру 7")

# 23. Проверка диапазона значений (от 50 до 300)
# alts = []
# out_of_range = []
# while True:
#     alt = int(input("Введите высоту. (или -1 для завершения)\n"))
#     if alt == -1:
#         break
#     alts.append(alt)

#     if alt < 50 or alt > 300:
#         out_of_range.append(alt)

# if len(out_of_range) == 0:
#     print("Все высоты в допустимом диапазоне")
# else:
#     print("Некоторые высоты вне допустимого диапазона",out_of_range)

# 24. Таблица умножения
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")
#     print()

# 25. Подсчет количества глассных и согласных букв
# vowels = "аеёиоуыэюя"
# vowels_count = 0
# consanant_count = 0
# text = input("Введите строку:\n").lower()
# for char in text:
#     if char.isalpha():
#         if char in vowels:
#             vowels_count += 1
#         else:
#             consanant_count += 1
# print(f"Глассные {vowels_count}, Согласные {consanant_count}")

# 26. Создание списка четных чисел (1 до 100)
# even_numbers = []
# for num in range(1, 101):
#     if num % 2 == 0:
#         even_numbers.append(num)
# print(even_numbers)

# 27. Подсчет четных чисел в списке
# numbers = input("Введите числа, разделенные пробелом\n").split()
# even_count = 0
# for num in numbers:
#     if int(num) % 2 == 0:
#         even_count += 1
# print(f"Количество четных чисел {even_count}")

# 28. Удаление дубликатов из списка
# numbers = input("Введите числа, разделенные пробелом\n").split()
# unique_numbers = []
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)
# print("Список без дубликатов",unique_numbers)

# 29. Удаление дубликатов из списка
# numbers = input("Введите числа, разделенные пробелом\n").split()
# unique_number = list(set(numbers))
# print(unique_number)

# 30. Проверка строки на наличие чисел
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

# 31. Удаление всех цифр из строки
# input_string = input("Введите строку\n")
# output_string = ''
# for char in input_string:
#     if not char.isdigit():
#         output_string += char
# print(f"Строка без чисел {output_string}")

# 32. Разделение строки на слова
# input_string = input("Введите строку\n")
# words = input_string.split()
# for word in words:
#     print(word)

# 33. Подсчет количества положительных чисел в списке
# input_list = input("Введите числа через пробел\n")
# numbers = []
# positive_count = 0
# for num in input_list.split():
#     numbers.append(int(num))

# for num in numbers:
#     if num > 0:
#         positive_count += 1
# print(f"Количество положительных чисел {positive_count}")

# 34. Нахождение разности между минимальным и максимальным числом
# input_list = input("Введите числа через пробел\n")
# numbers = []
# positive_count = 0
# for num in input_list.split():
#     numbers.append(int(num))
# min_num = min(numbers)
# max_num = max(numbers)
# print(f"Разница между {min_num} и {max_num} равна {max_num - min_num}")

# 35. Проверка что все числа списка положительные
# input_list = input("Введите числа через пробел\n")
# numbers = []
# all_positive = True
# negative_numbers = []
# for num in input_list.split():
#     numbers.append(int(num))

# for num in numbers:
#     if num <= 0:
#         all_positive = False
#         negative_numbers.append(num)
# if all_positive:
#     print("Все числа положительные")
# else:
#     print("В списке есть отрицательные числа или нули", negative_numbers)

# 36. Подсчет оставшегося заряда аккумулятора
# intial_charge = float(input("Введите начальный заряд аккумулятора в %\n"))
# distance = float(input("Введите дистанцию полета в км\n"))
# consumption_rate = float(input("Введите расход на 1км\n"))
# remaining_charge = intial_charge - (distance * consumption_rate)
# if remaining_charge < 0:
#     remaining_charge = 0
# print(f"Осталось заряда аккумулятора {remaining_charge}")

# 37. Поиск минимальной скорости
# num_speeds = int(input("Введите количество показателей скорости\n"))
# speeds = []

# for i in range(num_speeds):
#     speed = float(input("Введите скорость БПЛА\n"))
#     speeds.append(speed)

# min_speed = min(speeds)
# print(f"Минимальная скорость среди {num_speeds} {speeds} : {min_speed}")

# 38. Определение высоты полета через n минут (Пусть каждую минуту подъем БПЛА 10 метров)
# n = int(input("Введите количество минут\n"))
# alt = 0
# for i in range(n):
#     alt += 10
# print(f"Высота через {n} минут равна {alt}м.")

# 39. Отслеживание уровня заряда батареи БПЛА (в минуту теряет 1%)
# battery = 100
# minutes = 0
# while battery > 20:
#     battery -= 1
#     minutes += 1
# print(f"Заряд достиг 20% через {minutes}мин.")

# 40. Расчет времени на полный круг БПЛА
# pi = 3.14
# diameter = 500
# speed = 10
# circumference = pi * diameter
# time = circumference / speed
# print(f"Время на полный круг {int(time)}с.")

# 41. Вывод полетов, которые длились более 30 минут
# flights_input = input("Введите продолжительность полетов через пробел\n")
# flights = []
# for i in flights_input.split():
#     flights.append(int(i))

# for flight in flights:
#     if flight > 30:
#         print(f"Полет длился {flight}m.")

# 42. Подсчет полетов с перегрузкой (более 30 кг)
weights_input = input("Введите массы груза через пробел\n")
weights = []
overload_flights = 0
for i in weights_input.split():
    weights.append(int(i))

# for weight in weights:
#     if weight > 30:
#         overload_flights += 1

print(f"Количество полетов с перегрузкой - {overload_flights}")

