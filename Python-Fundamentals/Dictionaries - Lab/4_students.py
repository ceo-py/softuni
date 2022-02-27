student_information = input()

student_dic = dict()

while not student_dic.get(student_information):
    student_information = student_information.split(":")
    name_student = student_information[0]
    id_student = student_information[1]
    couse_student = student_information[-1]
    if couse_student not in student_dic:
        student_dic[couse_student] = {}
    student_dic[couse_student][name_student] = id_student
    student_information = input()
    student_information = student_information.replace("_", " ")

for key, value in student_dic[student_information].items():
    print(f"{key} - {value}")
