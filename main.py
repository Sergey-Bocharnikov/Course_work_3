import utils
FILEJSON = 'operations.json'
pj_file = utils.open_json_file(FILEJSON)

"""Задаем переменные:
    - file_executed - список операций выполненных (EXECUTED);
    - file_sort_date - операции отсортированные по дате;
    - file_sort_date_5 - выводит 5 последних операций"""
file_executed = utils.get_executed(pj_file)
file_sort_date = utils.sort_executed_of_date(file_executed)
file_sort_date_5 = file_sort_date[:5]


def get_date_and_operation_amount(filename):
    """ Выводим данные в заданном формате задачи:
        14.10.2018 Перевод организации"""
    for items in filename:
        s_1 = items['date']
        s_2 = items['description']
        file_str = f"{s_1[8:10]}.{s_1[5:7]}.{s_1[0:4]} {s_2}"
        return file_str


#print(get_date_and_operation_amount(file_sort_date_5))


def get_from_to(filename):
    """ Выводим данные в заданном формате задачи:
        Visa Platinum 7000 79** **** 6361 -> Счет **9638"""
    file_str = []
    for items in filename:
        s_3 = items['from']
        s_3[-5:-10] = '******'

        s_4 = items['to']
        s_4[-5:-20] = '**'

        file_str.append(f"{s_3} -> {s_4}")

    return file_str


#print(get_from_to(file_sort_date_5))


def get_amount_name(filename):
    """ Выводим данные в заданном формате задачи:
        82771.72 руб."""
    for items in filename:
        s_5 = items['operationAmount']['amount']
        s_6 = items['operationAmount']['currency']['name']
        file_str_2 = f"{s_5} {s_6}"
    return file_str_2


#print(get_amount_name(file_sort_date_5))


def get_print(filename):
    """ Выводим данные в заданном формате задачи:
        14.10.2018 Перевод организации
        Visa Platinum 7000 79** **** 6361 -> Счет **9638
        82771.72 руб."""
    text_file_print = []
    for items in filename:
        s_1 = items['date']
        s_2 = items['description']
        s_5 = items['operationAmount']['amount']
        s_6 = items['operationAmount']['currency']['name']
        file_str = f"{s_1[8:10]}.{s_1[5:7]}.{s_1[0:4]} {s_2}\n{s_5} {s_6}"
        text_file_print.append(file_str)
    for item in text_file_print:
        print(f"{item}\n")


get_print(file_sort_date_5)
