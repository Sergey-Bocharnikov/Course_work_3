import utils

FILEJSON = 'operations.json'
COUNT_LAST_VALUES = 5
pj_file = utils.open_json_file(FILEJSON)
FILTERED_EMPTY_FROM = True

""" Задаем переменные:
    - file_executed - список операций выполненных (EXECUTED),оставляем операции в которых есть 'from';
    - file_sort_date - выводит 5 последних операций, отсортированных по дате;"""

file_executed = utils.get_executed(pj_file, FILTERED_EMPTY_FROM)
file_sort_date = utils.sort_executed_of_date(file_executed, COUNT_LAST_VALUES)


def get_print(filename):
    """ Выводим данные в заданном формате задачи:
        14.10.2018 Перевод организации
        Visa Platinum 7000 79** **** 6361 -> Счет **9638
        82771.72 руб."""
    text_file_print = []
    for items in filename:
        s_1 = items['date']
        s_2 = items['description']

        s_3 = items['from'].split()
        s_3_int = s_3.pop(-1)
        s_3_int = f"{s_3_int[:4]} {s_3_int[4:6]}** **** {s_3_int[-4:]}"
        s_3_info = " ".join(s_3)

        s_4 = f"**{items['to'][-4:]}"

        s_5 = items['operationAmount']['amount']
        s_6 = items['operationAmount']['currency']['name']

        file_str = f"{s_1[8:10]}.{s_1[5:7]}.{s_1[0:4]} {s_2}\n{s_3_info} {s_3_int} -> Счет {s_4}\n{s_5} {s_6}"

        text_file_print.append(file_str)

    for item in text_file_print:
        print(f"{item}\n")


get_print(file_sort_date)
