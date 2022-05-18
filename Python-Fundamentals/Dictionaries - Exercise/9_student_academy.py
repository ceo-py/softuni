number_students = int(input())

students_grades = {}

for _ in range(number_students):
    name = input()
    grade = float(input())
    students_grades[name] = students_grades.get(name, {})
    students_grades[name][name + str(grade)] = 0
    students_grades[name][name + str(grade)] += grade

for name_student in students_grades:
    score = 0
    for key, value in students_grades[name_student].items():
        score += value
    average_score = score / len(students_grades[name_student])
    if average_score >= 4.50:
        print(f"{name_student} -> {average_score:.2f}")
