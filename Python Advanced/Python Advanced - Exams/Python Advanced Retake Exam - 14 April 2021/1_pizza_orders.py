from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]
made_pizzas = 0

while pizza_orders and employees:
    pizza_order = pizza_orders.popleft()
    if pizza_order <= 0 or pizza_order > 10:
        continue
    employee = employees.pop()
    if pizza_order <= employee:
        made_pizzas += pizza_order
    elif pizza_order > employee:
        made_pizzas += employee
        pizza_orders.appendleft(pizza_order - employee)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {made_pizzas}")
    if employees:
        print(f"Employees: {', '.join(str(x) for x in employees)}")
elif not employees and pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")




