number_range = int(input())

even = list()
negative = list()
positive = list()
odd = list()

for _ in range(1, number_range + 2):
    number = input()

    if number == "even":
        break
    elif number == "negative":
        break

    elif number == "positive":
        break

    elif number == "odd":
        break

    if int(number) % 2 == 0:
        even.append(int(number))

    if int(number) < 0:
        negative.append(int(number))

    if int(number) >= 0:
        positive.append(int(number))

    if int(number) % 2 != 0:
        odd.append(int(number))

if number == "even":
    print(even)

elif number == "negative":
    print(negative)

elif number == "positive":
    print(positive)

elif number == "odd":
    print(odd)



