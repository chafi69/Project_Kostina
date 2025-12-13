import random

try:
    # Сама функция
    def main():
        a = random.randint(1000, 9999)
        n1 = a // 1000
        n2 = (a // 100) % 10
        n3 = (a % 100) // 10
        n4 = a % 10

        # Проверка
        if n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
            return f"Число {a}: есть одинаковые цифры"
        else:
            return f"Число {a}: все цифры разные"


    # Вывод
    print(main())
except ValueError as e:
    print(e)