"""Генерировать список случайных чисел"""
"""Найдем макс  и мин и среднее"""
"""Создать список квдратов"""
""""кол-во четных и нечетныч"""

import random

def generate_random_numbers(count, min_val, max_val):
    numbers = []
    for i in range(count):
        number = random.randint(min_val, max_val)
        numbers.append(number)
    return numbers

def calculate(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    avg_num = sum(numbers) / len(numbers)
    return min_num, max_num, avg_num

def squares(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num ** 2)
    return squared_numbers

def count_even_odd(numbers):
    count_evens = 0
    count_odd = 0
    for num in numbers:
        if num % 2 == 0:
            count_odd += 1
        else:
            count_evens += 1
    return count_odd, count_evens

def main():
    numbers = generate_random_numbers(10, 1, 100)
    print(f"Список случайных чисел: {numbers}")
    min_num, max_num, avg_num = calculate(numbers)
    print(f"Минимум {min_num}, Максимум {max_num}, среднее: {avg_num}")
    squared_numbers = squares(numbers)
    print(f"Квадратные корни числе {numbers} равны {squared_numbers}")
    count_odd, count_evens = count_even_odd(numbers)
    print(f"Нечетных чисел - {count_evens}, четных чисел {count_odd}")

main()