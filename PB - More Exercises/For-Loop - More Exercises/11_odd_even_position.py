total_numbers_for_input = int(input())

all_numbers = list()
odd_numbers = list()
even_numbers = list()

for _ in range(1, total_numbers_for_input + 1):
    all_numbers.append(float(input()))

check = 0

for number in all_numbers:
    if check % 2 == 0:
        odd_numbers.append(number)
    else:
        even_numbers.append(number)
    check += + 1

even_sum = sum(even_numbers)
odd_sum = sum(odd_numbers)
even_numbers.sort()
odd_numbers.sort()

if total_numbers_for_input == 1:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_numbers[0]:.2f},")
    print(f"OddMax={odd_numbers[-1]:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")

elif total_numbers_for_input == 0:
    print(f"OddSum=0.00,")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
    print(f"EvenSum=0.00,")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")

else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_numbers[0]:.2f},")
    print(f"OddMax={odd_numbers[-1]:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_numbers[0]:.2f},")
    print(f"EvenMax={even_numbers[-1]:.2f}")
