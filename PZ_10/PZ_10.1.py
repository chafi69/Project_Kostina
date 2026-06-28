# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Среднее арифметическое элементов:
# Последовательность, в которой каждый последующий элемент равен квадрату суммы двух
# соседних элементов:
import random

numbers = [random.randint(-20, 20) for _ in range(10)]  

with open("numbers.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(map(str, numbers)))

with open("numbers.txt", "r", encoding="utf-8") as f:
    data = list(map(int, f.read().split()))

count = len(data)
avg = sum(data) / count

new_seq = []
for i in range(count):
    if i == 0:
        new_seq.append((data[i+1]) ** 2)
    elif i == count - 1:
        new_seq.append((data[i-1]) ** 2)
    else:
        new_seq.append((data[i-1] + data[i+1]) ** 2)

with open("processed_numbers.txt", "w", encoding="utf-8") as f:
    f.write("Исходные данные:\n")
    f.write(" ".join(map(str, data)) + "\n")
    f.write(f"Количество элементов: {count}\n")
    f.write(f"Среднее арифметическое элементов: {avg:.2f}\n")
    f.write("Последовательность, в которой каждый последующий элемент "
            "равен квадрату суммы двух соседних элементов:\n")
    f.write(" ".join(map(str, new_seq)) + "\n")

print("Файлы созданы: numbers.txt и processed_numbers.txt")