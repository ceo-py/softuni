number = int(input())
word = input()

target_list = list()
no_filter = list()
for _ in range(number):
    text = input()
    no_filter.append(text)
    if word in text:
        target_list.append(text)

print(no_filter)
print(target_list)
