exercise_list = []


class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems.split(", ")


data_input = input()
while data_input != "go go go":
    topic, course_name, judge_contest_link, *problem = data_input.split(" -> ")
    exercise_list.append(Exercise(topic, course_name, judge_contest_link, *problem))
    data_input = input()

for show in exercise_list:
    print(f"Exercises: {show.topic}")
    print(
        f'Problems for exercises and homework for the "{show.course_name}" course @ SoftUni.\n'
        f'Check your solutions here: {show.judge_contest_link}')
    for pos, i in enumerate(show.problems, 1):
        print(f"{pos}. {i}")
