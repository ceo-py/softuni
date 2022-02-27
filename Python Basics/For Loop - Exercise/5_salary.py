open_tab_browser = int(input())
salary = int(input())

salary_info = {"penalty": {
    "Facebook": 150,
    "Instagram": 100,
    "Reddit": 50, },
    "tabs counter": {
        "Facebook": 0,
        "Instagram": 0,
        "Reddit": 0}
}
salary_left = salary
tabs_check = ["Facebook", "Instagram", "Reddit"]
no_money_left = False

for tab in range(0, open_tab_browser):
    tab_name = input()
    if tab_name in tabs_check:
        salary_left = salary_left - salary_info["penalty"][tab_name]
    if salary_left <= 0:
        no_money_left = True
        print("You have lost your salary.")
        break

if no_money_left == False:
    if salary_left == salary:
        print(salary_left)
    else:
        print(salary_left)
