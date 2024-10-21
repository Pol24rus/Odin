"""Прочитать несколькол тхт файлов, объединить содержимое.
Записать рез-т в новый файл. Вывести кол-во объединенных строк"""

def read_files(filenames):
    all_lines = []
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            all_lines.extend(file.readlines())
    return all_lines

def write_files(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

def main(output_files, input_files):
    combined_lines = read_files(input_files)
    write_files(output_files, combined_lines)
    print((f"Объединено строк {len(combined_lines)}"))

input_files = ["file1.txt", "file2.txt"]

main("combinet.txt", input_files)