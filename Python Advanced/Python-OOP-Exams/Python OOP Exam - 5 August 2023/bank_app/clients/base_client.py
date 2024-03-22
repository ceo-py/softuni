from abc import ABC, abstractmethod

from project.Validation.validation import Validation


class BaseClient(ABC):

    def __init__(self, name: str, client_id: str, income: float, interest: float):
        self.name = name
        self.client_id = client_id
        self.income = income
        self.interest = interest
        self.loans = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.empty_or_white_space(value, 'Client name cannot be empty!')
        self.__name = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        Validation.symbols_are_long(value, 10, 'Client ID should be 10 symbols long!')
        self.__client_id = value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value):
        Validation.number_is_less_than(value, 0.0, 'Income must be greater than zero!')
        self.__income = value

    @abstractmethod
    def increase_clients_interest(self):
        pass

    def add_loan(self, loan: object):
        self.loans.append(loan)

    def check_if_has_loans(self):
        if self.loans:
            Validation.has_loan('The client has loans! Removal is impossible!')
