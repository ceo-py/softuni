# name, age, town, salary = input(), int(input()), input(), float(input())
#
# age_range = ""
# salary_range = ""
#
# if age < 18:
#     age_range = "teen"
# elif age < 70:
#     age_range = "adult"
# else:
#     age_range = "elder"
# if salary < 500:
#     salary_range = "low"
# elif salary < 2000:
#     salary_range = "medium"
# else:
#     salary_range = "high"
#
# salary = f"{salary:.2f}"
#
# result_show = "Name: {}\nAge: {}\nTown: {}\nSalary: ${}\nAge range: {}\nSalary range: {}"
# print(result_show.format(name, age, town, salary, age_range, salary_range))



name, age, town, salary = input(), int(input()), input(), float(input())

age_range = None
salary_range = None

if age < 18:
    age_range = "teen"
elif age < 70:
    age_range = "adult"
else:
    age_range = "elder"
if salary < 500:
    salary_range = "low"
elif salary < 2000:
    salary_range = "medium"
else:
    salary_range = "high"

print(f"Name: {name}\nAge: {age}\nTown: {town}\nSalary: ${salary:.2f}\nAge range: {age_range}\nSalary range: {salary_range}")