import datetime
from collections import deque


class Factory:
    robots = []
    staring_time = None
    products_on_line = deque()

    def __init__(self, name: str, process_time: int):
        self.name = name
        self.process_time = process_time
        self.busy_until = self.staring_time

    def getting_item(self):
        self.busy_until = self.staring_time + datetime.timedelta(0, self.process_time)

    @staticmethod
    def adding_time():
        Factory.staring_time += datetime.timedelta(0, 1)


robot_data_list = input().split(";")
hours, minutes, seconds = [int(x) for x in input().split(":")]
Factory.staring_time = datetime.datetime(100, 1, 1, hours, minutes, seconds)
product = input()

while product != "End":
    Factory.products_on_line.append(product)
    product = input()

for robot_data in robot_data_list:
    name, process = [int(x) if x.isdigit() else x for x in robot_data.split("-")]
    Factory.robots.append(Factory(name, process))

while Factory.products_on_line:
    Factory.adding_time()
    item = Factory.products_on_line.popleft()

    for robot in Factory.robots:
        if Factory.staring_time >= robot.busy_until:
            robot.getting_item()
            print(f'{robot.name} - {item} [{Factory.staring_time.time()}]')
            break
    else:
        Factory.products_on_line.append(item)






# import datetime
# from collections import deque
#
# robot_data_list = input().split(";")
# starting_time = input()
# command_product = input()
# hours, minutes, seconds = [int(x) for x in starting_time.split(":")]
# starting_time = datetime.datetime(100, 1, 1, hours, minutes, seconds)
#
#
# def adding_processing_time_to_robots(time_, star_time="No"):
#     global starting_time
#     if star_time != "No":
#         return starting_time + datetime.timedelta(0, time_)
#     starting_time += datetime.timedelta(0, time_)
#     return starting_time
#
#
# product_line_robots = {}
# for robot_info in robot_data_list:
#     name, busy_until = robot_info.split("-")
#     product_line_robots[name] = product_line_robots.get(name, {})
#     product_line_robots[name]["process time"] = int(busy_until)
#     product_line_robots[name]["busy until"] = starting_time
#
# products_in_line = deque()
#
# while command_product != "End":
#     products_in_line.append(command_product)
#     command_product = input()
#
# while products_in_line:
#     adding_processing_time_to_robots(1)
#     item_to_process = products_in_line.popleft()
#     for robot in product_line_robots:
#         if starting_time >= product_line_robots[robot]["busy until"]:
#             product_line_robots[robot]["busy until"] = adding_processing_time_to_robots(
#                 product_line_robots[robot]["process time"], "Yes")
#             print(f'{robot} - {item_to_process} [{starting_time.time()}]')
#             break
#         else:
#             products_in_line.append(item_to_process)
#
#
#
#
#
#


#
# from collections import deque
#
#
# def convert_str_to_seconds(str_time):
#     hours, minutes, seconds = [int(x) for x in str_time.split(':')]
#     return hours * 60 * 60 + minutes * 60 + seconds
#
#
# def convert_seconds_to_str_time(seconds):
#     hours = seconds // (60 * 60)
#     seconds %= (60 * 60)
#     minutes = seconds // 60
#     seconds %= 60
#     return f'{hours:02d}:{minutes:02d}:{seconds:02d}'
#
#
# robots_data = input().split(';')
# process_time_by_robot = {}
# busy_until_by_robot = {}
#
# for robot_data in robots_data:
#     name, process_time = robot_data.split('-')
#     process_time_by_robot[name] = int(process_time)
#     busy_until_by_robot[name] = -1
#
# time = convert_str_to_seconds(input())
# items = deque()
# line = input()
#
# while line != "End":
#     items.append(line)
#     line = input()
#
# while items:
#     time = (time + 1) % 24 * 60 * 60
#     item = items.popleft()
#
#     for name, busy_until in busy_until_by_robot.items():
#         if time >= busy_until:
#             busy_until_by_robot[name] = time + process_time_by_robot[name]
#             print(f'{name} - {item} [{convert_seconds_to_str_time(time)}]')
#             break
#     else:
#         items.append(item)
#
