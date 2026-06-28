# Имеется список студентов группы, в котором все имена различны. Определить, есть ли в
# группе студент, который побывал в гостях у всех студентов. (Для каждого студента
# составить список из множества побывавших у него в гостях друзей, причем хозяина в этот
# список не включать)

anna = {"Борис", "Вика"}
boris = {"Анна", "Вика", "Дима"}
vika = {"Анна", "Борис", "Дима"}
dima = {"Борис", "Вика"}


vse_studenty = {"Анна", "Борис", "Вика", "Дима"}

for student in vse_studenty:
    if student == "Анна":
        byl_v_gostyah = all(student in g for g in [boris, vika, dima])
    elif student == "Борис":
        byl_v_gostyah = all(student in g for g in [anna, vika, dima])
    elif student == "Вика":
        byl_v_gostyah = all(student in g for g in [anna, boris, dima])
    else:  
        byl_v_gostyah = all(student in g for g in [anna, boris, vika])
    
    if byl_v_gostyah:
        print(f"{student} побывал у всех")
        break
else:
    print("Нет такого")