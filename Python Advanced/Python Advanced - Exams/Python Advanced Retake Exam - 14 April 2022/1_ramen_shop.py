from collections import deque

bowls = [int(x) for x in input().split(", ")]
customers = deque(int(x) for x in input().split(", "))


while bowls and customers:
    bowl = bowls.pop()
    customer = customers.popleft()
    if bowl == customer:
        continue

    if bowl > customer:
        bowl -= customer
        bowls.append(bowl)

    elif customer > bowl:
        customer -= bowl
        customers.appendleft(customer)


if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")