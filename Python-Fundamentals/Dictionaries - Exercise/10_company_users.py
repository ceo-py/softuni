command = input()

company_info = {}


def employee_id_search(id):
    for value in company_info[id].values():
        if id == value:
            return True
    return False


while command != "End":
    company_name, employee_id = command.split(" -> ")
    company_info[company_name] = company_info.get(company_name, {})
    if not employee_id_search(company_name):
        company_info[company_name][employee_id] = employee_id
    command = input()

for name_uni in company_info:
    print(name_uni)
    for key, value in company_info[name_uni].items():
        print(f"-- {value}")
