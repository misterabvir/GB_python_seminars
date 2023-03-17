"""
Задача 20:
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.

А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.

Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
"""

def get_letters_dictionary(l_dict, letters, cost):
    for item in letters.split(', '):
        l_dict[item] = cost
    return l_dict

def get_letters():
    letters = {}
    letters = get_letters_dictionary(letters, 'A, E, I, O, U, L, N, S, T, R', 1)
    letters = get_letters_dictionary(letters, 'D, G', 2)
    letters = get_letters_dictionary(letters, 'B, C, M, P', 3)
    letters = get_letters_dictionary(letters, 'F, H, V, W, Y', 4)
    letters = get_letters_dictionary(letters, 'K', 5)
    letters = get_letters_dictionary(letters, 'J, X', 8)
    letters = get_letters_dictionary(letters, 'Q, Z', 10)
    letters = get_letters_dictionary(letters, 'А, В, Е, И, Н, О, Р, С, Т', 1)
    letters = get_letters_dictionary(letters, 'Д, К, Л, М, П, У', 2)
    letters = get_letters_dictionary(letters, 'Б, Г, Ё, Ь, Я', 3)
    letters = get_letters_dictionary(letters, 'Й, Ы', 4)
    letters = get_letters_dictionary(letters, 'Ж, З, Х, Ц, Ч', 5)
    letters = get_letters_dictionary(letters, 'Ш, Э, Ю', 8)
    letters = get_letters_dictionary(letters, 'Ф, Щ, Ъ', 10)
    return letters

def get_points(word, dictionary):
    amount = 0
    for index in range(len(word.strip())):
        amount += dictionary[word[index].upper()]
    return amount

dictionary = get_letters()
word = input('Enter a word for scrabble: ')
cost = get_points(word, dictionary)
print(f'Your word \'{word}\' is worth  {cost}')


"""
OUTPUT========================
Enter a word for scrabble: Enter 
Your word 'Enter ' is worth  5
==============================
Enter a word for scrabble: ноутбук
Your word 'ноутбук' is worth  12
==============================
"""


