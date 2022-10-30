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
        return f"Person {index}: {self.people[index].name} {self.people[index].surname}"

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(x) for x in self.people)}"


