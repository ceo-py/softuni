name = input()
year_grade = 0
bad_years = 0
average_grade = 0

while year_grade < 12:
    year_grade = float(input())

    if year_grade < 4:
        bad_years += 1
        if bad_years == 2:
            print(f"{name} has been excluded at {year_grade + 1} grade")
            break
        continue
    year_grade += 1
    average_grade += year_grade
else:
    print(f"{name} graduated. Average grade: {average_grade / year_grade:.2f}")




# name = input()
# years_counter = 0
# failed_counter = 0
# grades_counter = 0
#
# while True:
#     year_grade = float(input())
#
#     if year_grade < 4:
#         failed_counter += 1
#         if failed_counter == 2:
#             print(f'{name} has been excluded at {years_counter + 1} grade')
#             break
#     else:
#         grades_counter += year_grade
#         years_counter += 1
#
#     if years_counter == 12:
#         average_grade = grades_counter / 12
#         print(f'{name} graduated. Average grade: {average_grade:.2f}')
#         break






#
# student_name = input()
# total = list()
# classes = 0
# scored_under_four = 0
# while True:
#     grade = float(input())
#     if grade >= 4.00:
#         classes += 1
#         total.append(grade)
#     else:
#         scored_under_four += 1
#     if scored_under_four == 2:
#         classes += 1
#         print(f"{student_name} has been excluded at {classes} grade")
#         break
#     elif classes == 13:
#         total = sum(total) / 12
#         print(f"{student_name} graduated. Average grade: {total:.2f}")
#         break
#     elif classes == 12:
#         total = sum(total) / 12
#         print(f"{student_name} graduated. Average grade: {total:.2f}")
#         break
