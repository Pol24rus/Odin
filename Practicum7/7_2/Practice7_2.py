"""Читаем csv файл. Подсчитываем общую сумму зарплат.
Найдем с макс и мин зарплатой. В тхт выведем общую сумму, среднюю з/п, мин и макс"""

# def create_csv(filename):
#     data = [
#         ["Ivan", 50000],
#         ["Petr", 47000],
#         ["Nikolas", 40000],
#         ["Alex", 53000],
#         ["Svetlana", 60000],
#         ["Olga", 65000],
#         ["Maria", 45000],
#         ["Semen", 52000]
#     ]
#     with open(filename, "w", encoding='utf-8') as file:
#         for entry in data:
#             name = entry[0]
#             money = entry[1]
#             line = f"{name},{money}\n"
#             file.write(line)

import random

def create_random_csv(filename):
    data = [
            ["Ivan"],
            ["Petr"],
            ["Nikolas"],
            ["Alex"],
            ["Svetlana"],
            ["Olga"],
            ["Maria"],
            ["Semen"]
        ]
    with open(filename, "w", encoding='utf-8') as file:
        for entry in data:
            name = entry[0]
            salary = random.randint(40000, 65000)
            line = f"{name},{salary}\n"
            file.write(line)

def read_csv(filename):
    with open(filename, "r", encoding='utf-8') as file:
        data = []
        for line in file:
            line = line.strip()  # удаляем переносы
            row = line.split(',')
            data.append(row)
    return data

def calculate(data):
    total = 0
    for row in data:
        total += float(row[1])
    return total

def find_max(data):
    max_salary = data[0]
    for row in data:
        if float(row[1]) > float(max_salary[1]):
            max_salary = row
    return max_salary

def find_min(data):
    min_salary = data[0]
    for row in data:
        if float(row[1]) < float(min_salary[1]):
            min_salary = row
    return min_salary

def write_file(filename, total, min_salary, max_salary, avg):
    with open(filename, "w", encoding='utf-8') as file:
        file.write(f"Общая сумма {total}\n")
        file.write(f"Минимальная зарплата {min_salary[0]}: {min_salary[1]}\n")  # имя и число
        file.write(f"Максимальная зарплата {max_salary[0]}: {max_salary[1]}\n")
        file.write(F"Средняя зарплата - {avg}")


def main():
    filename = "salary.csv"
    create_random_csv(filename)
    data = read_csv(filename)
    total = calculate(data)
    min_salary = find_min(data)
    max_salary = find_max(data)
    avg = total / len(data)
    write_file("report.txt", total, min_salary, max_salary, avg)

main()