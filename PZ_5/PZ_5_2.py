try:
    #Сама функция
    def PowerA234(A, B, C, D):
        B = A ** 2
        C = A ** 3
        D = A ** 4
        return B, C, D

    # Пример использования
    A = float(input("Введите значение:  "))
    B = C = D = 0
    #Записывание значений в переменные
    B, C, D = PowerA234(A, B, C, D)
    #Вывод степеней
    print(f"A = {A}")
    print(f"A^2 = {B}")
    print(f"A^3 = {C}")
    print(f"A^4 = {D}")
except ValueError as e:
    print(e)