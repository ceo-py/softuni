number_of_inputs = int(input())

pyramidic = {}

for consecutive in range(number_of_inputs):
    symbols = input()

    for s in symbols:
        if s not in pyramidic:
            pyramidic[s] = [1]
    if not consecutive:
        continue
    symbols_len = len(symbols)
    current_letter = ''
    for i, s in enumerate(symbols):
        symbols_unique = set(symbols[i: i + 2])
        if i + 2 <= symbols_len and len(symbols_unique) == 1 and symbols_unique.pop() == s:
            current_letter += s
        else:
            current_letter += s
            if len(current_letter) > 1:
                pyramidic[s].append(len(current_letter))
            current_letter = ''

max_repeat_letter = ''
max_repeat = 0
max_time_repeat = 0

for l, repeat in pyramidic.items():
    counter = 1
    repeat_times = 0
    for number_repeat in repeat:
        if counter <= number_repeat and max_repeat < number_repeat:
            max_repeat_letter = l
            max_repeat = number_repeat
            repeat_times += 1
            max_time_repeat += 1
        counter += 2

for r in range(1, max_time_repeat * 2, 2):
    print(max_repeat_letter * r)
'''
5
asdfghjkl
asdgggjkl
asgggggkl
agggggggl
ggggggggg

7
abcdefg
aaadc\\
cbaaaaa
d
ddddasd
!!ddddd!!!!!!!!...
dddddddd
'''