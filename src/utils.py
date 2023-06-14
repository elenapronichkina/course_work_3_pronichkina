import json
from main import latest_operations


def read_json(file_path):
    """
    читает файл json и возвращает его содержимое
    return: данные, список словарей
    """
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data


def sort_data(data: list[dict]) -> list[dict]:
    """
    сортирует данные по статусу операции
    :param data: исходные данные
    :return: отсортированные данные
    """
    sorted_data = []
    for operation in data:
        if operation.get('state') == 'EXECUTED':
            sorted_data.append(operation)

    return sorted_data


def mask_card_number(card_number):
    """
    маскирует цифры номера карты на *
    :param card_number: номер карты
    :return: маскированная строка
    """
    return f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'


def mask_account_number(account_number):
    """
    маскирует цифры номера счета на *
    :param account_number: номер счета
    :return: маскированная строка
    """
    return f"**{account_number[-4:]}"


def modify_date(date):
    """
    меняет формат даты
    :param date: дата операции в исходном формате
    :return: дата в формате ДД.ММ.ГГГГ (14.10.2018)
    """
    new_date = date[0:10]
    list_date = new_date.split("-")
    return f"{list_date[2]}.{list_date[1]}.{list_date[0]}"


def sort_data_by_date(data):
    '''
    сортирует данные по дате операции
    :param data: данные
    :return: отсортированные данные
    '''
    data.sort(key=lambda x: x['date'], reverse=True)
    return data


def print_message_to_user(latest_operations):
    """
    выводит на экран список из 5 последних выполненных клиентом операций в формате:
   <дата перевода> <описание перевода>
   <откуда> -> <куда>
   <сумма перевода> <валюта>
    :param latest_operations: данные по пяти последним операциям
    :return: сообщение для пользователя
    """
    messages = []
    for operation in latest_operations:

        date = operation["date"]
        description = operation["description"]
        card_number = operation.get("from")
        account_number = operation["to"]
        amount = operation["operationAmount"]["amount"]
        currency = operation["operationAmount"]["currency"]["name"]

        date_for_print = modify_date(date)

        if card_number is None:
            operation_from = 'Информация не указана'
            card_name = ''
        elif card_number.split()[0] == 'Счет':
            operation_from = mask_account_number(card_number[-20:])
            card_name = 'Счет'
        else:
            operation_from = mask_card_number(card_number[-16:])
            card_name = card_number[:-17]

    operation_to = mask_account_number(account_number[-20:])

    messages.append(
    f"{date_for_print} {description}\n{card_name} {operation_from} -> Счет {operation_to}\n{amount} {currency}")

    return messages
