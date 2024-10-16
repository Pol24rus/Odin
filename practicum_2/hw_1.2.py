""" Проверка любого числа на что оно кратно """
number = int(input("Введите число, которое надо проверить на кратность\n"))
numbers = []
for num in range(1, number+1):
    if number % num == 0:
        numbers.append(num)
print(f"Число {number} может быть кратноследующим числам: {numbers}")