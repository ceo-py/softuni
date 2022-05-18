numbers_to_check = int(input())

for _ in range(numbers_to_check):
    num = int(input())
    if num == 88:
        print("Hello")
    elif num == 86:
        print("How are you?")
    elif all([num != 88, num != 86]) and num < 88:
        print("GREAT!")
    elif num > 88:
        print("Bye.")
