from collections import deque

name = input()

supermarket_line = deque()


def customers_to_paid():
    for person in range(len(supermarket_line)):
        print(f"{supermarket_line.popleft()} ")


while name != "End":
    if name == "Paid":
        customers_to_paid()
    else:
        supermarket_line.append(name)
    name = input()

else:
    print(f"{len(supermarket_line)} people remaining.")
