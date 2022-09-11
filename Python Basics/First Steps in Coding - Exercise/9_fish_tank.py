a = int(input())
b = int(input())
c = int(input())
d = float(input())/100

cm = a * b * c
litri = cm * 0.001
total = litri * (1 - d)
print(total)