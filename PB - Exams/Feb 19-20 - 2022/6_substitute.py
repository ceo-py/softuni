k_num = int(input())
l_num = int(input())
m_num = int(input())
n_num = int(input())

valid_count = 0
for k in range(k_num, 9):
    if k % 2 == 0:
        for l in range(9, l_num - 1, -1):
            if l % 2 != 0:
                for m in range(m_num, 9):
                    if m % 2 == 0:
                        for n in range(9, n_num - 1, -1):
                            if n % 2 != 0:
                                digit_one = k * 10 + l
                                digit_two = m * 10 + n
                                if digit_one != digit_two:
                                    print(f"{k}{l} - {m}{n}")
                                    valid_count += 1
                                    if valid_count == 6:
                                        exit()
                                if digit_one == digit_two:
                                    print("Cannot change the same player.")

