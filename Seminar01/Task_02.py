# Задача 2: Найдите сумму цифр трехзначного числа.

def getValidate():
    while (data := input('Enter 3-digit number: ')).isdigit() == False or (100 <= int(data) < 1000) == False:
        print('Wrong input, try again')
    return int(data)

def sumOfDigits(data):
    count = 0
    while data != 0:
        count += data % 10
        data //= 10
    return count

number = getValidate()
result = sumOfDigits(number)
print('Sum of digits of', number, 'equal to', result)

'''
OUTPUT ===========================
Enter 3-digit number: F
Wrong input, try again
Enter 3-digit number: 12
Wrong input, try again
Enter 3-digit number: 1111
Wrong input, try again
Enter 3-digit number: 468
Сумма цифр введенного числа: 18
=================================
'''