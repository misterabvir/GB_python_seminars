"""
Задача 16:
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь вводит натуральное число N – количество элементов в массиве и число, 
которое необходимо проверить - X. 
Заполните массив случайными натуральными числами от 1 до N/2. 
Выведите, сколько раз X встречается в массиве.
"""

import random

def get_validate_input(message, min, max):
    while not ((data:=input(message)).isdigit()) or not (min <= int(data) <= max):
        print("Wrong input, try again")
    return int(data)

def get_random_list(length, min, max):
    return [random.randint(min, max) for i in range(length)]
     
def get_amount_of_desired(array, number):
    count = 0
    for item in array:
        if item == number:
            count += 1
    return count

max_length = 15
min_length = 5
max_limit = 3
min_limit = 1

length = get_validate_input(F'Enter list length ({min_length}...{max_length}): ', min_length, max_length)
r_list = get_random_list(length, min_limit, max_limit)
desired = get_validate_input(F'Enter desired value ({min_limit}...{max_limit}): ', min_limit, max_limit)
result = get_amount_of_desired(r_list, desired)

print(F'Amount {desired} in {r_list} is {result}')

"""
OUTPUT============================================
Enter list length (5...15): 10
Enter desired value (1...3): 2
Amount 2 in [2, 1, 3, 3, 2, 1, 3, 2, 3, 2] is 4
==================================================
Enter list length (5...15): 10
Enter desired value (1...3): 3
Amount 3 in [1, 3, 2, 2, 3, 2, 2, 2, 2, 3] is 3
==================================================
"""