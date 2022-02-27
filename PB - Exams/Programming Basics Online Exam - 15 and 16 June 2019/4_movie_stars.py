budget_actors = float(input())

budget_left = budget_actors
actor_salary = 0
adding_more_people = 100

while True:

    name_actor = input()
    if name_actor == "ACTION":
        print(f"We are left with {budget_left:.2f} leva.")
        break

    elif len(name_actor) > 15:
        budget_left = budget_left - (budget_left * 0.20)
        name_actor = input()
        if len(name_actor) > 15:
            budget_left = budget_left - (budget_left * 0.20)
            name_actor = input()
            for i in range(0, adding_more_people):
                if len(name_actor) > 15:
                    budget_left = budget_left - (budget_left * 0.20)
                    name_actor = input()

                else:
                    break

        if name_actor == "ACTION":
            print(f"We are left with {budget_left:.2f} leva.")
            break

        actor_salary = float(input())

    else:
        actor_salary = float(input())

    budget_left -= actor_salary

    if budget_left < 0:
        print(f"We need {abs(budget_left):.2f} leva for our actors.")
        break
