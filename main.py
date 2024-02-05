from function import load_file, formatter_date, filter_operations, sort_operations, encryption


def main():
    #Загружаем список операций
    operations = load_file("data/operations.json")

    #Сортируем операции по дате
    sort_data = sort_operations(operations)

    #Фильтруем операции по статусу ВЫПОЛНЕННО
    filter_state = filter_operations(sort_data)

    #Обрезаем первые пять выполненных операций
    five_operations = filter_state[:5]
    for operations in five_operations:
        if 'from' not in operations:
            operations['from'] = ''

        print(f'{formatter_date(operations["date"])} {operations["description"]}\n'
              f'{encryption(operations["from"], "from")} -> {encryption(operations["to"], "to")}'
              f' {operations['operationAmount']['amount']} {operations['operationAmount']["currency"]["name"]}\n')

if __name__ == '__main__':
    main()