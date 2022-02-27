import string

n = int(input())
l = int(input())

alphabet_string_low = string.ascii_lowercase
alphabet_list_lower = list(alphabet_string_low)
l_letters = alphabet_list_lower[:l]

for n_one in range(1, n):

    for n_num in range(1, n + 2):

        for l in l_letters:

            for l_num in l_letters:

                for check in range(1, n + 3):

                    if n_one < check and check > n_num and check <= n:
                        print(f"{n_one}{n_num}{l}{l_num}{check}", end=" ")
