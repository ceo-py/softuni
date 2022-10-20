def start_spring(**kwargs):
    result, output = {}, []
    for value, key in kwargs.items():
        result[key] = result.get(key, []) + [value]
    for s_key, s_value in sorted(result.items(), key= lambda x: (-len(x[1]), x[0])):
        output.append(f"{s_key}:")
        for p_value in sorted(s_value):
            output.append(f"-{p_value}")

    return '\n'.join(output)



#
# def start_spring(**kwargs):
#     output, result = "", {}
#     for value, key in kwargs.items():
#         result[key] = result.get(key, []) + [value]
#     for p_key, p_value in sorted(result.items(), key=lambda x: (-len(x[1]), x[0])):
#         output += f"{p_key}:\n"
#         for type_ in sorted(p_value):
#             output += f"-{type_}\n"
#     return output
#




# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
#
# print(start_spring(**example_objects))


#
# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))








example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))