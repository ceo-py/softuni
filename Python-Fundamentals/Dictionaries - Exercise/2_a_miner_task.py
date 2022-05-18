resourse = input()

total_resourse = dict()
while resourse != "stop":
    quantity = int(input())
    total_resourse[resourse] = total_resourse.get(resourse, 0)
    total_resourse[resourse] += quantity
    resourse = input()

for key, value in total_resourse.items():
    print(f"{key} -> {value}")
