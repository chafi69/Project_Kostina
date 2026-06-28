# Организовать словарь avto, содержащий 3 ключа (марки авто) и списки из трех
# моделей в качестве значений. Обеспечить отображение вторых моделей по каждому
# авто, всех моделей словаря
avto = {
    "Toyota": ["Camry", "Corolla", "RAV4"],
    "BMW": ["X5", "3 Series", "5 Series"],
    "Mercedes": ["E-Class", "C-Class", "S-Class"]
}

print("Вторые модели каждого авто:")
for marka, models in avto.items():
    print(f"{marka}: {models[1]}")  

print("Все модели словаря:")
for marka, models in avto.items():
    print(f"\n{marka}:")
    for model in models:
        print(f"  - {model}")