"""2. Даны три числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим)."""
try:
    #Ввод значения
    a, b, c = int(input("Введите значение 1\n")), int(input("Введите значение 2\n")), int(input("Введите значение 3\n"))
    #Логика
    if a > b:
        if b > c:
            print(b)
        elif a > c:
            print(c)
        else:
            print(a)
    else:
        if a > c:
            print(a)
        elif b > c:
            print(c)
        else:
            print(b)
except ValueError as e:
    print(e)