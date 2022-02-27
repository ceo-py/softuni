number_list = [int(n) for n in input().split(", ")]

negative = [number for number in number_list if number < 0]
positive = [number for number in number_list if number >= 0]

odd = [number for number in number_list if number % 2 != 0]
even = [number for number in number_list if number % 2 == 0]

print("Positive:", end=" ")
print(*positive, sep = ", ")
print("Negative:", end=" ")
print(*negative, sep = ", ")
print("Even:", end=" ")
print(*even, sep = ", ")
print("Odd:", end=" ")
print(*odd, sep = ", ")
