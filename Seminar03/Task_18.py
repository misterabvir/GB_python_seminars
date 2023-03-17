"""
Задача 18:
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь вводит натуральное число N – количество элементов в массиве и число, 
которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N.
Выведите, ближайший к X элемент. Если есть несколько элементов, 
которые равноудалены от X, выведите наименьший по величине.
"""
import math
import random

def get_validate_input(message, min, max):
    while not ((data:=input(message)).isdigit()) or not (min <= int(data) <= max):
        print("Wrong input, try again")
    return int(data)

def get_random_list(length, min, max):
    return [random.randint(min, max) for i in range(length)]
     
def get_closest_of_desired(array, number):   
    offset = 1000
    des = array[0]
    for index, item in enumerate(array):
        if index == 0: continue
        if item > number and offset > item - number:
            offset = item - number
            des = item
        elif item <= number and offset >= number - item:
            offset = number - item
            des = item
    return des

max_length = 20
min_length = 10
max_limit = 100
min_limit = 1

length = get_validate_input(F'Enter list length ({min_length}...{max_length}): ', min_length, max_length)
r_list = get_random_list(length, min_limit, max_limit)
desired = get_validate_input(F'Enter desired value ({min_limit}...{max_limit}): ', min_limit, max_limit)
result = get_closest_of_desired(r_list, desired)

print(F'Closest to {desired} in {r_list} is {result}')

"""
OUTPUT==============================================================================
Enter list length (10...20): 15
Enter desired value (1...100): 50
Closest to 50 in [88, 60, 19, 34, 99, 53, 23, 46, 86, 31, 9, 4, 64, 4, 44] is 53
===================================================================================
Enter list length (10...20): 15
Enter desired value (1...100): 25
Closest to 25 in [87, 92, 50, 44, 17, 97, 60, 19, 23, 49, 31, 80, 58, 42, 49] is 23
===================================================================================
"""