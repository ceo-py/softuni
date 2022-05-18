data_input = input()
while data_input != "end":
    find_text_to_replace = False
    if "<a" in data_input:
        index_find_start = data_input.find("<a")
        find_text_to_replace = True
    if "</a>" in data_input:
        index_find_end = data_input.find("</a>")
    if find_text_to_replace:
        result = f"{data_input[:index_find_start]}{'[URL'}{data_input[index_find_start + 2:index_find_end]}{'[/URL]'}"
        tag_ = result.rfind(">")
        data_input = f"{result[:tag_]}{']'}{result[tag_+1:]}"
    print(data_input)
    data_input = input()
