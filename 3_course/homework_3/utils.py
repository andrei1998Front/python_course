import json
from datetime import datetime


def convert_to_list(data_list):
    converted_list = []

    for item in data_list:
        converted_list.append(item.as_dict())

    return converted_list


def install_date(data_list, name_attr_list):
    for row in data_list:
        for name_attr in name_attr_list:
            if row[name_attr] is None:
                row[name_attr] = None
                continue

            row[name_attr] = datetime.strptime(row[name_attr], '%m/%d/%Y').date()

    return data_list


def get_data_from_json(path):

    with open(path, "r", encoding="utf-8") as connection:

        data_dict = json.load(connection)

        orders_date_keys = ['start_date', 'end_date']
        orders = install_date(data_dict['orders'], orders_date_keys)

        return {
            "users": data_dict['users'],
            "orders": orders,
            "offers": data_dict['offers']
        }
