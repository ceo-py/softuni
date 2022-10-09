import os

result = {}


def get_directory_files(directory):
    return [x for x in os.listdir(rf"{directory}") if os.path.isfile(rf"{directory}\{x}")]


def save_report(data, directory):
    with open(f"{directory}\\report.txt", "a", encoding="utf-8") as file:
        file.write(data)


def prepare_for_data_for_save(directory):
    files = get_directory_files(directory)
    for file in files:
        extension = file[file.find("."):]
        result[extension] = result.get(extension, []) + [file]
    sorting_data_for_save(directory)


def sorting_data_for_save(directory):  # умишлено е така за да не се налага за всеки ред да се отваря файла на ново !
    data = ""
    for pos, extension in enumerate(sorted(result.keys())):
        if pos > 0:
            data += "\n"
        data += f"{extension}"
        for file in sorted(result[extension]):
            data += "\n"
            data += f"- - - {file}"
    save_report(data, directory)


prepare_for_data_for_save(input())
