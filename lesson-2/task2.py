"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров —
товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    """
    :param item: item
    :param quantity: quantity
    :param price: price
    :param buyer: buyer
    :param date: date
    :return: None
    """

    with open('orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders.json', 'w', encoding='utf-8') as f_in:
        orders_list = data['orders']
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        }
        orders_list.append(order_info)
        json.dump(data, f_in, indent=4)


if __name__ == '__main__':
    write_order_to_json('Computer', 10, 435, 'Dmitriy', '2020-10-12')
    write_order_to_json('Mouse', 15, 2356, 'Ivan', '2021-09-25')
    write_order_to_json('Keyboard', 54, 2454, 'Danil', '2022-01-29')
