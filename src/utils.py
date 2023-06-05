import json
def read_json(file_path):
    """
    читает файл json и возвращает его содержимое
    return: данные, список словарей
    """
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data

def sort_data(data):
    """
    сортирует данные по статусу операции
    :param data: исходные данные
    :return: отсортированные данные
    """
    pass

def mask_card_number(card_number):
    """
    маскирует цифры номера карты на *
    :param card_number: номер карты
    :return: маскированная строка
    """
    pass

def mask_account_number(account_number):
    """маскирует цифры номера счета на *
    :param account_number: номер счета
    :return: маскированная строка"""
    pass

