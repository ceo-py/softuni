from project.Validation.validation import Validation
from project.clients.base_client import BaseClient


class Student(BaseClient):
    INITIAL_INTEREST = 2.0
    INCREASE_INTEREST_RATE = 1.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=Student.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += Student.INCREASE_INTEREST_RATE

    @staticmethod
    def can_get_loan(loan_type: str):
        if loan_type != 'StudentLoan':
            Validation.cant_be_granted('Inappropriate loan type!')
