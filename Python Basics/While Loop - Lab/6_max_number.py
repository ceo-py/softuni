total = list()
while True:
    numbers = input()
    if numbers != "Stop":
        total.append(int(numbers))
    else:
        total.sort()
        print(total[-1])
        break
