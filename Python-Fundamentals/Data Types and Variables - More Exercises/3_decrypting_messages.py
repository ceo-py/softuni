key = int(input())
line = int(input())

word = list()

for _ in range(line):
    letter = input()

    to_check = ord(letter) + key
    word.append(chr(to_check))

for letter in word:
    print(letter, end="")
