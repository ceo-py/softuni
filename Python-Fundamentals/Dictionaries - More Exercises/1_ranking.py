contest_add = input()

exams_information = {"contest": {}, "students": {}}
contest_d = "contest"
students_d = "students"

while contest_add != "end of contests":
    contest_add = contest_add.split(":")
    contest = contest_add[0]
    contest_pass = contest_add[-1]
    exams_information[contest_d][contest] = contest_pass
    contest_add = input()

submissions = input()
while submissions != "end of submissions":
    submissions = submissions.split("=>")
    contest = submissions[0]
    contest_pass = submissions[1]
    contest_user = submissions[2]
    contest_points = int(submissions[-1])
    if contest in exams_information[contest_d]:
        if exams_information[contest_d][contest] == contest_pass:
            if contest_user not in exams_information[students_d]:
                exams_information[students_d][contest_user] = {}
            if contest not in exams_information[students_d][contest_user]:
                exams_information[students_d][contest_user][contest] = 0
            if exams_information[students_d][contest_user][contest] < contest_points:
                exams_information[students_d][contest_user][contest] = contest_points
    submissions = input()


def show_result():
    best_name = ""
    total_points = 0
    for name in exams_information[students_d]:
        score_for_user = sum(exams_information[students_d][name].values())
        if score_for_user > total_points:
            total_points = score_for_user
            best_name = name
    print(f"Best candidate is {best_name} with total {total_points} points.\nRanking:")
    for name in sorted(exams_information[students_d]):
        print(name)
        for contest, points in sorted(exams_information[students_d][name].items(), key=lambda item: -item[1]):
            print(f"#  {contest} -> {points}")


show_result()
