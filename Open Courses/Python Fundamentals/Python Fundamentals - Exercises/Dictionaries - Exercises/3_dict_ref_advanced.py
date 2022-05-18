dic_ref = {}

add_keys = input()

while add_keys != "end":
    name_key, values = add_keys.split(" -> ")
    if values[0].isdigit():
        if name_key not in dic_ref:
            dic_ref[name_key] = []
        [dic_ref[name_key].append(num) for num in values.split(", ")]
    else:
        if values in dic_ref:
            dic_ref[name_key] = dic_ref[values].copy()
    add_keys = input()


[print(f"{name} === {', '.join(dic_ref[name])}") for name in dic_ref]









# dic_ref = {}
#
# add_keys = input()
#
# while add_keys != "end":
#     name_key, values = add_keys.split(" -> ")
#     if values[0].isdigit():
#         if name_key not in dic_ref:
#             dic_ref[name_key] = []
#         for num in values.split(", "):
#             dic_ref[name_key].append(num)
#     else:
#         if values in dic_ref:
#             dic_ref[name_key] = dic_ref[values].copy()
#     add_keys = input()
#
#
# def show_results():
#     for name in dic_ref:
#         print(f"{name} === {', '.join(dic_ref[name])}")
#
#
# show_results()
