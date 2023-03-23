# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.


def sum(a:int, b:int)->int:
    if a == 0: 
        return b
    return int(sum(a - 1, b + 1))

first_number = float(input('Enter first number: '))
second_number = float(input( 'Enter second number: '))

result = sum(first_number,second_number)
print(f'result: {result}')

"""
OUTPUT==========================
Enter first number: 45
Enter second number: 15
result: 60
================================
Enter first number: 12
Enter second number: 33
result: 45
================================
"""