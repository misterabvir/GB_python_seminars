## Задача 26: 
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def pow(number:float, power:int)-> float: 
    if power < 0: 
        power *= -1
        number = 1 / number
    if power == 1 : return number
    return number * pow(number, power - 1)

number = float(input('Enter number: '))
power = float(input( 'Enter  power: '))

result = pow(number, power)
print(f'result: {result}')

"""
OUTPUT==========================
Enter your number: 2
Enter your power: -3
result: 0.125
================================
Enter your number: 2  
Enter your power: 10
result: 1024.0
================================
"""