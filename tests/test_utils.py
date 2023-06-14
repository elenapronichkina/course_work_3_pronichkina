import pytest

from src.utils import read_json, sort_data, modify_date, mask_card_number, mask_account_number, sort_data_by_date, \
    print_message_to_user

def test_read_json(path_to_test_json, expected_result_read_json_test):
    assert read_json(path_to_test_json) == expected_result_read_json_test


def test_sort_data(data_for_sort, expected_result_for_sort):
    assert sort_data(data_for_sort) == expected_result_for_sort


def test_modify_date(date_for_modify, expected_result_for_date):
    assert modify_date(date_for_modify) == expected_result_for_date


def test_mask_card_number():
    assert mask_card_number("1596837868705199") == "1596 83** **** 5199"


def test_mask_account_number():
    assert mask_account_number("64686473678894779589") == "**9589"


def test_sort_by_date(expected_result_read_json_test, expected_result_for_sort_by_date):
    assert sort_data_by_date(expected_result_read_json_test) == expected_result_for_sort_by_date

def test_print_message_to_user(expected_result_for_sort):
    assert print_message_to_user(expected_result_for_sort) == [
        '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.']
    assert print_message_to_user([
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "to": "Счет 64686473678894779589"
        }
    ]) == ['26.08.2019 Перевод организации\n Информация не указана -> Счет **9589\n31957.58 руб.']
    assert print_message_to_user([
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 64686473678894779589"
        }
    ]) == ['26.08.2019 Перевод организации\nСчет **6952 -> Счет **9589\n31957.58 руб.']
