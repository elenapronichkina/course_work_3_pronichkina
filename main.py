
from src.utils import read_json, sort_data, sort_data_by_date, print_message_to_user

if __name__ == '__main__':

    raw_data = read_json('src/operations.json')

    sorted_data = sort_data(raw_data)

    date_sorted_data = sort_data_by_date(sorted_data)

    latest_operations = date_sorted_data[:5]

    for message in print_message_to_user(latest_operations):
        print(message, end='\n\n')

