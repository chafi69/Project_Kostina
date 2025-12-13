# Ввод данных (пример: можно заменить на статичные значения для тестирования)
X_input = input("Введите вещественное число X: ")
N_input = input("Введите целое положительное число N (> 0): ")
# Используем try-except для обработки ошибок ввода
try:
    X = float(X_input)
    N = int(N_input)
    # Проверка условия задачи N > 0
    if N <= 0:
        print("Ошибка: N должно быть целым положительным числом (> 0).")
    else:
        sum_series = 0
        for i in range(N + 1):
            # Вычисление факториала N! вручную в цикле
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            # Вычисление члена ряда
            if factorial == 0:  # Обработка случая i=0, 0! = 1
                term = X ** i
            else:
                term = (X ** i) / factorial
            sum_series += term
        print(f"\nПриближенное значение exp({X}) для N={N}: {sum_series}")
except ValueError as e:
    print(e)