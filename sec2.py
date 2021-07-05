from secretary import Secretary


if __name__ == '__main__':
    secretary = Secretary('Jhon', 'qwerty')
    print('good morning', secretary.name)
    secretary.get_documents()