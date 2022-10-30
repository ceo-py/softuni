from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def __add_data(collection, item):
        if item not in collection:
            collection.append(item)

    def add_customer(self, customer: Customer):
        Gym.__add_data(self.customers, customer)

    def add_trainer(self, trainer: Trainer):
        Gym.__add_data(self.trainers, trainer)

    def add_equipment(self, equipment: Equipment):
        Gym.__add_data(self.equipment, equipment)

    def add_plan(self, plan: ExercisePlan):
        Gym.__add_data(self.plans, plan)

    def add_subscription(self, subscription: Subscription):
        Gym.__add_data(self.subscriptions, subscription)

    def subscription_info(self, subscription_id: int):

        # output = []
        # for info in (self.subscriptions,self.customers, self.trainers, self.equipment, self.plans):
        #     for x in info:
        #         if x.id == subscription_id:
        #             output.append(str(x))

        # output = [[str(x) for x in self.subscriptions if x.id == subscription_id][0],
        #           [str(x) for x in self.customers if x.id == subscription_id][0],
        #           [str(x) for x in self.trainers if x.id == subscription_id][0],
        #           [str(x) for x in self.equipment if x.id == subscription_id][0],
        #           [str(x) for x in self.plans if x.id == subscription_id][0]]

        return "\n".join(
            str(x) for info in (self.subscriptions, self.customers, self.trainers, self.equipment, self.plans)
            for x in info if x.id == subscription_id)
