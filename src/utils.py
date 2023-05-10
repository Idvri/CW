import json
from operator import itemgetter
import re


def get_operations(file):
    """Функция для форматирования данных операций из файла с ними в формате json под формат проекта"""
    with open(file, 'r', encoding='utf-8') as operations:
        operations_from_file = json.loads(operations.read())
        return operations_from_file


def get_executed_operations(operations_list):
    """Функция для получения выполненых операций"""
    executed_operations = list()
    for operation in operations_list:
        if len(operation) > 0 and operation['state'] == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations


def get_last_five_operations(operations_list):
    "Функция для получения 5 последних операций"""
    operations_list.sort(key=itemgetter('date'))
    last_five_operations = list()
    for operation in reversed(operations_list[-5:]):
        last_five_operations.append(operation)
    return last_five_operations


def get_date_of_operation(operation):
    "Функция для корректного отображения даты"""
    date = operation["date"][:10].replace("-", ".")
    date = '.'.join(reversed(date.split('.')))
    return date


def get_information_of_operation(operation):
    """Функция для маскировки счетов"""
    nums = ''.join(re.findall(r'\d+', operation))
    name_of_card = ''.join(re.findall(r'\D+', operation))
    if nums[16:20]:
        nums = nums.replace(nums[6:-4], '**********')
        nums = ''.join([nums[14:20]])
        return f'{name_of_card}{nums}'
    else:
        nums = nums.replace(nums[6:-4], '******')
        nums = ' '.join([nums[:4], nums[4:8], nums[8:12], nums[12:16]])
        return f'{name_of_card}{nums}'
