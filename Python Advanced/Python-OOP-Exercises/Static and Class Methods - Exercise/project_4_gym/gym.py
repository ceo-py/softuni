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

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

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
