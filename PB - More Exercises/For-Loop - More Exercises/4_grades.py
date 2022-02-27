total_people_show_for_examp = int(input())

fail_students = 0
between_three_and_four = 0
between_four_and_five = 0
top_students = 0
average_grade = 0

for _ in range(1, total_people_show_for_examp + 1):
    grade = float(input())
    average_grade += grade

    if grade <= 2.99:
        fail_students += 1

    elif grade <= 3.99:
        between_three_and_four += 1

    elif grade <= 4.99:
        between_four_and_five += 1

    elif grade >= 5:
        top_students += 1

average_grade = average_grade / total_people_show_for_examp
fail_students = (fail_students / total_people_show_for_examp) * 100
between_three_and_four = (between_three_and_four / total_people_show_for_examp) * 100
between_four_and_five = (between_four_and_five / total_people_show_for_examp) * 100
top_students = (top_students / total_people_show_for_examp) * 100

print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {between_four_and_five:.2f}%")
print(f"Between 3.00 and 3.99: {between_three_and_four:.2f}%")
print(f"Fail: {fail_students:.2f}%")
print(f"Average: {average_grade:.2f}")
