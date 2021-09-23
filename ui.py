
def get_name():
    name=input('name: ')
    return name

def get_country_and_record():
    country = input('country: ')
    record = int(input('number of chainsaws caught: '))
    return country, record

def get_new_record():
    new_record = int(input('number of chainsaws caught: '))
    return new_record

def error_message(name):
    print(f'{name} not in the database')