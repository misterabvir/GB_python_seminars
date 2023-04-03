import json

FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
SECOND_NAME = 'second_name'
PHONE = 'phone'
ID = 'id'
PEOPLE = 'people'

class PhoneBook():
    def __init__(self, path):
        self.path = path
        self.data:dict = self.read()
       
    def read(self):
        with open(self.path, 'r') as data:
            return json.load(data)

    def save(self):
        with open(self.path, 'w') as data:
            json.dump(self.data, data)

    def append(self):
        person = {}
        person[ID] = self.data[ID] = self.data[ID] + 1
        person[LAST_NAME] = input('Enter last name: ')
        person[FIRST_NAME] = input('Enter first name: ')
        person[SECOND_NAME] = input('Enter second name: ')
        person[PHONE] = input('Enter phone: ')
        self.data[PEOPLE].append(person)
        self.save()

    def print_all(self):
        for person in self.data[PEOPLE]:
            self.print_concrete(person)

    def print_concrete(self, person):
        print(f'{person[ID]}, {person[FIRST_NAME]} {person[SECOND_NAME]} {person[LAST_NAME]}, {person[PHONE]}')

    def find(self, substring:str):
        for person in self.data[PEOPLE]:
            if substring in person[FIRST_NAME] or substring in person[SECOND_NAME] or substring in person[LAST_NAME]:
                self.print_concrete(person)

    def delete(self, id:int):
        for person in self.data[PEOPLE]:           
            if person[ID] == id:             
                self.data[PEOPLE].remove(person)
                self.save()

    def change(self, id:int):
        for person in self.data[PEOPLE]:           
            if person[ID] == id:
                name = input(f'Enter last name ("{person[LAST_NAME]}" enter empty for keep): ')             
                if name != '': person[LAST_NAME] = name
                name = input(f'Enter first name ("{person[FIRST_NAME]}" enter empty for keep): ')             
                if name != '': person[FIRST_NAME] = name
                name = input(f'Enter second name ("{person[SECOND_NAME]}" enter empty for keep): ')             
                if name != '': person[SECOND_NAME] = name
                phone = input(f'Enter phone ("{person[PHONE]}" enter empty for keep): ')             
                if phone != '': person[PHONE] = phone
                self.save()
                

def welcome():
    print()
    print('Welcome!', 'Super Phone Book')
    print('1. Print all entries')    
    print('2. Append new entry ')    
    print('3. Find entry ')    
    print('4. Delete entry  by id') 
    print('5. Change entry  by id')
    print('6. Exit')
    print()

def main():
    book = PhoneBook('phones.json') 
    while True:
        welcome()    
        command = input('> ')
        if command == '1':
            book.print_all()
        elif command == '2':
            book.append()
        elif command == '3':
            substring = input('Enter what you want to search for (search by name): ')
            book.find(substring)
        elif command == '4':
            id = int(input('Enter the ID of the person you want to remove: '))
            book.delete(id)
        elif command == '5':
            id = int(input('Enter the ID of the person you want to change: '))
            book.change(id)
        elif command == '6':
            break
        else: print('Invalid input, please try again\n', '\r>')

main()

"""
OUTPUT ===========================================
Welcome! Super Phone Book
1. Print all entries
2. Append new entry
3. Find entry
4. Delete entry by id
5. Change entry by id
6. Exit

# READ
> 1
3, John K Macferson, 111-222-333
4, Smith S Smithson, 333-222-111
5, Mac M Donald, 999-999-777
7, Ivan Ivanovich Ivanov, 555-777-999

# CREATE
> 2
Enter last name: Petr
Enter first name: Peter
Enter second name: P
Enter phone: 444-111-888

> 1 
3, John K Macferson, 111-222-333
4, Smith S Smithson, 333-222-111
5, Mac M Donald, 999-999-777
7, Ivan Ivanovich Ivanov, 555-777-999
8, Peter P Petr, 444-111-888

# SEARCH
> 3
Enter what you want to search for (search in names): Petr
8, Peter P Petr, 444-111-888

# DELETE
> 4
Enter the ID of the person you want to remove: 7  

> 1
3, John K Macferson, 111-222-333
4, Smith S Smithson, 333-222-111
5, Mac M Donald, 999-999-777
8, Peter P Petr, 444-111-888

# UPDATE
> 5
Enter the ID of the person you want to change: 5
Enter last name ("Donald" enter empty for keep): MacDonald
Enter first name ("Mac" enter empty for keep): Trumpoid
Enter second name ("M" enter empty for keep): J
Enter phone ("999-999-777" enter empty for keep):

> 1
3, John K Macferson, 111-222-333
4, Smith S Smithson, 333-222-111
5, Trumpoid J MacDonald, 999-999-777
8, Peter P Petr, 444-111-888
"""