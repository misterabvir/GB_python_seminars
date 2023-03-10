# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

def getValidate():
    while (data := input('Enter amount of paper cranes: ')).isdigit() == False or (int(data) % 6 == 0) == False:
        print('Wrong or impossible input (the amount must be a multiple of 6), please try again')
    return int(data)

amount = getValidate()

resultPeter = amount // 6
resultSergei = amount // 6 
resultKaty = amount // 3 * 2

print('Peter made', resultPeter, 'of the paper cranes')
print('Katy made', resultKaty, 'of the paper cranes')
print('Sergei made', resultSergei, 'of the paper cranes')

'''
OUTPUT ===========================================================
Enter amount of paper cranes: 49
Wrong or impossible input (amount must be multiple 6), try again
Enter amount of paper cranes: 48
Peter made 8 of the paper cranes
Katy made 32 of the paper cranes
Sergei made 8 of the paper cranes
==================================================================
'''