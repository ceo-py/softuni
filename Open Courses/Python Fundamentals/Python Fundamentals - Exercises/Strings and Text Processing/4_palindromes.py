result = {x: x for x in input().split() if x == x[::-1]}
print(", ".join((sorted(result.keys(), key=str.lower))))

#
# result = [x for x in input().split() if x == x[::-1]]
# print(", ".join((sorted(list(set(result)), key=str.lower))))
