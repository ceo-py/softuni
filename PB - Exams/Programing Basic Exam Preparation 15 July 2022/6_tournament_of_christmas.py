year = int(input())
year_dic = {}
while True:
    year_dic.clear()
    for i in str(year):
        year_dic.update({i: i})
    if len(year_dic.keys()) == len(str(year)):
        break
    else:
        year = int(year)
        year += 1
print(year)