heritage_money = float(input())
year_till_he_will_live = int(input())

total_heritage_left = heritage_money
starting_year = 18
expense_per_year = 12_000

for year in range(1800, year_till_he_will_live + 1):

    if year % 2 == 0:
        total_heritage_left = total_heritage_left - expense_per_year
        starting_year += 1

    else:
        total_heritage_left = total_heritage_left - (expense_per_year + (starting_year * 50))
        starting_year += 1

if total_heritage_left >= 0:
    print(f"Yes! He will live a carefree life and will have {total_heritage_left:.2f} dollars left.")
else:
    print(f"He will need {abs(total_heritage_left):.2f} dollars to survive.")
