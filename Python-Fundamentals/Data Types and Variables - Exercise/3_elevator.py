number_of_people = int(input())
capacity = int(input())

people_full_course = 0
people_left = number_of_people
curses = 0

for courses in range(1, number_of_people + 1):

    people_full_course = people_left - capacity

    if people_full_course > 0:
        if people_full_course == 0:
            break
        else:
            people_left = people_full_course
            curses += 1
    else:
        curses += 1
        break

print(f"{curses}")
