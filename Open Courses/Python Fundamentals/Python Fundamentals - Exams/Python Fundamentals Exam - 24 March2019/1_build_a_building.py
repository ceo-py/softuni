budget = float(input())
capital = float(input())
investors_number = int(input())

for number_investors in range(1, investors_number + 1):
    money_give = float(input())
    capital += money_give
    print(f"Investor {number_investors} gave us {money_give:.2f}.")
    if capital >= budget:
        print(f"We will manage to build it. Start now! Extra money - {(capital - budget):.2f}.")
        break

if capital < budget:
    print(f"Project can not start. We need {abs(capital - budget):.2f} more.")
