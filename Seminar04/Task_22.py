# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

# input stuff
n = int(input('Enter size of first set: '))
m = int(input('Enter size of second set: '))

# getting list
n_list = [random.randint(n // 2, n * 2) for _ in range(n)]
m_list = [random.randint(m // 2, m * 2) for _ in range(m)]

# make unique
n_unique = set(n_list)
m_unique = set(m_list)

# make intersection
result = [item for item in n_unique.intersection(m_unique)]

# make sort
result.sort()

# answer
print('first:', n_list)
print('second:', m_list)
print('result:', result)


"""
OUTPUT========================================
Enter size of first set: 10
Enter size of second set: 10
first: [11, 6, 10, 20, 18, 9, 16, 18, 15, 17]
second: [10, 13, 12, 19, 7, 8, 12, 16, 16, 13]
result: [10, 16]
==============================================
"""