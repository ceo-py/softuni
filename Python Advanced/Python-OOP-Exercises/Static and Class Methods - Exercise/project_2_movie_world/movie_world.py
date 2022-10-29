from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def __get_customer(self, id):
        return [customer for customer in self.customers if id == customer.id][0]

    def __get_dvd(self, id):
        return [x for x in self.dvds if x.id == id][0]

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        find_dvd = self.__get_dvd(dvd_id)
        find_customer = self.__get_customer(customer_id)

        if find_dvd in find_customer.rented_dvds:
            return f"{find_customer.name} has already rented {find_dvd.name}"

        if find_dvd.is_rented:
            return "DVD is already rented"

        if find_customer.age < find_dvd.age_restriction:
            return f"{find_customer.name} should be at least {find_dvd.age_restriction} to rent this movie"

        find_customer.rented_dvds.append(find_dvd)
        find_dvd.is_rented = True
        return f"{find_customer.name} has successfully rented {find_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        find_dvd = self.__get_dvd(dvd_id)
        find_customer = self.__get_customer(customer_id)

        if find_dvd in find_customer.rented_dvds:
            find_customer.rented_dvds.remove(find_dvd)
            find_dvd.is_rented = False
            return f"{find_customer.name} has successfully returned {find_dvd.name}"

        return f"{find_customer.name} does not have that DVD"

    def __repr__(self):
        output = ""
        for x in self.customers:
            output += f"{str(x)}\n"
        for x in self.dvds:
            output += f"{str(x)}\n"
        return output.rstrip()
    


