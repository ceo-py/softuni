number_one = int(input())
number_two = int(input())

for i in range(number_one, number_two + 1):
    for o in range(number_one, number_two + 1):
        for p in range(number_one, number_two + 1):
            for l in range(number_one, number_two + 1):
                if ((i % 2 == 0 and l % 2 != 0) or (i % 2 != 0 and l % 2 == 0)) and \
                        i > l and ((o + p) % 2) == 0:
                    print(f"{i}{o}{p}{l}", end=" ")
