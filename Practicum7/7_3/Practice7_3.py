"""Прочитать 2 тхт файла. Определить процент совпадения слов.
Подсчитать кол-во уникальных слов в каждом тексте. Создать файл с результатами"""

def read_file(filename):
    with open(filename, "r") as file:
        return file.read().split()

def calculate_similatry(words1, words2):
    common_words = set(words1) & set(words2)
    return len(common_words) / len(set(words1 + words2)) * 100  # процент

def couunt_unique_words(words):
    return len(set(words))

def write_report(filename, similarity, unique_words1, unique_words2):
    with open(filename, "w", encoding='utf-8') as file:
        file.write(f"Процент совпадения: {similarity}\n")
        file.write(f"Уникальных слов в первом тексте: {unique_words1}\n")
        file.write(f"Уникальных слов в втором тексте: {unique_words2}\n")

def main(file1, file2, report_file):
    words1 = read_file(file1)
    words2 = read_file(file2)
    similarity = calculate_similatry(words1, words2)
    unique_words1 = couunt_unique_words(words1)
    unique_words2 = couunt_unique_words(words2)
    write_report(report_file,similarity,unique_words1, unique_words2)

main("file1.txt", "file2.txt", "report_file")