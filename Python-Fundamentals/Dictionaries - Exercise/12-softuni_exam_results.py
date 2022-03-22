user_command = input()
student_information = {}
ban_user_list = []
submissions = "Submissions"


def ban_user(name):
    ban_user_list.append(name)


def add_user(name, lang, score):
    if lang not in student_information:
        student_information[lang] = {}
        student_information[lang][name] = 0
        student_information[lang][submissions] = 0
    if name not in student_information[lang]:
        student_information[lang][name] = 0
    if student_information[lang][name] < score:
        student_information[lang][name] = score
    student_information[lang][submissions] += 1


def show_result():
    global submissions
    print("Results:")
    for key in student_information:
        for name, score in student_information[key].items():
            if name not in ban_user_list and submissions not in name:
                print(f"{name} | {score}")
    print("Submissions:")
    for key in student_information:
        if len(student_information[key]) > 0:
            print(f"{key} - {student_information[key][submissions]}")


while user_command != "exam finished":
    user_command = user_command.split("-")
    if user_command[-1] == "banned":
        ban_user(user_command[0])
    else:
        add_user(user_command[0], user_command[1], int(user_command[-1]))
    user_command = input()

show_result()