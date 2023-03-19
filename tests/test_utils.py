import pytest

from utils import open_json_file


def test_open_json_file():
    url = 'operations.json'
    data = open_json_file(url)
    print(data)
