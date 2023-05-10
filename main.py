from src.utils import get_operations, get_executed_operations, get_last_five_operations, get_date_of_operation, \
    get_information_of_operation


def main():
    """Основной код виджета"""
    operations = get_operations('data/operations.json')
    executed_operations = get_executed_operations(operations)
    last_five_operations = get_last_five_operations(executed_operations)
    for operation in last_five_operations:
        if 'from' in operation.keys():
            print(f"{get_date_of_operation(operation)} {operation['description']}\n"
                  f"{get_information_of_operation(operation['from'])} -> "
                  f"{get_information_of_operation(operation['to'])}\n"
                  f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")
        else:
            print(f"{get_date_of_operation(operation)} {operation['description']}\n"
                  f"{get_information_of_operation(operation['to'])}\n"
                  f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")


main()
