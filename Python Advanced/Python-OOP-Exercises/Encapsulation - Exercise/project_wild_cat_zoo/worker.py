class Worker:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = int(age)
        self.salary = int(salary)

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
