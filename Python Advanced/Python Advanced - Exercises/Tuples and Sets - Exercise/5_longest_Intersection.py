import sys

lines = int(input())
max_intersection = -sys.maxsize
combined_intersection = set()
set_a = set()
set_b = set()

for i in range(lines):
    data = input().split("-")
    range_1 = [int(i) for i in data[0].split(",")]
    range_2 = [int(i) for i in data[1].split(",")]
    for i in range(range_1[0], range_1[1] + 1):
        set_a.add(i)
    for i in range(range_2[0], range_2[1] + 1):
        set_b.add(i)
    sets_intersection = set_a.intersection(set_b)
    if len(sets_intersection) > max_intersection:
        max_intersection = len(sets_intersection)
        combined_intersection = sets_intersection
    set_a.clear()
    set_b.clear()


print(f"Longest intersection is [", end="")
print(*combined_intersection, sep=", ", end="")
print(f"] with length {max_intersection}")


#
# lines_of_input = int(input())
#
# biggest_range = 0
# result_ = []
# for _ in range(lines_of_input):
#     first_intersection, second_intersection = input().split("-")
#     first_intersection = [int(num) for num in first_intersection.split(",") if num.isdigit()]
#     second_intersection = [int(num) for num in second_intersection.split(",") if num.isdigit()]
#     if first_intersection[1] > second_intersection[1]:
#         first_num = first_intersection[0]
#         if first_intersection[0] < second_intersection[0]:
#             first_num = second_intersection[0]
#         result_.append([first_num, second_intersection[-1]])
#     else:
#         first_num = first_intersection[0]
#         if first_intersection[0] < second_intersection[0]:
#             first_num = second_intersection[0]
#         result_.append([first_num, first_intersection[-1]])
#
# result_ = sorted(result_, key=lambda x: abs(x[0] - x[1]), reverse=True)
# longest_result = [x for x in range(result_[0][0], result_[0][1]+1)]
# print(f"Longest intersection is {longest_result} with length {len(longest_result)}")
#
