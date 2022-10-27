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
        cheetah, tigers, lions = [], [], []
        for x in self.animals:
            if x.__class__.__name__ == "Cheetah":
                cheetah.append(str(x))
            elif x.__class__.__name__ == "Tiger":
                tigers.append(str(x))
            elif x.__class__.__name__ == "Lion":
                lions.append(str(x))
        output = [f"You have {len(cheetah) + len(tigers) + len(lions)} animals",
                  f"----- {len(lions)} Lions:", *lions, f"----- {len(tigers)} Tigers:", *tigers,
                 f"----- {len(cheetah)} Cheetahs:", *cheetah]
        return "\n".join(output)

    def workers_status(self):
        keeper, vet, caretaker = [], [], []
        for x in self.workers:
            if x.__class__.__name__ == "Keeper":
                keeper.append(str(x))
            elif x.__class__.__name__ == "Vet":
                vet.append(str(x))
            elif x.__class__.__name__ == "Caretaker":
                caretaker.append(str(x))
        output = [f"You have {len(keeper) + len(vet) + len(caretaker)} workers",
                  f"----- {len(keeper)} Keepers:", *keeper, f"----- {len(caretaker)} Caretakers:", *caretaker,
                 f"----- {len(vet)} Vets:", *vet]
        return "\n".join(output)

