
prime = 0
not_prime = 0
while True:
    n = input()
    if n == "stop":
        break
    n = int(n)
    if n >= 0:
        for i in range(2, n // 2):
            if (n % i) == 0:
                not_prime += n
                break
        else:
            prime += n

    else:
        print("Number is negative.")


print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {not_prime}")