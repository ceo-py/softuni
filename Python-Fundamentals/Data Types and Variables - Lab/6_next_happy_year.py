year = int(input()) + 1

while len(set(str(year))) != len(str(year)):
    year += 1

print(year)

#
#
# year = int(input())
#
# result = {}
# while len(result.keys()) != len(str(year)):
#     result = {}
#     year += 1
#     for num in str(year):
#         result[num] = num
#
#
# print(year)
#
#


# years = int(input()) + 1
#
# find_year = False
#
# while not find_year:
#     find_year = True
#     for num in range(len(str(years))):
#         if str(years).count(str(years)[num]) != 1:
#             years = int(years) + 1
#             find_year = False
#             break
#
# print(years)

