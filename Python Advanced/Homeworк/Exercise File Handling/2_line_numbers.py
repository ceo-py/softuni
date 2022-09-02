import string


def open_file():
    with open("text.txt", "r", encoding="utf-8") as file:
        return file.read().split("\n")


def write_file(info):
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(info))


def count_letters(text):
    return sum([1 for x in text if x.isalpha()])


def count_punctuation(text):
    return sum([text.count(symbol) for symbol in string.punctuation])


def show_result():
    data = open_file()
    data_to_save_in_file = []
    for pos, row in enumerate(range(len(data)), 1):
        letters_ = count_letters(data[row])
        punctuation_ = count_punctuation(data[row])
        data_to_save_in_file.append(f"Line {pos}: {data[row]} ({letters_})({punctuation_})")
    write_file(data_to_save_in_file)


show_result()
