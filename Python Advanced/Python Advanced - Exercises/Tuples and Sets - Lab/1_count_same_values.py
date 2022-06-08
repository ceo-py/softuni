numbers_to_count = input().split()

result = {float(num): numbers_to_count.count(num) for num in numbers_to_count}
for number, counter in result.items():
    print(f"{number:.1f} - {counter} times")


