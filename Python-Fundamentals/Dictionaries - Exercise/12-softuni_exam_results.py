school = {"Submissions": {}}

command = input()
while command != "exam finished":
    if "banned" in command.split("-"):
        del school[username]
    else:
        username, language, points = [int(x) if x.isdigit() else x for x in command.split("-")]
        school["Submissions"][language] = school["Submissions"].get(language, 0)
        school["Submissions"][language] += 1
        school[username] = school.get(username, {})
        school[username][language] = school[username].get(language, points)
        if school[username][language] < points:
            school[username][language] = points

    command = input()

print("Results:")
for user in school:
    if user != "Submissions":
        for k, v in school[user].items():
            print(f"{user} | {v}")
print("Submissions:")
for lang, count in school["Submissions"].items():
    print(f"{lang} - {count}")





#
#
# user_command = input()
# student_information = {}
# ban_user_list = []
# submissions = "Submissions"
#
#
# def ban_user(name):
#     ban_user_list.append(name)
#
#
# def add_user(name, lang, score):
#     student_information[lang] = student_information.get(lang, {})
#     student_information[lang][name] = student_information[lang].get(name, 0)
#     student_information[lang][submissions] = student_information[lang].get(submissions, 0)
#     if student_information[lang][name] < score:
#         student_information[lang][name] = score
#     student_information[lang][submissions] += 1
#
#
# def show_result():
#     global submissions
#     print("Results:")
#     for key in student_information:
#         for name, score in student_information[key].items():
#             if all([name not in ban_user_list, submissions not in name]):
#                 print(f"{name} | {score}")
#     print(f"{submissions}:")
#     for key in student_information:
#         if student_information[key]:
#         # if len(student_information[key]) > 0:
#             print(f"{key} - {student_information[key][submissions]}")
#
#
# while user_command != "exam finished":
#     user_command = user_command.split("-")
#     if user_command[-1] == "banned":
#         ban_user(user_command[0])
#     else:
#         add_user(user_command[0], user_command[1], int(user_command[-1]))
#     user_command = input()
#
# show_result()
