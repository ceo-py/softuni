class Zoo:

    def __init__(self, name : str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        price = int(price)
        if self.__animal_capacity > len(self.animals) and price > self.__budget:
            return "Not enough budget"

        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for pos, x in enumerate(self.workers):
            if x.name == worker_name:
                del self.workers[pos]
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salary = sum(x.salary for x in self.workers)
        if workers_salary <= self.__budget:
            self.__budget -= workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tended_animals = sum(x.money_for_care for x in self.animals)
        if tended_animals <= self.__budget:
            self.__budget -= tended_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += int(amount)

    def animals_status(self):
        info = {"Cheetah": [], "Tiger": [], "Lion": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.animals]
        output = [f"You have {len(info['Cheetah']) + len(info['Tiger']) + len(info['Lion'])} animals",
                  f"----- {len(info['Lion'])} Lions:", *info['Lion'],
                  f"----- {len(info['Tiger'])} Tigers:", *info['Tiger'],
                 f"----- {len(info['Cheetah'])} Cheetahs:", *info['Cheetah']]
        return "\n".join(output)

    def workers_status(self):
        info = {"Keeper": [], "Vet": [], "Caretaker": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.workers]
        output = [f"You have {len(info['Keeper']) + len(info['Vet']) + len(info['Caretaker'])} workers",
                  f"----- {len(info['Keeper'])} Keepers:", *info['Keeper'],
                  f"----- {len(info['Caretaker'])} Caretakers:", *info['Caretaker'],
                 f"----- {len(info['Vet'])} Vets:", *info['Vet']]
        return "\n".join(output)

