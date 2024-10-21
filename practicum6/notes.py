"""заметки; Создавать заметки; Просматривать; Удалять заметку"""

def create_note():
    note_text = input("Введите текст заметки: ")
    with open("notes.txt", "a", encoding='utf-8') as file:
        file.write(note_text + '\n')
        file.close()
    print("Заметка сохранена ")

def view_notes():
    try:
        with open("notes.txt", "r", encoding='utf-8') as file:
            notes = file.readlines()
            if not notes:
                print("Заметок пока нет")
            else:
                print("Список заметок")
                display_notes(notes)

    except FileNotFoundError:
        print("Файл с заметками не найден. Создайте новую")

def display_notes(notes):
    for idx in range(1, len(notes) + 1):
        note = notes[idx - 1]
        print(f"{idx}.{note}")

def delete_notes():
    try:
        with open("notes.txt", "r", encoding='utf-8') as file:
            notes = file.readlines()
        if not notes:
            print("Заметок пока нет")
            return

        print("Список заметок для удаления")
        display_notes(notes)

        note_number = int(input("Введите номер заметок для удаления: "))
        if 1 <= note_number <= len(notes):
            del notes[note_number - 1]
            with open("notes.txt", "w", encoding='utf-8') as file:
                file.writelines(notes)
            print("Заметка удалена")
        else:
            print("Неколрректный номер заметки")

    except FileNotFoundError:
        print("Файл с заметками не найден. Создайте новый заметку")
    except ValueError:
        print("Введите корректное число")



def main_menu():

    while True:
        print("\n======Меню=======")
        print("1. Создать заметку")
        print("2. Просматривать заметку")
        print("3. Удалить заметку")
        print("0. Выход")

        choice = input("Выберите (0-3): ")

        if choice == '1':
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == '3':
            delete_notes()
        elif choice == "0":
            print("Программа завершена")
            break
        else:
            print("Некорректный ввод. Пожалуйста выведите опцию от 0 до 3")


main_menu()
