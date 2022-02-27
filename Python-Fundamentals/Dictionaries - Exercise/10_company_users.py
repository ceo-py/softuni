command = input()

company_info = {}


def employee_id_seach(id):
    global duplicate_id
    for key, value in company_info[id].items():
        if id == value:
            duplicate_id = True
            break


while command != "End":
    duplicate_id = False
    command = command.split(" -> ")
    company_name = command[0]
    employee_id = command[-1]
    if company_name not in company_info:
        company_info[company_name] = {}
    employee_id_seach(company_name)

    if not duplicate_id:
        company_info[company_name][employee_id] = employee_id
    command = input()

for name_uni in company_info:
    print(name_uni)
    for key, value in company_info[name_uni].items():
        print(f"-- {value}")
