a = int(input())
b = int(input())
c = int(input())
d = int(input())

aa = (a + 2) * 1.50
bb = (11 * 1.1) * 14.50
cc = c * 5
expense = aa + bb + cc + 0.40
workers = (expense * 0.30) * d
total = expense + workers
print(total)