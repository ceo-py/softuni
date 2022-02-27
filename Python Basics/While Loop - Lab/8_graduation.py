student_name = input()
total = list()
classes = 0
scored_under_four = 0
while True:
    grade = float(input())
    if grade >= 4.00:
        classes += 1
        total.append(grade)
    else:
        scored_under_four += 1
    if scored_under_four == 2:
        classes += 1
        print(f"{student_name} has been excluded at {classes} grade")
        break
    elif classes == 13:
        total = sum(total) / 12
        print(f"{student_name} graduated. Average grade: {total:.2f}")
        break
    elif classes == 12:
        total = sum(total) / 12
        print(f"{student_name} graduated. Average grade: {total:.2f}")
        break
