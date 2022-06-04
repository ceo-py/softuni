numbers = list(map(int, input().strip().split(" ")))
[numbers.remove(min(numbers)) for _ in range(int(input()))]
print(", ".join(str(x) for x in numbers))






# numbers = list(map(int,input().strip().split(" ")))
# how_many_numbers_to_remove = int(input())
#
# for n in range(how_many_numbers_to_remove):
#     numbers.remove(min(numbers))
# print(", ".join(str(x) for x in numbers))



# numbers = list(map(int,input().strip().split(" ")))
# how_many_numbers_to_remove = int(input())
#
# for n in range(how_many_numbers_to_remove):
#     numbers.remove(min(numbers))
# count = 1
# for o in numbers:
#     if count != (len(numbers)):
#         print(f"{o},", end=" ")
#
#     else:
#         print(f"{o}")
#     count += 1
