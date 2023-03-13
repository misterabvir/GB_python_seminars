# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

import math
S = int(input('S = '))
P = int(input('P = '))

'''
| x + y = S
| x * y = P

| x  + P / x = S
| x ^ 2 + P - S * x = 0
| x ^ 2 - S * x + P = 0

D = S * S - 4 * 1 * P = S^2 - 4*P

D > 0
x1 = (S + sqrt(D)) / (2 * P), y1 = s - x1
x2 = (S + sqrt(D)) / (2 * P), y2 = s - x2

D = 0
x = S / (2 * P), y = S - x

D < 0 ERORR
'''

D = S * S - 4 * P
if D == 0:
    x = S / 2
    y = S - x
    if x.is_integer() and y.is_integer():
        print(f'x = {int(x)}  y = {int(y)}')
    else: 
        print('Don\'t have solution in integers')
elif D > 0:
    x1 = (S - math.sqrt(D)) / 2
    x2 = (S + math.sqrt(D)) / 2
    y1 = S - x1
    y2 = S - x2
    if x1.is_integer() and y1.is_integer():
        print(f'x = {int(x1)}  y = {int(y1)}')
    elif x2.is_integer() and y2.is_integer():
        print(f'x = {int(x1)}  y = {int(y1)}')
    else:
       print('Don\'t have solution in integers') 
else: 
    print('Don\'t have solution in integers')


'''
OUTPUT=========
S = 2
P = -3
x = -1  y = 3
==============
S = 20
P = 99
x = 9  y = 11
==============
S = -19
P = 70
x = -14  y = -5
==============
'''
