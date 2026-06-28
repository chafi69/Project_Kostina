# Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме выведя строки в обратном порядке.
# Знаки пунктуации вручную (без import string)
punctuation_marks = '''!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
with open("text18-18.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

total_punct = 0

for i in range(min(4, len(lines))):
    punct_count = sum(1 for ch in lines[i] if ch in punctuation_marks)
    total_punct += punct_count
    print(f"Строка {i+1}: {punct_count} знаков пунктуации")

print(f"\nВсего в первых 4 строках: {total_punct}\n")

print("Содержимое файла text18-18.txt:")
for line in lines:
    print(line.rstrip())


with open("reversed_poem.txt", "w", encoding="utf-8") as f:
    for line in reversed(lines):
        f.write(line)

print("\nСоздан файл reversed_poem.txt со строками в обратном порядке.")