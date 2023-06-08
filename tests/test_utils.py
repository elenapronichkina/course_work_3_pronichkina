import pytest

from src.utils import read_json, sort_data, modify_date, mask_card_number, mask_account_number


def test_read_json(path_to_test_json, expected_result_read_json_test):
    assert read_json(path_to_test_json) == expected_result_read_json_test


def test_sort_data(data_for_sort, expected_result_for_sort):
    assert sort_data (data_for_sort) == expected_result_for_sort


def test_modify_date(date_for_modify, expected_result_for_date):
    assert modify_date(date_for_modify) == expected_result_for_date

def test_mask_card_number():
    assert mask_card_number("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

def test_mask_account_number():
    assert mask_account_number("Счет 64686473678894779589") == "Счет ***************9589"