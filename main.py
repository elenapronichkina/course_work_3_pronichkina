from src.utils import read_json, sort_data, sort_data_by_date, mask_card_number, mask_account_number

if __name__ == '__main__':
    #прочитать данные
    read_json()

    #отсортировать данные по статусу
    sort_data()

    # отсортированные по статусу данные (sorted_data []) отсортировать по дате
    sort_data_by_date()

    #взять последние 5 операций:
    latest_operations = sort_data_by_date [-5:-1]

    for operations in latest_operations:
        date = operation["date"]
        description = operation["description"]
        card_number = operation["from"]
        account_number = operation["to"]
        amount = operation["operationAmount"]["amount"]
        currency = operation["operationAmount"]["currency"]["name"]

        #привести дату к формату ДД.ММ.ГГГГ
        date_for_print = modify_date(date)

        #маскировка номера карты (откуда)
        operation_from = mask_card_number(card_number)

        #маскировка номера счета (куда)
        operation_to = mask_account_number(account_number)

#    print(< дата перевода > < описание перевода > < откуда > -> < куда > < сумма перевода > < валюта > "\n")
        print(f"{date_for_print}, {description}, {operation_from}, '->', {operation_to}, {amount}, {currency} \n")

