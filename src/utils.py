import json
import datetime
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
        if operation['state'] == 'EXECUTED':
            sorted_data.append(operation)

    return sorted_data

def mask_card_number(card_number):
    """
    маскирует цифры номера карты на *
    :param card_number: номер карты
    :return: маскированная строка
    """
    for operation in data:
        card_number = operation['from']
        mask_card = card_number[0:14] + '*' * len(card_number[15:-4]) + card_number[-4:]
        return mask_card[:12], mask_card[13:17], mask_card[-9:-5], mask_card[-4:]
#        print(mask_card[:12], mask_card[13:17], mask_card[-9:-5], mask_card[-4:])
# "from": "Maestro 1596837868705199"


def mask_account_number(account_number):
    """
    маскирует цифры номера счета на *
    :param account_number: номер счета
    :return: маскированная строка
    """
    for operation in data:
        account_number = operation['to']
        return account_number[0:5] + '*' * len(account_number[6:-4]) + account_number[-4:]
#       print(account_number[0:5] + '*' * len(account_number[6:-4]) + account_number[-4:])
# "to": "Счет 64686473678894779589"
#mask_account_number()
#
# def modify_date(date):
#      """меняет формат даты
#      :param date: дата операции в исходном формате
#      :return: дата в формате ДД.ММ.ГГГГ (14.10.2018)
#     """
#
#      # dt_string = "2019-08-26T10:50:58.294041"
#      # dt_str = dt_string[0:10]
#      # # dt_str_reversed = ''.join(reversed(dt_str))
#      # dt_modify = datetime.strptime(dt_str, "%d %m %Y")
#
# #     for operation in data:
#      #     date = operation['date']
# #           modify_date = date.strftime('%d.%m.%Y')
# #           print (modify_date)
# #     return modify_date
#     pass
#
# def sort_data_by_date(data):
#     '''
#     сортирует данные по дате операции
#     :param date: дата операции
#     :return: отсортированные данные'''
#      data.sort(key=lambda x: x['date'], reversed=True)
#      return data
#      sorted_data_for_date = []
#       for operation in data:
#         #operation['date']
#         sorted_data_for_date.append(operation)
#         return sorted_data_for_date
#     pass
#
