coins_per_one = int(input())
coins_per_two = int(input())
banknotes_per_five = int(input())
total_looking_sum = int(input())

for coins_one in range(0, coins_per_one + 1):
    i = coins_one * 1

    for coins_tow in range(0, coins_per_two + 1):
        o = coins_tow * 2

        for banknotes in range(0, banknotes_per_five + 1):
            p = banknotes * 5

            if i + o + p == total_looking_sum:
                print(f"{coins_one} * 1 lv. + {coins_tow} * 2 lv. + {banknotes} * 5 lv. = {total_looking_sum} lv.")
