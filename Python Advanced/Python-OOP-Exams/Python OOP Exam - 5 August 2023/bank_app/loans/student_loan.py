from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INTEREST_RATE = 1.5
    INTEREST_INCREASE_RATE = 0.2
    LOAN_AMOUNT = 2_000.0
    LOAN_TYPE = 'StudentLoan'

    def __init__(self):
        super().__init__(interest_rate = StudentLoan.INTEREST_RATE, amount = StudentLoan.LOAN_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += StudentLoan.INTEREST_INCREASE_RATE
