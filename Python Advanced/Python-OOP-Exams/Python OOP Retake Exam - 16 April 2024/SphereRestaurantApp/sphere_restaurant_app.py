from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient


class SphereRestaurantApp:
    def __init__(self):
        self.waiters = []
        self.clients = []

    @property
    def waiter_types(self):
        return {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}

    @property
    def client_types(self):
        return {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def __find_object_by_attribute(self, text: str, attribute: str, collection: list) -> object:
        for obj in collection:
            if getattr(obj, attribute) == text:
                return obj

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.waiter_types:
            return f"{waiter_type} is not a recognized waiter type."

        if any(w.name == waiter_name for w in self.waiters):
            return f"{waiter_name} is already on the staff."

        self.waiters.append(self.waiter_types[waiter_type](
            waiter_name, hours_worked))
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.client_types:
            return f"{client_type} is not a recognized client type."

        if any(c.name == client_name for c in self.clients):
            return f"{client_name} is already a client."

        self.clients.append(self.client_types[client_type](client_name))

        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = self.__find_object_by_attribute(
            waiter_name, "name", self.waiters)

        if not waiter:
            return f"No waiter found with the name {waiter_name}."
        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = self.__find_object_by_attribute(
            client_name, "name", self.clients)

        if not client:
            return f"{client_name} is not a registered client."

        return f"{client_name} earned {client.earning_points(order_amount)} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = self.__find_object_by_attribute(
            client_name, "name", self.clients)

        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount_percentage, remaining_points = client.apply_discount()

        return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

    def generate_report(self):
        output = ["$$ Monthly Report $$",
                  f"Total Earnings: ${sum(w.calculate_earnings() for w in self.waiters):.2f}",
                  f"Total Clients Unused Points: {sum(c.points for c in self.clients)}",
                  f"Total Clients Count: {len(self.clients)}",
                  f"** Waiter Details **",
                  *[str(w) for w in sorted(self.waiters,
                                           key=lambda w: -w.calculate_earnings())],
                  ]

        return "\n".join(output)

