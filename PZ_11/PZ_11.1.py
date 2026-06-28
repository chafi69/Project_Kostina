# В последовательности на n целых элементов найти произведение элементов
# средней трети.
from functools import reduce

def product_of_middle_third(seq):
    n = len(seq)
    if n < 3:
        return None
    
    start = n // 3
    end = 2 * n // 3
    
    middle_third = seq[start:end]
    
    product = reduce(lambda x, y: x * y, middle_third, 1)
    
    return product


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(product_of_middle_third(numbers))  