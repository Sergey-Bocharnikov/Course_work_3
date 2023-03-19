import pytest

from utils import open_json_file


def test_open_json_file():
    url = 'operations.json'
    assert open_json_file(url)
