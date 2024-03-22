from project.Validation.validation import Validation
from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []


    @property
    def loan_types(self):
        return {
            'StudentLoan': StudentLoan,
            'MortgageLoan': MortgageLoan,
        }

    @property
    def client_types(self):
        return {
            'Student': Student,
            'Adult': Adult,
        }

    @staticmethod
    def __get_item(key: str, key_value: str, collection:  list):
        for obj in collection:
            if getattr(obj, key) == key_value:
                return obj

    def __get_all_loans_from_type(self, type_loan: str) -> list:
        return [l for l in self.loans if l.LOAN_TYPE == type_loan]

    def __get_bank_statistic(self):
        output = {'active clients': len(self.clients),
                  'total income': sum(c.income for c in self.clients),
                  'granted loans': 0,
                  'granted loans sum': 0,
                  'not granted loans': 0,
                  'not granted loans sum': 0,
                  'avr client interest rate': 0}
        for c in self.clients:
            output['granted loans'] += len(c.loans)
            output['granted loans sum'] += sum(l.amount for l in c.loans)
            output['avr client interest rate'] += c.interest

        output['not granted loans'] += len(self.loans)
        output['not granted loans sum'] += sum(l.amount for l in self.loans)

        try:
            output['avr client interest rate'] /= len(self.clients)
        except ZeroDivisionError:
            pass
        return output




    def add_loan(self, loan_type: str):
        Validation.is_type_correct(loan_type, self.loan_types, 'Invalid loan type!')

        self.loans.append(self.loan_types[loan_type]())
        return f'{loan_type} was successfully added.'

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        Validation.is_type_correct(client_type, self.client_types, 'Invalid client type!')

        if self.capacity <= len(self.clients):
            return 'Not enough bank capacity.'

        self.clients.append(self.client_types[client_type](client_name, client_id, income))
        return f'{client_type} was successfully added.'

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.__get_item('client_id', client_id, self.clients)
        loan = self.__get_item('LOAN_TYPE', loan_type, self.loans)

        client.can_get_loan(loan_type)
        client.add_loan(loan)
        self.loans.remove(loan)

        return f'Successfully granted {loan_type} to {client.name} with ID {client_id}.'

    def remove_client(self, client_id: str):
        client = self.__get_item('client_id', client_id, self.clients)

        if not client:
            Validation.no_such_client('No such client!')

        client.check_if_has_loans()

        self.clients.remove(client)
        return f'Successfully removed {client.name} with ID {client_id}.'

    def increase_loan_interest(self, loan_type: str):
        all_loans_from_type = [l.increase_interest_rate() for l in self.__get_all_loans_from_type(loan_type)]

        return f'Successfully changed {len(all_loans_from_type)} loans.'

    def increase_clients_interest(self, min_rate: float):
        all_clients_below_min_rate = [c.increase_clients_interest() for c in self.clients if c.interest < min_rate]

        return f'Number of clients affected: {len(all_clients_below_min_rate)}.'

    def get_statistics(self):
        bank = self.__get_bank_statistic()
        output = [
            f'Active Clients: {bank["active clients"]}',
            f'Total Income: {bank["total income"]:.2f}',
            f'Granted Loans: {bank["granted loans"]}, Total Sum: {bank["granted loans sum"]:.2f}',
            f'Available Loans: {bank["not granted loans"]}, Total Sum: {bank["not granted loans sum"]:.2f}',
            f'Average Client Interest Rate: {bank["avr client interest rate"]:.2f}',
        ]
        return '\n'.join(output)
