# Задача 10:
# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random
amount = int(input('Enter amount of coin: '))
coins = [random.randint(0, 1) for _ in range(amount)]
heads = sum(coins)
tail = amount - heads
print(coins)
result = heads if heads < tail else tail
if result > 0:
    print(f'We have to flip {result} coin')
else:
    print('We don\'t have to do anything')

'''
OUTPUT=======================================
Enter amount of coin: 10
[1, 1, 0, 0, 1, 0, 0, 1, 1, 1]
We have to flip 4 coin
=============================================
Enter amount of coin: 15
[1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1]
We have to flip 5 coin
=============================================
Enter amount of coin: 2
[0, 0]
We don't have to do anything
=============================================
'''
