phonenumbers = {}

numbers = input()

while numbers != "Over":
    numbers = numbers.split(" : ")
    if numbers[-1].isdigit():
        phonenumbers[numbers[0]] = numbers[-1]
    else:
        phonenumbers[numbers[-1]] = numbers[0]
    numbers = input()

for key, value in sorted(phonenumbers.items(), key = lambda item: item[0]):
    print(f"{key} -> {value}")