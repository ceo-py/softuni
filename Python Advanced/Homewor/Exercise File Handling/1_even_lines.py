def open_file():
    with open("text.txt", "r") as file:
        return file.read()


def replace_elements(data):
    for element in ["-", ",", ".", "!", "?"]:
        data = data.replace(element, "@")
    return data.split("\n")[::2]


def show_result():
    list_to_print = replace_elements(open_file())
    [print(*list_to_print[row].split()[::-1]) for row in range(len(list_to_print))]


show_result()
