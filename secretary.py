import requests

print(requests.__version__)

print('Start secretary.py')
# import requests
# import os
# import data
from package_data.config import NAME, PASSWORD
from package_data.data import documents, directories


class Secretary:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def get_name_by_number(self):
        number = input('Введите номер документа: ')
        for doc in documents:
            if doc['number'] == number:
                print('{0}'.format(doc['name']))
                break
        else:
            print('Отсутствуют документы с таким номером')

    def get_documents(self):
        for doc in documents:
            print('{0} "{1}" "{2}"'.format(doc['type'], doc['number'], doc['name']))
        for key, values in directories.items():
            print(key, '->', values)

    def get_directory_by_number(self):
        number = input('Введите номер документа: ')
        for directory, list_docs in directories.items():
            if number in list_docs:
                print('Документ с номером {0} находится на полке {1}'.format(number, directory))
                break
        else:
            print('Отсутствуют документы с таким номером')

    def add_document(self):
        number = input('Введите номер документа:')
        name = input('Введите имя и фамилию:')
        doc_type = input('Введите тип документа:')
        directoryNumber = input('Введите номер полки:')
        if number and name and doc_type and directoryNumber:
            documents.append({"type": doc_type, "number": number, "name": name})
            if directoryNumber in directories:
                directories[directoryNumber].append(number)
            else:
                directories[directoryNumber] = [number]
        else:
            print('ВНИМАНИЕ! Введены не все данные')


def main():
    secretary = Secretary(NAME, PASSWORD)
    print('Доброе утро', secretary.name)
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            secretary.get_name_by_number()
        if command == 'l':
            secretary.get_documents()
        if command == 's':
            secretary.get_directory_by_number()
        if command == 'a':
            secretary.add_document()
        if command == 'e':
            break

print('__name__ ->', __name__)
if __name__ == '__main__':
    main()
    print('End secretary.py')