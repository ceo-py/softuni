command_judge = input()

judge_info = {"user": {}, "contest": {}}
user_d = "user"
contest_d = "contest"

while command_judge != "no more time":
    user_name, contest, points = [int(x) if x.isdigit() else x for x in command_judge.split(" -> ")]
    judge_info[contest_d][contest] = judge_info[contest_d].get(contest, {})
    judge_info[contest_d][contest][user_name] = judge_info[contest_d][contest].get(user_name, 0)
    judge_info[user_d][user_name] = judge_info[user_d].get(user_name, 0)
    if user_name in judge_info[user_d] and judge_info[user_d][user_name] == points:
        judge_info[user_d][user_name] += points
    if judge_info[contest_d][contest][user_name] < points:
        judge_info[user_d][user_name] += points - judge_info[contest_d][contest][user_name]
        judge_info[contest_d][contest][user_name] = points

    command_judge = input()


def show_result():
    for contest in judge_info[contest_d]:
        print(f"{contest}: {len(judge_info[contest_d][contest])} participants")
        for pos, (name, points) in enumerate(
                sorted(judge_info[contest_d][contest].items(), key=lambda item: (-item[1], item[0])), 1):
            print(f"{pos}. {name} <::> {points}")
    print("Individual standings:")
    for pos, (name, points) in enumerate(sorted(judge_info[user_d].items(), key=lambda item: (-item[1], item[0])), 1):
        print(f"{pos}. {name} -> {points}")


show_result()








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
