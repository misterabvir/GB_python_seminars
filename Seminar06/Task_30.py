# Задача 30:
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

start = int(input('Start: '))
step  = int(input('Step : '))
count = int(input('Count: '))
stop = start + count * step

result = [item for item in range(start, stop, step)]
print(f'result: {result}')

"""
OUTPUT=================================
Start: 7
Step : 2
Count: 5
result: [7, 9, 11, 13, 15]
=======================================
Start: 4
Step : 6
Count: 8
result: [4, 10, 16, 22, 28, 34, 40, 46]
=======================================
"""