number = int(input())

guessed_passwords = ''
counter = 0

for a in range(1, 10):

    for b in range(1, 10):

        for c in range(1, 10):

            for d in range(1, 10):

                if a * b + c * d == number and a < b and c > d:
                    print(f"{a}{b}{c}{d}", end=" ")
                    counter += 1

                    if counter == 4:
                        guessed_passwords = f"{a}{b}{c}{d}"

if counter >= 4:
    print(f"\nPassword: {guessed_passwords}")

else:
    print(f"\nNo!")






# number = int(input())
#
# guessed_passwords = list()
#
#
# for a in range(1, 10):
#
#     for b in range(1, 10):
#
#         for c in range(1, 10):
#
#             for d in range(1, 10):
#
#                 if a * b + c * d == number and a < b and c > d:
#                     print(f"{a}{b}{c}{d}", end=" ")
#                     guessed_passwords.append(f"{a}{b}{c}{d}")
#
#
# if len(guessed_passwords) >= 4:
#     print(f"\nPassword: {guessed_passwords[3]}")
#
# else:
#     print(f"\nNo!")
