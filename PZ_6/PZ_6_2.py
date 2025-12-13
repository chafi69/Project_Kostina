try:
    #Ввод значений
    N = int(input("Длина списка = "))
    R = int(input("Число к которому надо приблизиться = "))
    A = [int(input(f"Значение в списке A[{i}] = ")) for i in range(N)]
    #Нужные параметры
    best_sum = A[0] + A[1]  # начальное приближение
    best_i, best_j = 0, 1
    #Перебор
    for i in range(N):
        for j in range(i + 1, N):
            current_sum = A[i] + A[j]
            if abs(current_sum - R) < abs(best_sum - R):
                best_sum = current_sum
                best_i, best_j = i, j

    # Вывод в порядке возрастания индексов
    if best_i < best_j:
        print(A[best_i], A[best_j])
    else:
        print(A[best_j], A[best_i])
except ValueError as e:
    print(e)