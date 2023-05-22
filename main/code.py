import json
from datetime import date


with open(r"C:\Users\Денис\PycharmProjects\coursework3\operations.json", "r", encoding="utf-8") as file:
    data = json.load(file)


def all_executed_values(operations):
    """Возвращает список всех выполненных операций"""
    all_executed_state = []
    for i in range(len(operations)):
        if operations[i].get('state') == "EXECUTED":
            all_executed_state.append(operations[i])
    return all_executed_state


def sort_date(operations):
    """Сортировка операций по датам"""
    operations.sort(key=lambda x: x['date'][0:10], reverse=True)
    return operations


def transformation_date(wrong_date):
    """Преобразует дату в нужный формат"""
    true_date = date.fromisoformat(wrong_date[0:10])
    day = str(true_date.day).rjust(2, '0')
    month = str(true_date.month).rjust(2, '0')
    year = true_date.year
    return f"{day}.{month}.{year}"


def change_date(operations):
    """Изменение формата даты непосредственно в списке операций"""
    for i in range(len(operations)):
        operations[i]['date'] = transformation_date(operations[i]['date'])
    return operations


def last_operations(operations):
    """Берем из списка всех операций только 5 последних"""
    required = []
    if len(operations) >= 5:
        for i in range(5):
            required.append(operations[i])
    else:
        for i in range(len(operations)):
            required.append(operations[i])
    return required


def hide_information_from(operations):
    """Скрывает информацию о карте отправителя"""
    result_card_info = ''
    card_info = operations.get("from")
    if card_info is not None:
        info = card_info.split()
        stars_count = len(info[-1]) - 6
        intermediate = stars_count * '*'
        hide_card_number = f"{info[-1][0:4]} {info[-1][4:6]}{intermediate[0:2]}"
        for i in range(stars_count - 6):
            if i % 4 != 0:
                hide_card_number += '*'
            else:
                hide_card_number += ' '
                hide_card_number += '*'
        hide_card_number += ' '
        hide_card_number += f"{info[-1][-4::]}"

        if len(info) == 2:
            result_card_info = info[0] + ' ' + hide_card_number
        elif len(info) == 3:
            result_card_info = info[0] + ' ' + info[1] + ' ' + hide_card_number
    return result_card_info


def hide_information_to(operations):
    """Скрывает информацию о получателе"""
    card_info = operations.get('to').split()
    result_card_info = card_info[0] + ' ' + '**' + card_info[1][-4:]
    return result_card_info


def full_information_about_operation(list_of_operations):
    """Возвращает информацию об успешной операции"""
    for i in range(len(list_of_operations)):
        print(f'''
{list_of_operations[i]['date']} {list_of_operations[i]['description']}
{hide_information_from(list_of_operations[i])} -> {hide_information_to(list_of_operations[i])}
{list_of_operations[i]['operationAmount']['amount']} {list_of_operations[i]['operationAmount']['currency']['name']}''')


executed_values = all_executed_values(data)
sorted_operations_list = sort_date(executed_values)

all_operations = change_date(sorted_operations_list)
required_values = last_operations(all_operations)

full_information_about_operation(required_values)
