lessons = input().split(", ")
commands_ = input()


def lesson_exist(lessons_title):
    if lessons_title in lessons:
        return True
    return False


def find_lesson_index(lesson_title):
    return lessons.index(lesson_title)


def check_for_exercise(index):
    for pos, x in enumerate(lessons[index:], 1):
        if pos == 2 and "Exercise" in x:
            return True
        if pos == 3:
            return False
    return False


def add_lesson(lessons_title):
    if not lesson_exist(lessons_title):
        lessons.append(lessons_title)


def insert_lesson(lessons_title, index_to_insert):
    if not lesson_exist(lessons_title):
        lessons.insert(index_to_insert, lessons_title)


def remove_lesson(lessons_title):
    if lesson_exist(lessons_title):
        index_lesson = find_lesson_index(lessons_title)
        del lessons[index_lesson]
        if check_for_exercise(index_lesson):
            del lessons[index_lesson]


def swap_lessons(lessons_title_one, lessons_title_two):
    if lesson_exist(lessons_title_one) and lesson_exist(lessons_title_two):
        lesson_one = find_lesson_index(lessons_title_one)
        lesson_two = find_lesson_index(lessons_title_two)
        lesson_one_exercise = check_for_exercise(lesson_one)
        lesson_two_exercise = check_for_exercise(lesson_two)
        if lesson_one_exercise and lesson_two_exercise:
            lesson_one_exercise = lessons[lesson_one + 1]
            lessons[lesson_one + 1] = lessons[lesson_two + 1]
            lessons[lesson_two + 1] = lesson_one_exercise
        elif lesson_one_exercise:
            lesson_one_exercise = lessons.pop(lesson_one + 1)
            lessons.insert(find_lesson_index(lessons_title_two) + 1, lesson_one_exercise)
        elif lesson_two_exercise:
            lesson_two_exercise = lessons.pop(lesson_two + 1)
            lessons.insert(find_lesson_index(lessons_title_one) + 1, lesson_two_exercise)
        lesson_one = find_lesson_index(lessons_title_one)
        lesson_two = find_lesson_index(lessons_title_two)
        lessons[lesson_one] = lessons_title_two
        lessons[lesson_two] = lessons_title_one


def exercise_lesson(lessons_title):
    if lesson_exist(lessons_title):
        lesson_index = find_lesson_index(lessons_title)
        if not check_for_exercise(lesson_index):
            lessons.insert(lesson_index + 1, f"{lessons_title}-Exercise")
    else:
        lessons.append(lessons_title)
        lessons.append(f"{lessons_title}-Exercise")


while commands_ != "course start":
    type_command, *info = commands_.split(":")
    if type_command == "Add":
        add_lesson(info[0])
    elif type_command == "Insert":
        insert_lesson(info[0], int(info[-1]))
    elif type_command == "Remove":
        remove_lesson(info[0])
    elif type_command == "Swap":
        swap_lessons(info[0], info[-1])
    elif type_command == "Exercise":
        exercise_lesson(info[0])
    commands_ = input()

for pos, lesson in enumerate(lessons, 1):
    print(f"{pos}.{lesson}")
