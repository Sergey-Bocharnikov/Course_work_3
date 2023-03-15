import json


def open_json_file(filename):
    """В аргументы попадет ссылка 'operations.json' с файлом json
    выводит список операций в Python"""
    with open(filename, "rt", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_executed(filename):
    """Выводим список выполненных "EXECUTED" операций"""
    executed_file = []
    for items in filename:
        if items["state"] == "EXECUTED":
            executed_file.append(items)
    return executed_file


def get_data_for_sort(x):
    """Функция которая принимает ключ и выводит значение по ключу.
    Нужно для следующей функции sort_executed_of_date"""
    return x['date']


def sort_executed_of_date(filename):
    """Сортируем по 'date' и выводим 5 последних операций"""
    return sorted(filename, key=get_data_for_sort, reverse=True)
