number_of_user_names = int(input())
names = set()
for name in range(number_of_user_names):
    names.add(input())

print("\n".join(names))


#
#
#
#
#
#
#
#
#
#
# number_of_user_names = int(input())
# names = [input() for _ in range(number_of_user_names)]
# print("\n".join(set(names)))