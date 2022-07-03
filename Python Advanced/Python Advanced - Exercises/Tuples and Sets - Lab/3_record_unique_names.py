number_of_names = int(input())

names = set()

for _ in range(number_of_names):
    names.add(input())

print("\n".join(names))



#
# number_of_names = int(input())
#
# names = [input() for _ in range(number_of_names)]
# print("\n".join(set(names)))