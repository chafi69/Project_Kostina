import sqlite3 as sq
from datetime import datetime

insurance_data = [
    ("2024-01-15", 500000.00, "Автострахование", 3.5, "Центральный"),
    ("2024-01-20", 1000000.00, "Страхование жизни", 2.8, "Северный"),
    ("2024-02-10", 750000.00, "Недвижимость", 4.0, "Центральный"),
    ("2024-02-18", 300000.00, "Автострахование", 3.5, "Южный"),
    ("2024-03-05", 1200000.00, "Страхование жизни", 2.8, "Западный"),
    ("2024-03-12", 450000.00, "Недвижимость", 4.0, "Северный"),
    ("2024-04-02", 600000.00, "Автострахование", 3.5, "Центральный"),
    ("2024-04-15", 2000000.00, "Страхование жизни", 2.5, "Восточный"),
    ("2024-05-01", 350000.00, "Недвижимость", 4.2, "Южный"),
    ("2024-05-10", 850000.00, "Автострахование", 3.5, "Западный")
]

with sq.connect('insurance.db') as con:
    cursor = con.cursor()

    cursor.execute("DROP TABLE IF EXISTS Договор")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Договор (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_start TEXT NOT NULL,
        sum_insurance REAL NOT NULL,
        insurance_type TEXT NOT NULL,
        rate REAL NOT NULL,
        branch TEXT NOT NULL
    )""")

    cursor.executemany("INSERT INTO Договор VALUES (NULL, ?, ?, ?, ?, ?)", insurance_data)

    def print_table(title_text):
        print('\n')
        print(title_text)
        print(f"{'ID':<4} {'Дата':<12} {'Страховая сумма':<18} {'Вид страхования':<22} {'Ставка':<8} {'Филиал':<15}")
        cursor.execute("SELECT * FROM Договор")
        for row in cursor.fetchall():
            id, date_s, sum_ins, ins_type, rate, branch = row
            print(f"{id:<4} {date_s:<12} {sum_ins:<18.2f} {ins_type:<22} {rate:<8.2f} {branch:<15}")

    print_table("Исходное содержимое таблицы Договор")

    print("\n\n")
    print("ОПЕРАЦИИ ПОИСКА")

    print("\n1. Поиск договоров со страховой суммой более 800 000 руб.:")
    cursor.execute("SELECT id, date_start, sum_insurance, insurance_type, branch FROM Договор WHERE sum_insurance > 800000")
    for row in cursor.fetchall():
        print(f"   ID {row[0]}: {row[1]} - {row[2]:.2f} руб. ({row[3]}) - {row[4]}")

    print("\n2. Поиск договоров по виду страхования 'Автострахование':")
    cursor.execute("SELECT id, date_start, sum_insurance, rate, branch FROM Договор WHERE insurance_type = 'Автострахование'")
    for row in cursor.fetchall():
        print(f"   ID {row[0]}: {row[1]} - {row[2]:.2f} руб., ставка {row[3]}%, {row[4]}")

    print("\n3. Поиск договоров в Центральном филиале с датой после 01.02.2024:")
    cursor.execute("SELECT id, date_start, sum_insurance, insurance_type FROM Договор WHERE branch = 'Центральный' AND date_start > '2024-02-01'")
    for row in cursor.fetchall():
        print(f"   ID {row[0]}: {row[1]} - {row[2]:.2f} руб. ({row[3]})")

    print("\n\n")
    print("ОПЕРАЦИИ РЕДАКТИРОВАНИЯ")

    cursor.execute("UPDATE Договор SET rate = rate + 0.5 WHERE branch = 'Южный'")
    print("\n1. Увеличена тарифная ставка на 0.5% для Южного филиала")

    cursor.execute("UPDATE Договор SET sum_insurance = sum_insurance * 1.1 WHERE insurance_type = 'Страхование жизни'")
    print("2. Увеличена страховая сумма на 10% для договоров 'Страхование жизни'")

    cursor.execute("UPDATE Договор SET rate = rate * 0.9 WHERE branch = 'Центральный' AND sum_insurance > 600000")
    print("3. Снижена ставка на 10% для Центрального филиала с суммой > 600 000 руб.")

    print_table("Таблица после проведения 3-х операций редактирования")

    print("\n\n")
    print("ОПЕРАЦИИ УДАЛЕНИЯ")

    cursor.execute("DELETE FROM Договор WHERE sum_insurance < 400000")
    print("\n1. Удалены договоры со страховой суммой менее 400 000 руб.")

    cursor.execute("DELETE FROM Договор WHERE branch = 'Западный' AND insurance_type = 'Автострахование'")
    print("2. Удалены договоры 'Автострахование' в Западном филиале")

    cursor.execute("DELETE FROM Договор WHERE date_start < '2024-02-01'")
    print("3. Удалены договоры, заключённые до 01.02.2024")

    print_table("Итоговая таблица после проведения 3-х операций удаления")

    print("\n\n")
    print("СТАТИСТИКА ПО ФИЛИАЛАМ")
    cursor.execute("""
        SELECT branch, 
               COUNT(*) as count_contracts, 
               SUM(sum_insurance) as total_sum,
               AVG(sum_insurance) as avg_sum,
               AVG(rate) as avg_rate
        FROM Договор 
        GROUP BY branch
        ORDER BY total_sum DESC
    """)
    
    print(f"{'Филиал':<15} {'Кол-во':<10} {'Общая сумма':<18} {'Средняя сумма':<18} {'Средняя ставка':<15}")
    for row in cursor.fetchall():
        branch, count_c, total, avg_sum, avg_rate = row
        print(f"{branch:<15} {count_c:<10} {total:<18.2f} {avg_sum:<18.2f} {avg_rate:<15.2f}")