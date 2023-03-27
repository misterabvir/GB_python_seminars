# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

origin = [random.randint(-10, 10) for _ in range(random.randint(2, 10))]
print(F'You have: {origin}')
minimum = int(input('Enter min: '))
maximum = int(input('Enter max: '))

result = []

for index, item in enumerate(origin):
    if minimum <= item <= maximum:
        result.append(index)

print(f'result: {result}')

'''
OUTPUT=================================
Enter min: 1
Enter max: 6
result: [0, 1]
=======================================
You have: [-7, 1, 4, 3, -5, 7, -3]
Enter min: -5
Enter max: 5
result: [1, 2, 3, 4, 6]
=======================================
'''