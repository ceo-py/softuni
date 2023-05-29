key = int(input())
print(*[chr(ord(input()) + key) for _ in range(int(input()))], sep ="")


#
# key = int(input())
# line = int(input())
#
# word = list()
#
# for _ in range(line):
#     letter = input()
#     word.append(chr(ord(letter) + key))
#
# print(*word, sep="")
#





# key = int(input())
# line = int(input())
#
# word = list()
#
# for _ in range(line):
#     letter = input()
#
#     to_check = ord(letter) + key
#     word.append(chr(to_check))
#
# for letter in word:
#     print(letter, end="")
