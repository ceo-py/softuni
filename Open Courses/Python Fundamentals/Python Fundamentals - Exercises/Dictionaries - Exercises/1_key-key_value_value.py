key_main = input()
value_main = input()
range_to_look = int(input())

show_result = {}

for _ in range(range_to_look):
    string_to_search = input().split(" => ")
    if key_main in string_to_search[0]:
        show_result[string_to_search[0]] = {}
        for value in string_to_search[-1].split(";"):
            if value_main in value:
                show_result[string_to_search[0]][value] = value


def print_result():
    for name in show_result:
        print(f"{name}:")
        for value in show_result[name].keys():
            print(f"-{value}")


print_result()
