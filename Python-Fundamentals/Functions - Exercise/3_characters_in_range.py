character_one = input()
character_two = input()


def find_range_of_characters(one, two):
    one = int(ord(one) + 1)
    two = int(ord(two))
    for n in range(one, two):
        print(chr(n), end=" ")


find_range_of_characters(character_one, character_two)
