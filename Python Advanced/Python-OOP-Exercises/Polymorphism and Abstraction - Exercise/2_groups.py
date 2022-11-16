class Person:
    def __init__(self, name: str, surname: str):
        self.surname = surname
        self.name = name

    def __add__(self, obj):
        return Person(self.name, obj.surname)

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name:str, people: list):
        self.people = people
        self.name = name

    def __len__(self):
        return len(self.people)

    def __add__(self, obj):
        return Group(f"{self.name} {obj.name}", self.people + obj.people)

    def __getitem__(self, index):
        return f"Person {index}: {str(self.people[index])}"

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(x) for x in self.people)}"


aaa = [1,2,3,4]

for x in aaa:




p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')

p3 = p0 + p1
print(p3.name)
print(p3.surname)
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3



first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

# print(len(first_group))
# print(second_group)
# print(third_group[0])

# for person in third_group:
#     print(person)


for person in first_group:
    print(person)