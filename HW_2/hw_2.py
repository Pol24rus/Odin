"""заметки; Создавать заметки; Просматривать; Удалять заметку"""
from datetime import datetime

# ввожу дату и время, чтобы получить уникальность сообщения
input_time = datetime.now().replace(microsecond=0)

def create_note():
    note_text = input("Введите текст заметки: ")
    with open("My_notes.txt", "a", encoding='utf-8') as file:  # добавляет данные в конец файла не удаляя предыдущие
        file.write("Заметка от " + str(input_time) + " ==> " + note_text + '\n')
        # вместо ==> можно ввести любой текст, запрос
        file.close()
    print("Заметка сохранена ")


def view_notes():
    try:
        with open("My_notes.txt", "r", encoding='utf-8') as file:
            notes = file.readlines()
            if not notes:
                print("Заметок пока нет")
            else:
                print("Список заметок:")
                display_notes(notes)

    except FileNotFoundError:
        print("Файл с заметками не найден. Создайте новую заметку")


def display_notes(notes):  # создаю нумерацию заметок в выводе
    for i in range(1, len(notes) + 1):
        note = notes[i - 1]
        print(f"{i}.{note}")


def personal_notes():  # просмотр выбранной заметки
    try:
        with open("My_notes.txt", "r", encoding='utf-8') as file:
            notes = file.readlines()

        if not notes:
            print("Заметок пока нет")
            return

        note_number = int(input("Введите номер заметки для детального просмотра: "))
        if 1 <= note_number <= len(notes):
            print(notes[note_number - 1])

        else:
            print("Некорректный номер заметки")

    except FileNotFoundError:
        print("Файл с заметками не найден. Создайте новый заметку")
    except ValueError:
        print("Введите корректное число")


def main_menu():
    while True:
        print("\n======Меню=======")
        print("1. Создать заметку")
        print("2. Просмотр всех заметок")
        print("3. Просмотр конкретной заметки")
        print("0. Выход")

        choice = input("Выберите (0-3): ")

        if choice == '1':
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == '3':
            personal_notes()
        elif choice == "0":
            print("Программа завершена")
            break
        else:
            print("Некорректный ввод. Пожалуйста выведите номер от 0 до 3")


main_menu()
