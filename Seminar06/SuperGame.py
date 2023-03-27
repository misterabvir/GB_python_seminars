# Крестики-нолики

#1 печатаем поле
#2 просим ввести число
#3 если свободно вводим Х - печатаем поле
#4 проверяем нет ли выигрыша
#5 если нет АИ вводит число случайно - вводим О - печатаем поле
#6 проверяем нет ли выигрыша
#7 если нет -> идем в #2
#8 результаты

import random

def display(field:list):
    print(f'+---+---+---+')
    print(f'| {field[0]} | {field[1]} | {field[2]} |')
    print(f'+---+---+---+')
    print(f'| {field[3]} | {field[4]} | {field[5]} |')
    print(f'+---+---+---+')
    print(f'| {field[6]} | {field[7]} | {field[8]} |')
    print(f'+---+---+---+')

def get_user_input(field:list):
    # введено число
    # в диапазоне 1...9
    # ячейка свободна
    number = ''
    while (not (number:= input('Take your move: ')).isdigit() \
            or not int(number) in range(1, 10)) \
            and str(field[int(number) - 1]).isdigit():
        print('Try again')
    return int(number)

def get_ai_input(field:list):
    number = random.randint(0,8)
    while  not str(field[number]).isdigit():
        number = random.randint(0,8)
    return number

def is_over(field:list)->bool:
    if field[0] == field[1] and field[1] == field[2]: return True
    if field[3] == field[4] and field[4] == field[5]: return True
    if field[6] == field[7] and field[7] == field[8]: return True
    if field[0] == field[3] and field[3] == field[6]: return True
    if field[1] == field[4] and field[4] == field[7]: return True
    if field[2] == field[5] and field[5] == field[8]: return True
    if field[6] == field[4] and field[4] == field[2]: return True
    if field[0] == field[4] and field[4] == field[8]: return True
    return False

def main():
    field = [str(item+ 1)  for item in range(9)]
    while True:
        display(field)
        user_move = get_user_input(field)
        field[user_move - 1] = 'X'
        display(field)
        if is_over(field): 
            print('you win')
            break
        ai_move = get_ai_input(field)    
        field[ai_move] = 'O'
        print(f'AI moved to: {ai_move + 1}')
        if is_over(field): 
            print('you loose')
            break

main()
