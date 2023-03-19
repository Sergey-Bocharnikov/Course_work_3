import pytest

from utils import open_json_file, sort_executed_of_date


def test_open_json_file():
    url = 'operations.json'
    assert open_json_file(url)


def test_last_data(test_data):
    data = sort_executed_of_date(test_data, count_last_values=2)
    assert data[0]['date'] == '2019-08-26T10:50:58.294041'
    assert len(data) >= 2
