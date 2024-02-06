from function import load_file, formatter_date, filter_operations, sort_operations, encryption


def main():
    #Загружаем список операций
    operations = load_file("data/operations.json")

    #Сортируем операции по дате
    sort_data = sort_operations(operations, 'date')

    #Фильтруем операции по статусу ВЫПОЛНЕННО
    filter_state = filter_operations(sort_data, 'state', 'EXECUTED')

    #Обрезаем первые пять выполненных операций
    five_operations = filter_state[:5]
    for operation in five_operations:
        if 'from' not in operation:
            operation['from'] = ''

        print(f'{formatter_date(operation["date"])} {operation["description"]}\n'
              f'{encryption(operation["from"], "from")} -> {encryption(operation["to"], "to")}'
              f' -> {operation['operationAmount']['amount']} {operation['operationAmount']["currency"]["name"]}\n')

if __name__ == '__main__':
    main()