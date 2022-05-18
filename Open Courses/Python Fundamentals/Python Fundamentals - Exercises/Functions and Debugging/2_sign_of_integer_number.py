number = int(input())


def check_number(n):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


print(f"The number {number} is {check_number(number)}.")
