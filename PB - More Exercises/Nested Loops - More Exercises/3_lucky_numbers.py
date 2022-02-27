number = int(input())

for i in range(1, 10):
    for o in range(1, 10):
        for p in range(1, 10):
            for l in range(1, 10):
                if i + o == p + l and number % (i + o) == 0:
                    print(f"{i}{o}{p}{l}", end=" ")
