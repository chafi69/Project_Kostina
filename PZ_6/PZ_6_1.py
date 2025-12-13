try:
    #Ввод
    A = [int(input(f"A[{i}] = ")) for i in range(10)]
    #Логика
    result_index = 0
    for i in range(9, -1, -1):  # идем с конца
        if A[0] < A[i] < A[9]:
            result_index = i + 1  # +1 для порядкового номера
            break
    #Вывод
    print(result_index)
except ValueError as e:
    print(e)