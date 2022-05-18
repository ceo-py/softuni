class Party:
    def __init__(self):
        self.people = []


party_people = Party()
data_input = input()
while data_input != "End":
    party_people.people.append(data_input)
    data_input = input()

print(f"Going: {', '.join(party_people.people)}")
print(f"Total: {len(party_people.people)}")

# class Party:
#     def __init__(self):
#         self.name = []
#
#     def add_people(self, names):
#         self.name.append(names)
#
#
# party_people = Party()
#
# names_given = input()
#
# while names_given != "End":
#     party_people.add_people(names_given)
#     names_given = input()
#
# print("Going:", end=" ")
# print(*party_people.name, sep=", ")
# print(f"Total: {len(party_people.name)}")
