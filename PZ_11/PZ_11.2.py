# Составить генератор (yield), который преобразует все буквенные символы в
# строчные
def lowercase_generator(strings):
    for s in strings:
        yield ''.join(map(str.lower, s))

strrr = 'strstrstrstrSTRSTRSTRS'
print(list(lowercase_generator(strrr)))