import psycopg2
from config import data
import csv

conn = psycopg2.connect(**data)
conn.autocommit = True
cursor = conn.cursor()


def create_user(name, surname, phone_number):
    query = f"""
    Insert Into phone_book (name, surname, phone_number)
    Values ('{name}', '{surname}','{phone_number}')
    """
    try:
        cursor.execute(query)
        print('\n\n\nUser succesfully added\n\n\n')
    except:
        print('\n\n\nSomething went wrong\n\n\n')


def read_user():
    print('By what parameter do u want to find user\n[N]ame | [S]urname | [P]hone number')
    action = input()
    if action == 'N':
        name = input('Insert the name: ')
        query = f"""
        Select * from phone_book
        where name='{name}'
        """
        cursor.execute(query)
    elif action == 'S':
        surname = input('Insert the surname: ')
        query = f"""
        Select * from phone_book
        where surname='{surname}'
        """
        cursor.execute(query)
    elif action == 'P':
        phone_number = input('Insert the phone_number: ')
        query = f"""
        Select * from phone_book
        where phone_number='{phone_number}'
        """
        cursor.execute(query)
    else:
        print('\n\n\nPlease insert N S or P')
        read_user()

    response = cursor.fetchone()

    if (response == None):
        print('This user is not exists')
        return tuple()

    print('\n\n\n')

    print(f'id:           {response[0]}')
    print(f'name:         {response[1]}')
    print(f'surname:      {response[2]}')
    print(f'phone_number: {response[3]}')

    print('\n\n\n')

    return response


def show_users():
    query = '''
    SELECT * FROM phone_book
    '''
    cursor.execute(query)
    users = cursor.fetchall()
    for i in users:
        print(f'id:           {i[0]}')
        print(f'name:         {i[1]}')
        print(f'surname:      {i[2]}')
        print(f'phone_number: {i[3]}')
        print('\n')
    print('\n\n')


def update_person():
    response = read_user()
    if (len(response) == 0):
        return
    new_name = input('Enter new name:         ')
    new_surname = input('Enter new surname:      ')
    new_phone_number = input('Enter new phone number: ')

    query = f"""
    UPDATE phone_book
    set name='{new_name}', surname='{new_surname}', phone_number='{new_phone_number}'
    where id={response[0]}
    """

    cursor.execute(query)
    print('\n\n\nUser updated\n\n\n')


def delete_user():
    response = read_user()
    if (len(response) == 0):
        return

    query = f"""
    DELETE FROM phone_book where id={response[0]}
    """
    cursor.execute(query)
    print('\n\n\nPerson has been deleted\n\n\n')


def upload_from_csv():
    with open('users.csv', 'r') as read_file:
        file = csv.reader(read_file)
        for i in file:
            name, surname, phone_number = i[0], i[1], i[2]
            create_user(name, surname, phone_number)


while True:
    print('[C]reate | [R]ead | [L]ist | [U]pdate | [D]elete | [UP]load data from CSV | [E]xit')
    action = input()

    if action == 'C':
        name = input('Insert the name: ')
        surname = input('Insert the surname: ')
        phone_number = input('Insert the phone_number: ')
        create_user(name, surname, phone_number)
    elif action == 'R':
        read_user()
    elif action == 'L':
        show_users()
    elif action == 'U':
        update_person()
    elif action == 'D':
        delete_user()
    elif action == 'UP':
        upload_from_csv()
    elif action == 'E':
        break

cursor.close()
conn.close()