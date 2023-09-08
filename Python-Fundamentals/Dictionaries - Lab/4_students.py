students_course_info = []
while True:
    data = input().split(':')

    if len(data) == 1:
        data = data[0].replace("_", " ")
        break

    (students_course_info.append({data[i + 2]: f'{data[i]} - {data[i + 1]}' for i in range(0, len(data), 3)}))

for score in students_course_info:
    if score.get(data):
        print(score.get(data))






# student_information = input()

# student_dic = dict()
#
# while not student_dic.get(student_information):
#     student_information = student_information.split(":")
#     name_student = student_information[0]
#     id_student = student_information[1]
#     couse_student = student_information[-1]
#     if couse_student not in student_dic:
#         student_dic[couse_student] = {}
#     student_dic[couse_student][name_student] = id_student
#     student_information = input()
#     student_information = student_information.replace("_", " ")
#
# for key, value in student_dic[student_information].items():
#     print(f"{key} - {value}")
