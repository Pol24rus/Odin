"""перебираем числа пока не найдем четное. for: else:"""
# numbers = [1, 3, 5, 7, 9]
#
# for num in numbers:
#     if num % 2 == 0:
#         print("В списке есть чётное число")
#         break
#     else:
#         print("В списке нет четного числа ")

def contains_digit(s):
    for char in s:
        if char.isdigit():
            print("В строке есть цифры")
            break
        else:
            print("В списке нет цифр ")

contains_digit("Hello world 12345")
# contains_digit("Hello")  # не содержит

