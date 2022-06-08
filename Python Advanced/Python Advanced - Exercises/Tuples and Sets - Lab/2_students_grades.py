number_of_students = int(input())

result = {}
for student in range(number_of_students):
    student_name, student_grade = input().split()
    result[student_name] = result.get(student_name, list())
    result[student_name].append(f"{float(student_grade):.2f}")

for name, grades in result.items():
    print(f"{name} -> {' '.join(grades)} (avg: {(sum(float(num) for num in grades)/len(grades)):.2f})")


