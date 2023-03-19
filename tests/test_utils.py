import pytest

from utils import open_json_file, get_executed, sort_executed_of_date, get_print


def test_open_json_file():
    url = 'operations.json'
    assert open_json_file(url)


def test_get_executed(test_data):
    assert len(get_executed(test_data)) == 5
    assert len(get_executed(test_data, filtered_empty_from=True)) == 4


def test_last_data(test_data):
    data = sort_executed_of_date(test_data, count_last_values=2)
    assert data[0]['date'] == '2019-08-26T10:50:58.294041'
    assert len(data) >= 2


def test_get_print(test_data):
    data = get_print(test_data[:1])
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.']
    data = get_print(test_data[3:4])
    assert data == ["23.03.2018 Открытие вклада\n['СКРЫТО']  -> Счет **2431\n48223.05 руб."]
