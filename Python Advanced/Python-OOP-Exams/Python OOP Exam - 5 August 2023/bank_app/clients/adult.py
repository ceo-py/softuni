from project.Validation.validation import Validation
from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INITIAL_INTEREST = 4.0
    INCREASE_INTEREST_RATE = 2.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=Adult.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += Adult.INCREASE_INTEREST_RATE

    @staticmethod
    def can_get_loan(loan_type: str):
        if loan_type != 'MortgageLoan':
            Validation.cant_be_granted('Inappropriate loan type!')
