# Из исходного текстового файла (expansion.txt) выбрать имена фалов,
# соответствующие типам: .xls, .xml, .html, .css, .py. Посчитать количество полученных
# элементов.
import re

extensions = ['xls', 'xml', 'html', 'css', 'py']

pattern = r'\b[\w\-\.]+\.(?:' + '|'.join(extensions) + r')\b'

with open('expansion.txt', 'r', encoding='utf-8') as f:
    content = f.read()

files = re.findall(pattern, content, flags=re.IGNORECASE)

print("Найденные файлы:")
for file in files:
    print(f"  {file}")

print(f"\nКоличество: {len(files)}")