main_string = input()
command = input()

while command != "Done":
    nothing_to_replace = False
    if "TakeOdd" in command:
        main_string = main_string[1::2]
    else:
        _, index_or_substring, lenght_or_substitute = [int(x) if x.isdigit() else x for x in command.split()]
        if "Cut" in command:
            main_string = main_string[:index_or_substring] + main_string[index_or_substring + lenght_or_substitute:]
        elif "Substitute" in command:
            if index_or_substring in main_string:
                main_string = main_string.replace(index_or_substring, lenght_or_substitute)
            else:
                print("Nothing to replace!")
                nothing_to_replace = True
    if not nothing_to_replace:
        print(main_string)
    command = input()

print(f"Your password is: {main_string}")








#
#
#
# main_string = input()
# command = input()
#
#
# def take_odd_chr(main_string):
#     return "".join(main_string[x] for x in range(len(main_string)) if x % 2 != 0)
#
#
# def cut_string(index, length, main_string):
#     return main_string[:index] + main_string[index + length:]
#
#
# def substitute_string(substring, substitute, main_string):
#     return main_string.replace(substring, substitute)
#
#
# while command != "Done":
#     nothing_to_replace = False
#     if "TakeOdd" in command:
#         main_string = take_odd_chr(main_string)
#     else:
#         _, index_or_substring, lenght_or_substitute = [int(x) if x.isdigit() else x for x in command.split()]
#         if "Cut" in command:
#             main_string = cut_string(index_or_substring, lenght_or_substitute, main_string)
#         elif "Substitute" in command:
#             if index_or_substring in main_string:
#                 main_string = substitute_string(index_or_substring, lenght_or_substitute, main_string)
#             else:
#                 print("Nothing to replace!")
#                 nothing_to_replace = True
#     if not nothing_to_replace:
#         print(main_string)
#     command = input()
#
# print(f"Your password is: {main_string}")
#
#




#
# main_string = input()
# command = input()
#
#
# def take_odd_chr(main_string):
#     result = "".join(main_string[x] for x in range(len(main_string)) if x % 2 != 0)
#     print(result)
#     return result
#
#
# def cut_string(index, length, main_string):
#     result = main_string[:index] + main_string[index + length:]
#     print(result)
#     return result
#
#
# def substitute_string(substring, substitute, main_string):
#     if substring in main_string:
#         result = main_string.replace(substring, substitute)
#         print(result)
#         return result
#     print("Nothing to replace!")
#     return main_string
#
#
# while command != "Done":
#     if "TakeOdd" in command:
#         main_string = take_odd_chr(main_string)
#         command = input()
#         continue
#     _, index_or_substring, lenght_or_substitute = [int(x) if x.isdigit() else x for x in command.split()]
#     if "Cut" in command:
#         main_string = cut_string(index_or_substring, lenght_or_substitute, main_string)
#     elif "Substitute" in command:
#         main_string = substitute_string(index_or_substring, lenght_or_substitute, main_string)
#     command = input()
#
# print(f"Your password is: {main_string}")
#
#
#
#
#







#
#
#
# main_string = input()
#
# command = input()
#
#
# def take_odd():
#     global main_string
#     copy_main_string = main_string[:]
#     main_string = ""
#     for index, char in enumerate(copy_main_string):
#         if index % 2 != 0:
#             main_string += char
#     print(main_string)
#
#
# def cut_string(index, lenght_string):
#     global main_string
#     main_string = main_string[:index] + "" + main_string[index + lenght_string:]
#     print(main_string)
#
#
# def substitute_string(substring, substitute):
#     global main_string
#     if substring in main_string:
#         main_string = main_string.replace(substring, substitute)
#         print(main_string)
#     else:
#         print("Nothing to replace!")
#
#
# while command != "Done":
#     command = command.split()
#     type_command = command[0]
#     if type_command == "TakeOdd":
#         take_odd()
#     elif type_command == "Cut":
#         cut_string(int(command[1]), int(command[-1]))
#     elif type_command == "Substitute":
#         substitute_string(command[1], command[-1])
#     command = input()
#
# print(f"Your password is: {main_string}")
