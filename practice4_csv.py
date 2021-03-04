import csv

with open('csv_dummy.csv', 'r', encoding='utf-8') as f:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    reader = csv.DictReader(f, fields, delimiter=';')

    for row in reader: #<<<<<<<<<< как  исключить первую строку при обходе?
        print(row)


user_list = [
                {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
                {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
                {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
            ]

fields = ['name', 'age', 'job']

with open('export.csv', 'w', encoding='utf-8-sig', newline='') as f: #<<<<<< не пишет в utf-8 :( Почему нужно использовать utf-8-sig?
    
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)


