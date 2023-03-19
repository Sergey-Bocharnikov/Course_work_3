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


def get_print(filename):
    """ Выводим данные в заданном формате задачи:
        14.10.2018 Перевод организации
        Visa Platinum 7000 79** **** 6361 -> Счет **9638
        82771.72 руб."""
    text_file_print = []
    for items in filename:
        s_1 = items['date']
        s_2 = items['description']

        if "from" in items:
            s_3 = items['from'].split()
            s_3_int = s_3.pop(-1)
            s_3_int = f"{s_3_int[:4]} {s_3_int[4:6]}** **** {s_3_int[-4:]}"
            s_3_info = " ".join(s_3)
        else:
            s_3_int = ""
            s_3_info = ["СКРЫТО"]

        s_4 = f"**{items['to'][-4:]}"

        s_5 = items['operationAmount']['amount']
        s_6 = items['operationAmount']['currency']['name']

        file_str = f"{s_1[8:10]}.{s_1[5:7]}.{s_1[0:4]} {s_2}\n{s_3_info} {s_3_int} -> Счет {s_4}\n{s_5} {s_6}"

        text_file_print.append(file_str)
    return text_file_print
    #for item in text_file_print:
        #print(f"{item}\n")
