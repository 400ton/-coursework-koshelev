import json
import os.path


def load_file(filename) -> list:
    '''Функция загрузки информации из файла'''
    file_path = os.path.join(filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def sort_operations(operations, key):
    """Функция сортировки операции по ключу"""
    if not operations:
        return []
    return sorted(operations, key=lambda operation: operation.get(key, '0000-00-00'), reverse=True)


def filter_operations(operations, key, value):
    '''Функция фильтрации операций по паре ключ == значению'''
    if not operations:
        return []
    return list(filter(lambda operation: operation.get(key) == value, operations))


def formatter_date(date):
    '''Функция форматирования даты'''
    date = date.split('T')[0].split('-')
    return f'{date[2]}.{date[1]}.{date[0]}'


def encryption(data, key):
    '''Функция шифровки номеров номеров и платежных карт'''
    if data == '':
        return ''

    value_number = data.rsplit(' ', 1)
    value = value_number [0: len(value_number) -1]
    number = value_number[-1]

    if key == "from":
        encryption_key = number[0: 4] + ' ' + number[4: 6]+ '** **** ' + number[-4:]
    elif key == "to":
        encryption_key = '**' + number[-4:]
    return ' '.join([*value, encryption_key])
