from collections import deque


chocolate = [int(x) for x in input().split(",")]
cups_of_milk = deque(int(x) for x in input().split(","))

successfully_made_milkshakes = 0

while chocolate and cups_of_milk and successfully_made_milkshakes != 5:
    current_chocolate = chocolate.pop()
    current_cup = cups_of_milk.popleft()

    if current_chocolate <= 0 and current_cup <= 0:
        continue
    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup)
        continue
    elif current_cup <= 0:
        chocolate.append(current_chocolate)
        continue
    if current_chocolate == current_cup:
        successfully_made_milkshakes += 1
    else:
        cups_of_milk.append(current_cup)
        chocolate.append(current_chocolate - 5)

if successfully_made_milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")



#
# from collections import deque
#
#
# chocolate = [int(x) for x in input().split(",")]
# cups_of_milk = deque(int(x) for x in input().split(","))
#
# successfully_made_milkshakes = 0
#
# while chocolate and cups_of_milk:
#     current_chocolate = chocolate[-1]
#     current_cup = cups_of_milk[0]
#     if current_chocolate <= 0:
#         del chocolate[-1]
#         continue
#     if current_cup <= 0:
#         del cups_of_milk[0]
#     elif current_chocolate != current_cup:
#         cups_of_milk.append(cups_of_milk.popleft())
#         chocolate[-1] -= 5
#     else:
#         successfully_made_milkshakes += 1
#         del cups_of_milk[0]
#         del chocolate[-1]
#
#     if successfully_made_milkshakes == 5:
#         break
#
# if successfully_made_milkshakes == 5:
#     print(f"Great! You made all the chocolate milkshakes needed!")
# else:
#     print(f"Not enough milkshakes.")
#
# if chocolate:
#     print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
# else:
#     print("Chocolate: empty")
#
# if cups_of_milk:
#     print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
# else:
#     print("Milk: empty")
#
