schedule_of_lessons = input().split(", ")


def check_for_exercise(find_index: int) -> bool:
    try:
        return "Exercise" in schedule_of_lessons[find_index + 1]
    except IndexError:
        return


def add_lesson(lesson_title: str) -> None:
    if lesson_title not in schedule_of_lessons:
        schedule_of_lessons.append(lesson_title)


def insert_lesson(lesson_title: str, index: int) -> None:
    if lesson_title not in schedule_of_lessons:
        schedule_of_lessons.insert(index, lesson_title)


def remove_lesson(lesson_title: str) -> None:
    if lesson_title in schedule_of_lessons:
        find_index = schedule_of_lessons.index(lesson_title)
        if check_for_exercise(find_index):
            del schedule_of_lessons[find_index]
        del schedule_of_lessons[find_index]


def swap_lesson(lesson_title: str, lesson_title_swap: str) -> None:
    if lesson_title in schedule_of_lessons and lesson_title_swap in schedule_of_lessons:
        index_lesson_one = schedule_of_lessons.index(lesson_title)
        index_lesson_two = schedule_of_lessons.index(lesson_title_swap)
        schedule_of_lessons[index_lesson_one], schedule_of_lessons[index_lesson_two] = \
            schedule_of_lessons[index_lesson_two], schedule_of_lessons[index_lesson_one]
        if check_for_exercise(index_lesson_one):
            schedule_of_lessons.insert(index_lesson_two + 1, schedule_of_lessons.pop(index_lesson_one + 1))
        if check_for_exercise(index_lesson_two):
            schedule_of_lessons.insert(index_lesson_one + 1, schedule_of_lessons.pop(index_lesson_two + 1))


def exercise_lesson(lesson_title: str) -> bool:
    if lesson_title in schedule_of_lessons:
        find_index = schedule_of_lessons.index(lesson_title)
        if not check_for_exercise(find_index):
            schedule_of_lessons.insert(find_index + 1, f"{lesson_title}-Exercise")
    elif lesson_title not in schedule_of_lessons:
        schedule_of_lessons.append(lesson_title)
        schedule_of_lessons.append(f"{lesson_title}-Exercise")


commands = {
    "Add": add_lesson,
    "Insert": insert_lesson,
    "Remove": remove_lesson,
    "Swap": swap_lesson,
    "Exercise": exercise_lesson
}

command = input()

while command != "course start":
    command_type, *info = [int(x) if x.isdigit() else x for x in command.split(":")]
    commands[command_type](*info)
    command = input()

for pos, lesson in enumerate(schedule_of_lessons, 1):
    print(f"{pos}.{lesson}")




#
# lessons = input().split(", ")
# commands_ = input()
#
#
# def lesson_exist(lessons_title):
#     if lessons_title in lessons:
#         return True
#     return False
#
#
# def find_lesson_index(lesson_title):
#     return lessons.index(lesson_title)
#
#
# def check_for_exercise(index):
#     if len(lessons) - 1 > index:
#         if "Exercise" in lessons[index + 1]:
#             return True
#     return False
#
#     # try:
#     #     if "Exercise" in lessons[index + 1]:
#     #         return True
#     # except IndexError:
#     #     return False
#     #
#     # for pos, x in enumerate(lessons[index:]):
#     #     if pos == 1 and "Exercise" in x:
#     #         return True
#     #     if pos == 2:
#     #         return False
#     # return False
#
#
# def add_lesson(lessons_title):
#     if not lesson_exist(lessons_title):
#         lessons.append(lessons_title)
#
#
# def insert_lesson(lessons_title, index_to_insert):
#     if not lesson_exist(lessons_title):
#         lessons.insert(index_to_insert, lessons_title)
#
#
# def remove_lesson(lessons_title):
#     if lesson_exist(lessons_title):
#         index_lesson = find_lesson_index(lessons_title)
#         del lessons[index_lesson]
#         if check_for_exercise(index_lesson):
#             del lessons[index_lesson]
#
#
# def swap_lessons(lessons_title_one, lessons_title_two):
#     if lesson_exist(lessons_title_one) and lesson_exist(lessons_title_two):
#         lesson_one = find_lesson_index(lessons_title_one)
#         lesson_two = find_lesson_index(lessons_title_two)
#         lesson_one_exercise = check_for_exercise(lesson_one)
#         lesson_two_exercise = check_for_exercise(lesson_two)
#         if lesson_one_exercise and lesson_two_exercise:
#             lesson_one_exercise = lessons[lesson_one + 1]
#             lessons[lesson_one + 1] = lessons[lesson_two + 1]
#             lessons[lesson_two + 1] = lesson_one_exercise
#         elif lesson_one_exercise:
#             lesson_one_exercise = lessons.pop(lesson_one + 1)
#             lessons.insert(find_lesson_index(lessons_title_two) + 1, lesson_one_exercise)
#         elif lesson_two_exercise:
#             lesson_two_exercise = lessons.pop(lesson_two + 1)
#             lessons.insert(find_lesson_index(lessons_title_one) + 1, lesson_two_exercise)
#         lesson_one = find_lesson_index(lessons_title_one)
#         lesson_two = find_lesson_index(lessons_title_two)
#         lessons[lesson_one] = lessons_title_two
#         lessons[lesson_two] = lessons_title_one
#
#
# def exercise_lesson(lessons_title):
#     if lesson_exist(lessons_title):
#         lesson_index = find_lesson_index(lessons_title)
#         if not check_for_exercise(lesson_index):
#             lessons.insert(lesson_index + 1, f"{lessons_title}-Exercise")
#     else:
#         lessons.append(lessons_title)
#         lessons.append(f"{lessons_title}-Exercise")
#
#
# while commands_ != "course start":
#     type_command, *info = commands_.split(":")
#     if type_command == "Add":
#         add_lesson(info[0])
#     elif type_command == "Insert":
#         insert_lesson(info[0], int(info[-1]))
#     elif type_command == "Remove":
#         remove_lesson(info[0])
#     elif type_command == "Swap":
#         swap_lessons(info[0], info[-1])
#     elif type_command == "Exercise":
#         exercise_lesson(info[0])
#     commands_ = input()
#
# for pos, lesson in enumerate(lessons, 1):
#     print(f"{pos}.{lesson}")
