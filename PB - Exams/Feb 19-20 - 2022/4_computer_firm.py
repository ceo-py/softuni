pc_number = int(input())

total_sales = 0
rating_score = 0
for pc in range(pc_number):
    rating = input()
    sale = rating[0] + rating[1]

    if rating[-1] == "3":
        total_sales += int(sale) * 0.50

    elif rating[-1] == "4":
        total_sales += int(sale) * 0.70

    elif rating[-1] == "5":
        total_sales += int(sale) * 0.85

    elif rating[-1] == "6":
        total_sales += int(sale)
    rating_score += int(rating[-1])

print(f"{total_sales:.2f}")
print(f"{(rating_score / pc_number):.2f}")
