number = input()
prime_sum = 0
none_prime_sum = 0

while number != 'stop':

    number = int(number)

    if number < 0:
        print('Number is negative.')
        number = input()
        continue


    if number == 1:
        none_prime_sum += number

    elif number > 1:

        for i in range(2, number):
            if number % i == 0:
                none_prime_sum += number
                break

        else:
            prime_sum += number

    number = input()


print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {none_prime_sum}")






# prime = 0
# not_prime = 0
# while True:
#     n = input()
#     if n == "stop":
#         break
#     n = int(n)
#     if n >= 0:
#         for i in range(2, n // 2):
#             if (n % i) == 0:
#                 not_prime += n
#                 break
#         else:
#             prime += n
#
#     else:
#         print("Number is negative.")
#
#
# print(f"Sum of all prime numbers is: {prime}")
# print(f"Sum of all non prime numbers is: {not_prime}")