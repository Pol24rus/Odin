# использование переменных
# a = 10
# print(a)
# 2. измененине значения переменной
a = 10
print(a)
b = 3
print(b)
# 3. использование неск переменных
c = a + b
# print(c)
#  4. типы данных
# print(type(c))
y = 3.14159
text = "Hello world"
is_active = True
# print(type(y))
# print(type(text))
# print(type(is_active))

# 5. операции
add = a + b
sub = a - b
mult = a * b
div = a / b
f_div = a // b
mod = a % b
exp = a ** b
# print(add)
# print(sub)
# print(mult)
# print(div)
# print(f_div)
# print(mod)
# print(exp)

#  операторы сравнения
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

#  логические операции
# a = True
# b = False
# print(a and b)
# print(a or b)
# print(not a)

#  8. булевы значения в арифметике
# result = a + b
# print(result)

# 9. сравнение целых цисел с числами с плавающей точкой
# a = 5
# b = 5.0
# result = a == b
# print("result = ", result)

#  Арифметика целые числа и плаваяющая точка
# a = 4
# print(type(a))
# b = 4.2
# print(type(b))
# result2 = a + b
# print(type(result2))
# print(result2)

# 11. преобразования типов данных, число в строку
# a = 10
# print(type(a))
# b = str(a)
# print(type(b))

# 12 преобр строки в число
# a = "15"
# print(type(a))
# b = int(a)
# print(type(b))
# print(b + 5)

# # 13. логические операторы с операторами сравнения
# a = 10
# b = 5
# print((a > b) and (b < 10))
# print((a > 5) and (b > 5))

# #  14. операции с дробями
# a = 1
# print(type(a))
# a = 1 / 3
# print(type(a))
# b = 2 / 5
# print(type(b))
# result = a + b
# print(type(result))
# print(result)

#  вычисление минут и сек
# ttl_sec = int(input("Введи те кол-во секунд\n"))
# minutes = ttl_sec // 60
# seconds = ttl_sec % 60
# another = ttl_sec / 60   # если так считать, то в результате будут минуты и сотые, а не секунды
# print(minutes, "минут", seconds, "секунд")
# print(another)

# #  вставка переменных с клавиатуры
# name = input("Введите своё имя\n")
# age = input("Введите свой возраст\n")
# message = "Привет, меня зовут " + name + ", мне " + age + " лет"
# print(message)
# print(f"Привет, меня зовут {name}, мне {age} лет")

#  17 длина строки
text = "Hello world"
# print(len(text))

#  умножение числа на строку
# print(text * 3)

# проверка наличия подстроки
# word = "Hello"
# result = word in text
# print(result)

#  20 извлечение символа по индексу
# char = text[1]
# print(char)
# char = text[-1]
# print(char)

#  округление числа
# number = 5.2359654
# rounded = round(number, 1)
# print(rounded)

#  сложение строки с числом
# с = "14"
# result = int(c) + a
# print(c)

# преобразование строки в нижний и верхний регистр
# text = "Hello world"
# lower_text = text.lower()
# print(lower_text)
# upper_text = text.upper()
# print(upper_text)

#  замена символов
# new_text = text.replace("world", "python")
# print(new_text)

# найти кол-во слов в тексте
# text = ("на финансовое обеспечение затрат по обеспечению профессионального развития граждан в рамках построения гибких "
#         "образовательных траекторий посредством реализации дополнительных профессиональных программ и (или) программ "
#         "профессионального обучения в соответствии с отраслевым yjdsv заказом")
# print(text.count(" ")+1)  # считаем пробелы + 1 слово в конце, после которого нет рпобела

# нахождение минимального и максимального элемента списка
numbers = [10, 5, 1, 3]
min_num = min(numbers)
max_num = max(numbers)
print("минимальный - ", min_num, "Максимальный - ", max_num)

#  добавление элемента в список
numbers.append(44)
print(numbers)