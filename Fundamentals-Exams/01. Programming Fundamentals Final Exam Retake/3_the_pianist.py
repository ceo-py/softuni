number_pieces = int(input())

pieces_info = {}

for piece in range(number_pieces):
    piece_name, *info = input().split("|")
    pieces_info[piece_name] = info


def add_piece(info):
    piece, composer, key = info
    if piece in pieces_info:
        return f"{piece} is already in the collection!"

    pieces_info[piece] = [composer, key]
    return f"{piece} by {composer} in {key} added to the collection!"


def remove_piece(info):
    piece = info[0]
    if piece in pieces_info:
        del pieces_info[piece]
        return f"Successfully removed {piece}!"
    return f"Invalid operation! {piece} does not exist in the collection."


def change_key(info):
    piece, new_key = info
    if piece in pieces_info:
        pieces_info[piece][1] = new_key
        return f"Changed the key of {piece} to {new_key}!"
    return f"Invalid operation! {piece} does not exist in the collection."


def show_result():
    for piece in pieces_info:
        print(f"{piece} -> Composer: {pieces_info[piece][0]}, Key: {pieces_info[piece][1]}")


command_func = {
    "Add": add_piece,
    "Remove": remove_piece,
    "ChangeKey": change_key
}

command = input()
while command != "Stop":
    command_type, *info = command.split("|")
    print(command_func[command_type](info))
    command = input()

show_result()







#
# number_of_pieces = int(input())
#
# music_info = {}
# piece_d, composer_d, key_d = "piece", "composer", "key"
#
#
# def piece_exists(piece_name: str):
#     if piece_name in music_info:
#         return True
#     return False
#
#
# def add_music_info(piece_name: str, composer_name: str, key_name: str, first_input: bool):
#     if piece_exists(piece_name):
#         if not first_input:
#             print(f"{piece_name} is already in the collection!")
#             return
#     if not piece_exists(piece_name):
#         music_info[piece_name] = music_info.get(piece_name, {})
#         music_info[piece_name][key_name] = composer_name
#         if not first_input:
#             print(f"{piece_name} by {composer_name} in {key_name} added to the collection!")
#
#
# def remove_music_info(piece_name: str):
#     if piece_exists(piece_name):
#         del music_info[piece_name]
#         return f"Successfully removed {piece_name}!"
#     return f"Invalid operation! {piece_name} does not exist in the collection."
#
#
# def change_music_info(piece_name: str, key_name: str):
#     if piece_exists(piece_name):
#         _, name_compositor = music_info[piece_name].popitem()
#         music_info[piece_name] = {}
#         music_info[piece_name][key_name] = name_compositor
#         return f"Changed the key of {piece_name} to {key_name}!"
#     return f"Invalid operation! {piece_name} does not exist in the collection."
#
#
# def show_result():
#     for piece_name in music_info:
#         for key, name in music_info[piece_name].items():
#             print(f"{piece_name} -> Composer: {name}, Key: {key}")
#
#
# for _ in range(number_of_pieces):
#     piece_name, composer_name, key_name = input().split("|")
#     add_music_info(piece_name, composer_name, key_name, True)
#
# command = input()
#
# while command != "Stop":
#     command_type, *info = command.split("|")
#     piece_name = info[0]
#     if command_type == "Remove":
#         print(remove_music_info(piece_name))
#     elif command_type == "Add":
#         composer_name = info[1]
#         key_name = info[2]
#         add_music_info(piece_name, composer_name, key_name, False)
#     elif command_type == "ChangeKey":
#         key_name = info[1]
#         print(change_music_info(piece_name, key_name))
#     command = input()
#
# show_result()
#
#
#
#





#
#
#
#
#
# number_of_pieces = int(input())
#
# music_info = {}
# result_info = list()
# piece_d = "piece"
# composer_d = "composer"
# key_d = "key"
#
#
# def add_music_info(piece_name, composer_name, key_name, first_input):
#     if piece_name in music_info:
#         if not first_input:
#             print(f"{piece_name} is already in the collection!")
#     elif piece_name not in music_info:
#         music_info[piece_name] = {}
#         music_info[piece_name][key_name] = composer_name
#         if not first_input:
#             print(f"{piece_name} by {composer_name} in {key_name} added to the collection!")
#
#
# def remove_music_info(piece_name):
#     if piece_name in music_info:
#         del music_info[piece_name]
#         print(f"Successfully removed {piece_name}!")
#     else:
#         print(f"Invalid operation! {piece_name} does not exist in the collection.")
#
#
# def change_music_info(piece_name, key_name):
#     if piece_name in music_info:
#         value = music_info[piece_name].popitem()
#         name_com = value[1]
#         # for key, value in music_info[piece_name].items():
#         #     name_com = value
#         # del music_info[piece_name]
#         music_info[piece_name] = {}
#         music_info[piece_name][key_name] = name_com
#         print(f"Changed the key of {piece_name} to {key_name}!")
#     else:
#         print(f"Invalid operation! {piece_name} does not exist in the collection.")
#
#
# def show_result():
#     for piece_name in music_info:
#         for key, name in music_info[piece_name].items():
#             result_info.append({piece_d: piece_name, composer_d: name, key_d: key})
#     result_info.sort(key=lambda item: (item[piece_d], item[composer_d]))
#     for info_display in result_info:
#         print(f"{info_display[piece_d]} -> Composer: {info_display[composer_d]}, Key: {info_display[key_d]}")
#
#
# for _ in range(number_of_pieces):
#     command = input().split("|")
#     piece_name = command[0]
#     composer_name = command[1]
#     key_name = command[2]
#     add_music_info(piece_name, composer_name, key_name, True)
#
# command = input()
#
# while command != "Stop":
#     command = command.split("|")
#     command_type = command[0]
#     piece_name = command[1]
#     if command_type == "Remove":
#         remove_music_info(piece_name)
#     elif command_type == "Add":
#         composer_name = command[2]
#         key_name = command[3]
#         add_music_info(piece_name, composer_name, key_name, False)
#     elif command_type == "ChangeKey":
#         key_name = command[2]
#         change_music_info(piece_name, key_name)
#     command = input()
#
# show_result()
