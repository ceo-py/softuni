total_numbers_for_input = int(input())

max_even_number = 0
min_even_number = 0
max_odd_number = 0
min_odd_number = 0
even_sum = 0
odd_sum = 0


for time in range(1, total_numbers_for_input + 1):
    number = (float(input()))

    if time % 2 != 0:
        odd_sum += number
        if max_odd_number < number or time == 1:
            max_odd_number = number
        if min_odd_number > number or time == 1:
            min_odd_number = number
    else:
        even_sum += number
        if max_even_number < number or time == 2:
            max_even_number = number
        if min_even_number > number or time == 2:
            min_even_number = number



if total_numbers_for_input == 1:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={min_odd_number:.2f},")
    print(f"OddMax={max_odd_number:.2f},")
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
    print(f"OddMin={min_odd_number:.2f},")
    print(f"OddMax={max_odd_number:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={min_even_number:.2f},")
    print(f"EvenMax={max_even_number:.2f}")