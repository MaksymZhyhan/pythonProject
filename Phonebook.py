import json
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='Name of Phonebook')
args = parser.parse_args()

current_dir = os.path.dirname(os.path.realpath(__file__))
datafile_path = os.path.join(current_dir, (args.file_name + '.json'))

# print(os.path.exists(file_name))
first_phonebook = {}
if not os.path.exists(datafile_path):
    with open(datafile_path, 'w') as file:
        json.dump(first_phonebook, file)

else:
    with open(datafile_path, 'r') as file:
        second_phonebook = json.load(file)
        print(second_phonebook)


def show_all():
    with open(datafile_path, 'r', encoding="UTF-8") as book:
        print(book.read())


# Add new entries
def add():
    print('Please, enter the details of new contact!')
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    full_name = first_name + " " + last_name
    phone_number = input('Enter phone number: ')
    location = input('Enter city or state: ')

    first_phonebook[phone_number] = {
        'first_name': first_name,
        'last_name': last_name,
        'full_name': full_name,
        'location': location
    }


add()

with open(datafile_path, 'w') as book_file:
    json.dump(first_phonebook, book_file, indent=4)

show_all()
