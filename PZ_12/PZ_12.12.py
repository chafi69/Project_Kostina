# В матрице элементы кратные 3 увеличить в 3 раза.
# 2. В матрице найти среднее арифметическое элементов последних двух столбцов
from random import randint

rows = int(input("Количество строк: "))
cols = int(input("Количество столбцов: "))

matrix = [[randint(1, 20) for _ in range(cols)] for _ in range(rows)]

print("\nИсходная матрица:")
[print(row) for row in matrix]

matrix = list(map(lambda row: list(map(lambda x: x * 3 if x % 3 == 0 else x, row)), matrix))

print("\nМатрица после изменений:")
[print(row) for row in matrix]

if cols >= 2:
    last_two_cols = list(map(lambda row: row[-2:], matrix))
    all_elements = [num for row in last_two_cols for num in row]
    avg = sum(all_elements) / len(all_elements) if all_elements else 0
    print(f"\nСреднее арифметическое последних двух столбцов: {avg:.2f}")
else:
    print("\nВ матрице меньше двух столбцов")