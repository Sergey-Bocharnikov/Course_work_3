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

file_print = utils.get_print(file_sort_date)

for item in file_print:
    print(f"{item}\n")
