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


def sort_executed_of_date(filename, count_last_values):
    """Сортируем по 'date'"""
    date = sorted(filename, key=lambda x: x["date"], reverse=True)
    return date[:count_last_values]
