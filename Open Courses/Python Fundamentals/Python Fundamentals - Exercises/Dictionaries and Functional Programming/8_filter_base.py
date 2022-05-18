employee_attributes = input()

age = "Age"
position = "Position"
salary = "Salary"
employees_info = {age: {}, position: {}, salary: {}}

while employee_attributes != "filter base":
    employee_attributes = employee_attributes.split(" -> ")
    if employee_attributes[-1].isnumeric():
        employees_info[age][employee_attributes[0]] = employee_attributes[-1]
    elif employee_attributes[-1].isalpha():
        employees_info[position][employee_attributes[0]] = employee_attributes[-1]
    else:
        employees_info[salary][employee_attributes[0]] = employee_attributes[-1]
    employee_attributes = input()


def show_result(text):
    for name, value in employees_info[text].items():
        print(f"Name: {name}\n{text}: {value}")
        print("====================")


show_result(input())
