from collections import deque

name = input()

supermarket_line = deque()


def customers_to_paid():
    for person in range(len(supermarket_line)):
        print(f"{supermarket_line.popleft()} ")

    # while supermarket_line:
    #     print(f"{supermarket_line.popleft()} ")


while name != "End":
    if name == "Paid":
        customers_to_paid()
    else:
        supermarket_line.append(name)
    name = input()


print(f"{len(supermarket_line)} people remaining.")



# data_input = input()
# people_in_q = []
# while data_input != "End":
#     if data_input == "Paid":
#         [print(x) for x in people_in_q]
#         people_in_q.clear()
#         data_input = input()
#         continue
#     people_in_q.append(data_input)
#     data_input = input()
#
# print(f"{len(people_in_q)} people remaining.")