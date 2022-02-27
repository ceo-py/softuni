number = int(input())

for i in range(1, number + 1):
    print(i * "*")
m = i
for n in range(1, number):
    m = m - 1
    print(m * "*")
