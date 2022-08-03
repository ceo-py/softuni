last_ticket = False
student_tickets = 0
standard_tickets = 0
kid_tickets = 0


while not last_ticket:
    movie_name = input()
    if movie_name == "Finish":
        break
    movie_tickets = int(input())
    ticket_number_for_current_movie = 0
    for ticket in range(movie_tickets):
        ticket_type = input()
        if ticket_type == "kid":
            kid_tickets += 1
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "End":
            break
        elif ticket_type == "Finish":
            last_ticket = True
            break
        ticket_number_for_current_movie += 1
    print(f"{movie_name} - {((ticket_number_for_current_movie / movie_tickets) * 100):.2f}% full.")

total_tickets = student_tickets + standard_tickets + kid_tickets
total_student_tickets = (student_tickets / total_tickets) * 100
total_standard_tickets = (standard_tickets / total_tickets) * 100
total_kid_tickets = (kid_tickets / total_tickets) * 100
print(f"Total tickets: {total_tickets}")
print(f"{total_student_tickets:.2f}% student tickets.")
print(f"{total_standard_tickets:.2f}% standard tickets.")
print(f"{total_kid_tickets:.2f}% kids tickets.")




# movie_name = input()
# new_name = movie_name
# moive_theater_info = {}
# student_tickets = 0
# standart_tickets = 0
# kids_tickets = 0
# total_tickets = 0
# number_check = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# data = ""
# while True:
#     if data == "Finish":
#         break
#     data = input()
#     if data == "End":
#         data = input()
#         moive_theater_info[data] = 0
#     elif data[0] in number_check:
#         number_tickets = int(data)
#         moive_theater_info[new_name] = data
#         for ticket in range(number_tickets + 1):
#             if ticket == number_tickets:
#                 moive_theater_info[new_name] = (ticket / number_tickets) * 100
#                 data = input()
#                 new_name = data
#                 break
#             else:
#                 ticket_type = input()
#             if ticket_type == "Finish":
#                 data = "Finish"
#                 moive_theater_info[new_name] = (ticket / number_tickets) * 100
#                 break
#             elif ticket_type == "End":
#                 moive_theater_info[new_name] = (ticket / number_tickets) * 100
#                 data = input()
#                 if data == "Finish":
#                     break
#                 else:
#                     moive_theater_info[data] = 0
#                     new_name = data
#                 break
#             elif ticket_type == "student":
#                 student_tickets += 1
#
#             elif ticket_type == "standard":
#                 standart_tickets += 1
#             else:
#                 kids_tickets += 1
#
# total_tickets = standart_tickets + student_tickets + kids_tickets
# total_studend = (student_tickets / total_tickets) * 100
# total_stantard = (standart_tickets / total_tickets) * 100
# total_kid = (kids_tickets / total_tickets) * 100
# for movie, capacity in moive_theater_info.items():
#     print(f"{movie} - {capacity:.2f}% full.")
# print(f"Total tickets: {total_tickets}")
# print(f"{total_studend:.2f}% student tickets.")
# print(f"{total_stantard:.2f}% standard tickets.")
# print(f"{total_kid:.2f}% kids tickets.")
