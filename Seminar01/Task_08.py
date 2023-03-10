# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

def getValidate(message):
    while (data := input(message)).isdigit() == False or int(data) < 1:
        print('Wrong input, try again')
    return int(data)

m = getValidate('Enter length of the first chocolate side: ')
n = getValidate('Enter length of the second chocolate side: ')
k = getValidate('How many slices do you wanna break off: ')

if k >= m * n: print('No, you wanna too much, you so greedy')
elif k % m == 0 or k % n == 0:  print('OK, you can do this')
else:  print('Sorry, but this is impossible stuff')

'''
OUTPUT ===========================================================================
Enter length of the first chocolate side: 3
Enter length of the second chocolate side: 2
How many slices do you wanna break off: 4
OK, you can do this
OUTPUT ===========================================================================
Enter length of the first chocolate side: 3
Enter length of the second chocolate side: 2
How many slices do you wanna break off: 6
No, you wanna too much, you so greedy
OUTPUT ===========================================================================
Enter length of the first chocolate side: 3
Enter length of the second chocolate side: 2
How many slices do you wanna break off: 1
Sorry, but this is impossible stuff
==================================================================================
'''