try:
    #Ввод значений
    N = int(input("Длина списка = "))
    A = [int(input(f"Значение в списке A[{i}] = ")) for i in range(N)]
    #Нужные параметры
    first = A[0]

    # Ищем позицию для вставки первого элемента
    pos = 0
    for i in range(1, N):
        if A[i] > first:
            pos = i
            break
    else:
        pos = N  # если все элементы меньше первого

    # Сдвигаем элементы и вставляем первый на нужное место
    for i in range(pos - 1):
        A[i] = A[i + 1]
    A[pos - 1] = first

    print(A)
except ValueError as e:
    print(e)