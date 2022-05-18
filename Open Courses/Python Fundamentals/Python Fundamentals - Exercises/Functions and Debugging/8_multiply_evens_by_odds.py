number = input()
odd_numbers = 0
even_numbers = 0


def check_numbers(n):
    global odd_numbers, even_numbers
    for num in n:
        if num != "-":
            num = int(num)
            if num % 2 == 0:
                even_numbers += num
            else:
                odd_numbers += num


check_numbers(number)
print(odd_numbers * even_numbers)
