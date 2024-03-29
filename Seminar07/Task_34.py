'''
Задача 34:
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
'''
vowels = ['а', 'я', 'о', 'ё', 'э', 'е', 'ы', 'и', 'у', 'ю']
good_phrase = 'па-ра-ра рам-пам-па ра-па-дам ра-рам-па'
bad_phrase = 'па-ра-рам пам-ра-рам па-пам па-ра-па-дам'

def check(phrase):
    counts = list(map(lambda word: len(list(filter(lambda item: item in vowels, word))), phrase.split()))
    return all(item == counts[0] for item in counts)


print(f'{good_phrase} -> {check(good_phrase)}')
print(f'{bad_phrase} -> {check(bad_phrase)}')

# OUTPUT ==========================================
# па-ра-ра рам-пам-па ра-па-дам ра-рам-па -> True
# па-ра-рам пам-ра-рам па-пам па-ра-па-дам -> False
# ==================================================