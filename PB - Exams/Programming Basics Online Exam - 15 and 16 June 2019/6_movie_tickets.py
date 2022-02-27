number_one = int(input())
number_two = int(input())
number = int(input())

for i in range(number_one, number_two):
    n_one = chr(i)

    for o in range(1, number):

        for p in range(1, number // 2):

            if i % 2 != 0 and (i + o + p) % 2 != 0:
                print(f"{n_one}-{o}{p}{i}")
