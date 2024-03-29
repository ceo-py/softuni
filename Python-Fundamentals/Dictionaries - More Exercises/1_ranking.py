passwords = {}
rankings = {}

contest = input()

while contest != 'end of contests':
    name, password = contest.split(':')
    passwords[name] = password
    contest = input()

users_input = input()

while users_input != 'end of submissions':
    contest_name, password, user_name, score = users_input.split('=>')

    if contest_name not in passwords or password != passwords[contest_name]:
        users_input = input()
        continue

    rankings[user_name] = rankings.get(user_name, {})
    rankings[user_name][contest_name] = rankings[user_name].get(contest_name, 0)
    rankings[user_name][contest_name] = max(int(score), rankings[user_name][contest_name])

    users_input = input()

max_user, max_total_score = max(rankings.items(), key=lambda user_scores: sum(user_scores[1].values()))

print(f'Best candidate is {max_user} with total {sum(max_total_score.values())} points.\nRanking:')
for name in sorted(rankings):
    print(name)
    for contest, points in sorted(rankings[name].items(), key=lambda item: -item[1]):
        print(f"#  {contest} -> {points}")







# contests, users = {}, {}
# contest_data = input()
#
# while contest_data != "end of contests":
#     contest, password = contest_data.split(":")
#     contests[contest] = password
#     contest_data = input()
#
# submission_data = input()
#
# while submission_data != "end of submissions":
#     contest, password, username, points = [int(x) if x.isdigit() else x for x in submission_data.split("=>")]
#     if contests.get(contest) == password:
#         users[username] = users.get(username, {})
#         users[username][contest] = users[username].get(contest, 0)
#         if users[username][contest] < points:
#             users[username][contest] = points
#     submission_data = input()
#
#
# candidates = {name: sum(users[name].values()) for name in users}
# best_candidate = max(candidates, key=candidates.get)
# print(f"Best candidate is {best_candidate} with total {candidates[best_candidate]} points."
#       f"\nRanking:")
#
# for name in sorted(users):
#     print(name)
#     for contest, points in sorted(users[name].items(), key=lambda item: -item[1]):
#         print(f"#  {contest} -> {points}")


#
#
# contest_add = input()
#
# exams_information = {"contest": {}, "students": {}}
# contest_d, students_d = "contest", "students"
#
# while contest_add != "end of contests":
#     contest, contest_pass = contest_add.split(":")
#     exams_information[contest_d][contest] = contest_pass
#     contest_add = input()
#
# submissions = input()
# while submissions != "end of submissions":
#     contest, contest_pass, contest_user, contest_points = [int(x) if x.isdigit() else x for x in submissions.split("=>")]
#     if contest in exams_information[contest_d] and exams_information[contest_d][contest] == contest_pass:
#         exams_information[students_d][contest_user] = exams_information[students_d].get(contest_user, {})
#         exams_information[students_d][contest_user][contest] = exams_information[students_d][contest_user].get(contest, 0)
#         if exams_information[students_d][contest_user][contest] < contest_points:
#             exams_information[students_d][contest_user][contest] = contest_points
#     submissions = input()
#
#
# def show_result():
#     best_name = ""
#     total_points = 0
#     for name in exams_information[students_d]:
#         score_for_user = sum(exams_information[students_d][name].values())
#         if score_for_user > total_points:
#             total_points = score_for_user
#             best_name = name
#     print(f"Best candidate is {best_name} with total {total_points} points.\nRanking:")
#     for name in sorted(exams_information[students_d]):
#         print(name)
#         for contest, points in sorted(exams_information[students_d][name].items(), key=lambda item: -item[1]):
#             print(f"#  {contest} -> {points}")
#
#
# show_result()
#
#


#
#
# contest_add = input()
#
# exams_information = {"contest": {}, "students": {}}
# contest_d = "contest"
# students_d = "students"
#
# while contest_add != "end of contests":
#     contest_add = contest_add.split(":")
#     contest = contest_add[0]
#     contest_pass = contest_add[-1]
#     exams_information[contest_d][contest] = contest_pass
#     contest_add = input()
#
# submissions = input()
# while submissions != "end of submissions":
#     submissions = submissions.split("=>")
#     contest = submissions[0]
#     contest_pass = submissions[1]
#     contest_user = submissions[2]
#     contest_points = int(submissions[-1])
#     if contest in exams_information[contest_d]:
#         if exams_information[contest_d][contest] == contest_pass:
#             if contest_user not in exams_information[students_d]:
#                 exams_information[students_d][contest_user] = {}
#             if contest not in exams_information[students_d][contest_user]:
#                 exams_information[students_d][contest_user][contest] = 0
#             if exams_information[students_d][contest_user][contest] < contest_points:
#                 exams_information[students_d][contest_user][contest] = contest_points
#     submissions = input()
#
#
# def show_result():
#     best_name = ""
#     total_points = 0
#     for name in exams_information[students_d]:
#         score_for_user = sum(exams_information[students_d][name].values())
#         if score_for_user > total_points:
#             total_points = score_for_user
#             best_name = name
#     print(f"Best candidate is {best_name} with total {total_points} points.\nRanking:")
#     for name in sorted(exams_information[students_d]):
#         print(name)
#         for contest, points in sorted(exams_information[students_d][name].items(), key=lambda item: -item[1]):
#             print(f"#  {contest} -> {points}")
#
#
# show_result()
