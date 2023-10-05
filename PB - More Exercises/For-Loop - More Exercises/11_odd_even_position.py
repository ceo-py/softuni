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





#
# total_numbers_for_input = int(input())
# initial_list = [float(input()) for _ in range(total_numbers_for_input)]
# odd, even = initial_list[::2], initial_list[1::2]
#
# print(f"OddSum={sum(odd):.2f},")
# print(f"OddMin={min(odd):.2f}," if odd else 'OddMin=No,')
# print(f"OddMax={max(odd):.2f}," if odd else 'OddMax=No,')
# print(f"EvenSum={sum(even):.2f},")
# print(f"EvenMin={min(even):.2f}," if even else 'EvenMin=No,')
# print(f"EvenMax={max(even):.2f}" if even else 'EvenMax=No')
#
#
#
#
#








#
#
# total_numbers_for_input = int(input())
#
# all_numbers = list()
# odd_numbers = list()
# even_numbers = list()
#
# for _ in range(1, total_numbers_for_input + 1):
#     all_numbers.append(float(input()))
#
# check = 0
#
# for number in all_numbers:
#     if check % 2 == 0:
#         odd_numbers.append(number)
#     else:
#         even_numbers.append(number)
#     check += + 1
#
# even_sum = sum(even_numbers)
# odd_sum = sum(odd_numbers)
# even_numbers.sort()
# odd_numbers.sort()
#
# if total_numbers_for_input == 1:
#     print(f"OddSum={odd_sum:.2f},")
#     print(f"OddMin={odd_numbers[0]:.2f},")
#     print(f"OddMax={odd_numbers[-1]:.2f},")
#     print(f"EvenSum={even_sum:.2f},")
#     print(f"EvenMin=No,")
#     print(f"EvenMax=No")
#
# elif total_numbers_for_input == 0:
#     print(f"OddSum=0.00,")
#     print(f"OddMin=No,")
#     print(f"OddMax=No,")
#     print(f"EvenSum=0.00,")
#     print(f"EvenMin=No,")
#     print(f"EvenMax=No")
#
# else:
#     print(f"OddSum={odd_sum:.2f},")
#     print(f"OddMin={odd_numbers[0]:.2f},")
#     print(f"OddMax={odd_numbers[-1]:.2f},")
#     print(f"EvenSum={even_sum:.2f},")
#     print(f"EvenMin={even_numbers[0]:.2f},")
#     print(f"EvenMax={even_numbers[-1]:.2f}")
