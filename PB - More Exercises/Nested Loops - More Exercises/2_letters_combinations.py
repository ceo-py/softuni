import itertools

first_letter = input()
second_letter = input()
skip_letter = input()

lower_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

index_letter_one = lower_a.index(first_letter)
index_letter_two = lower_a.index(second_letter)
checking_letters = lower_a[index_letter_one:index_letter_two + 1]
if skip_letter in checking_letters:
    index_skip_letter = checking_letters.index(skip_letter)
    del checking_letters[index_skip_letter]
combinations_count = 0

for r in range(3, 4):
    for s in itertools.product(checking_letters, repeat=r):
        print(''.join(s), end=" ")
        combinations_count += 1

print(combinations_count)
