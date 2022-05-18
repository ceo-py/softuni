allow_bad_grades = int(input())

taks_names = list()
scores = 0
penalties = 0
total_taks = 0
task_score = 0

while True:
    taks_names.append(input())
    if "Enough" in taks_names:
        average_score = (scores / total_taks)
        print(f"Average score: {average_score:.2f}\nNumber of problems: {total_taks}\nLast problem: {taks_names[-2]}")
        break
    task_score = int(input())
    if task_score <= 4:
        penalties += 1
        total_taks += 1
        scores += task_score
    else:
        scores += task_score
        total_taks += 1
    if penalties == allow_bad_grades:
        print(f"You need a break, {penalties} poor grades.")
        break
