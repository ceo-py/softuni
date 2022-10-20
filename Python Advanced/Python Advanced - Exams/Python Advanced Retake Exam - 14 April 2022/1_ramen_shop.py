from collections import deque

bowls_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])


while bowls_ramen and customers:

    ramen = bowls_ramen.pop()
    customer = customers.popleft()

    if ramen == customer:
        pass

    elif ramen > customer:
        bowls_ramen.append(ramen - customer)

    elif customer > ramen:
        customers.appendleft(customer - ramen)

if not customers:
    print("Great job! You served all the customers.")
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")




#
#
# from collections import deque
#
# bowls = [int(x) for x in input().split(", ")]
# customers = deque(int(x) for x in input().split(", "))
#
#
# while bowls and customers:
#     bowl = bowls.pop()
#     customer = customers.popleft()
#     if bowl == customer:
#         continue
#
#     if bowl > customer:
#         bowl -= customer
#         bowls.append(bowl)
#
#     elif customer > bowl:
#         customer -= bowl
#         customers.appendleft(customer)
#
#
# if not customers:
#     print("Great job! You served all the customers.")
#     if bowls:
#         print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
# else:
#     print("Out of ramen! You didn't manage to serve all customers.")
#     print(f"Customers left: {', '.join(str(x) for x in customers)}")