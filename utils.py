import json


def open_json_file(filename):
    """В аргументы попадет ссылка 'operations.json' с файлом json
    выводит список операций в Python"""
    with open(filename, "rt", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_executed(data, filtered_empty_from=False):
    """Выводим список выполненных "EXECUTED" операций;
    оставляем операции в которых есть 'from' """
    data = [x for x in data if "state" in x and x["state"] == 'EXECUTED']
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def sort_executed_of_date(filename, count_last_values):
    """Сортируем по 'date'"""
    date = sorted(filename, key=lambda x: x["date"], reverse=True)
    return date[:count_last_values]
