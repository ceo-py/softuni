operation = input()
number_one = int(input())
number_two = int(input())


def show_result(type_operation, n_one, n_two):
    if type_operation == "multiply":
        result = n_one * n_two
        return result

    elif type_operation == "divide":
        result = n_one / n_two
        return int(result)

    elif type_operation == "add":
        result = n_one + n_two
        return result

    elif type_operation == "subtract":
        result = n_one - n_two
        return result


print(show_result(operation, number_one, number_two))
