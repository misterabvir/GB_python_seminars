# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет "счастливость" билета.

def getValidate():
    while (data := input('Enter ticket number: ')).isdigit() == False or (100000 <= int(data) < 1000000) == False:
        print('Wrong or impossible input (the number must be have of 6 digits), please try again')
    return int(data)

def sumOfDigits(data):
    sum = 0
    while data != 0:
        sum += data % 10
        data //= 10
    return sum

number = getValidate()
sumOfFirst3Digits = sumOfDigits(number // 1000)
sumOfLast3Digits = sumOfDigits(number % 1000)

if sumOfFirst3Digits == sumOfLast3Digits:
    print('Congrats you have a lucky ticket')
else:
    print('Sorry, your ticket is not lucky')


'''
OUTPUT ===========================================================================
Enter ticket number: wrong
Wrong or impossible input (the number must be have of 6 digits), please try again
Enter ticket number: 12345
Wrong or impossible input (the number must be have of 6 digits), please try again
Enter ticket number: 1234567
Wrong or impossible input (the number must be have of 6 digits), please try again
Enter ticket number: 456159
Congrats you have a lucky ticket
OUTPUT ===========================================================================
Enter ticket number: 321098 
Sorry, your ticket is not lucky
==================================================================================
'''