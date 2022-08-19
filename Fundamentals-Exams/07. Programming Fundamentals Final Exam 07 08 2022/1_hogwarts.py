spell_deciphered = [input()]


def check_index(index_):
    if 0 <= index_ < len(spell_deciphered[0]):
        return True
    print("The spell was too weak.")


def abjuration():
    spell_deciphered[0] = spell_deciphered[0].upper()
    print(spell_deciphered[0])


def necromancy():
    spell_deciphered[0] = spell_deciphered[0].lower()
    print(spell_deciphered[0])


def illusion(index_, letter):
    if check_index(index_):
        spell_deciphered[0] = spell_deciphered[0][:index_] + letter + spell_deciphered[0][index_ + 1:]
        print("Done!")


def divination(first_substring, second_substring):
    if first_substring in spell_deciphered[0]:
        spell_deciphered[0] = spell_deciphered[0].replace(first_substring, second_substring)
        print(spell_deciphered[0])


def alteration(substring):
    if substring in spell_deciphered[0]:
        spell_deciphered[0] = spell_deciphered[0].replace(substring, "", 1)
        print(spell_deciphered[0])


allowed_commands = ["Abracadabra", "Abjuration", "Necromancy", "Illusion", "Divination", "Alteration"]

commmand = input()

while commmand != "Abracadabra":
    command_type = commmand.split()
    if command_type[0] not in allowed_commands:
        print("The spell did not work!")
    else:
        if command_type[0] == "Abjuration":
            abjuration()
        elif command_type[0] == "Necromancy":
            necromancy()
        elif command_type[0] == "Illusion":
            illusion(int(command_type[1]), command_type[2])
        elif command_type[0] == "Divination":
            divination(command_type[1], command_type[2])
        elif command_type[0] == "Alteration":
            alteration(command_type[1])
    commmand = input()











