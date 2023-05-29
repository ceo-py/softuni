courses, individual = {}, {}
data = input()
while data != "no more time":

    name, course, score = [x if x.isalpha() else int(x) for x in data.split(" -> ")]
    courses[course] = courses.get(course, {})
    courses[course][name] = courses[course].get(name, 0)
    if courses[course][name] < score:
        courses[course][name] = score
    data = input()

for course in courses:
    print(f"{course}: {len(courses[course])} participants")
    for pos, (user, score) in enumerate(sorted(courses[course].items(), key= lambda x: (-x[1], x[0])), 1):
        print(f"{pos}. {user} <::> {score}")
        individual[user] = individual.get(user, 0) + score

print("Individual standings:")
for pos, (user, score) in enumerate(sorted(individual.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{pos}. {user} -> {score}")













#
#
# command_judge = input()
#
# judge_info = {"user": {}, "contest": {}}
# user_d = "user"
# contest_d = "contest"
#
# while command_judge != "no more time":
#     user_name, contest, points = [int(x) if x.isdigit() else x for x in command_judge.split(" -> ")]
#     judge_info[contest_d][contest] = judge_info[contest_d].get(contest, {})
#     judge_info[contest_d][contest][user_name] = judge_info[contest_d][contest].get(user_name, 0)
#     judge_info[user_d][user_name] = judge_info[user_d].get(user_name, 0)
#     if user_name in judge_info[user_d] and judge_info[user_d][user_name] == points:
#         judge_info[user_d][user_name] += points
#     if judge_info[contest_d][contest][user_name] < points:
#         judge_info[user_d][user_name] += points - judge_info[contest_d][contest][user_name]
#         judge_info[contest_d][contest][user_name] = points
#
#     command_judge = input()
#
#
# def show_result():
#     for contest in judge_info[contest_d]:
#         print(f"{contest}: {len(judge_info[contest_d][contest])} participants")
#         for pos, (name, points) in enumerate(
#                 sorted(judge_info[contest_d][contest].items(), key=lambda item: (-item[1], item[0])), 1):
#             print(f"{pos}. {name} <::> {points}")
#     print("Individual standings:")
#     for pos, (name, points) in enumerate(sorted(judge_info[user_d].items(), key=lambda item: (-item[1], item[0])), 1):
#         print(f"{pos}. {name} -> {points}")
#
#
# show_result()
#







#
#
#
# command_judge = input()
#
# judge_info = {"user": {}, "contest": {}}
# user_d = "user"
# contest_d = "contest"
#
# while command_judge != "no more time":
#     command_judge = command_judge.split(" -> ")
#     user_name = command_judge[0]
#     contest = command_judge[1]
#     points = int(command_judge[-1])
#     if contest not in judge_info[contest_d]:
#         judge_info[contest_d][contest] = {}
#     if user_name not in judge_info[contest_d][contest]:
#         judge_info[contest_d][contest][user_name] = 0
#     if user_name not in judge_info[user_d]:
#         judge_info[user_d][user_name] = 0
#     if user_name in judge_info[user_d] and judge_info[user_d][user_name] == points:
#         judge_info[user_d][user_name] += points
#     if judge_info[contest_d][contest][user_name] < points:
#         judge_info[user_d][user_name] += points - judge_info[contest_d][contest][user_name]
#         judge_info[contest_d][contest][user_name] = points
#
#     command_judge = input()
#
#
# def show_result():
#     for contest in judge_info[contest_d]:
#         print(f"{contest}: {len(judge_info[contest_d][contest])} participants")
#         for pos, (name, points) in enumerate(
#                 sorted(judge_info[contest_d][contest].items(), key=lambda item: (-item[1], item[0])), 1):
#             print(f"{pos}. {name} <::> {points}")
#     print("Individual standings:")
#     for pos, (name, points) in enumerate(sorted(judge_info[user_d].items(), key=lambda item: (-item[1], item[0])), 1):
#         print(f"{pos}. {name} -> {points}")
#
#
# show_result()



# contests = {}
# users = {}
# while True:
#     command = input()
#     if command == "no more time":
#         break
#     username, contest, points = command.split(" -> ")
#     if contest not in contests:
#         contests[contest] = {}
#     if username not in contests[contest]:
#         contests[contest][username] = 0
#     if contests[contest][username] < int(points):
#         contests[contest][username] = int(points)
# for contest in contests.keys():
#     print(f"{contest}: {len(contests[contest].keys())} participants")
#     for i, (username, points) in enumerate(sorted(contests[contest].items(), key=lambda x: (-x[1], x[0])), 1):
#         if username not in users:
#             users[username] = 0
#         users[username] += points
#         print(f"{i}. {username} <::> {points}")
# print("Individual standings:")
# for i, (key, value) in enumerate(sorted(users.items(), key=lambda x: (-x[1], x[0])), 1):
#     print(f"{i}. {key} -> {value}")
#