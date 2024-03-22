from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST_RATE = 3.5
    INTEREST_INCREASE_RATE = 0.5
    LOAN_AMOUNT = 50_000.0
    LOAN_TYPE = 'MortgageLoan'

    def __init__(self):
        super().__init__(interest_rate = MortgageLoan.INTEREST_RATE, amount = MortgageLoan.LOAN_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += MortgageLoan.INTEREST_INCREASE_RATE
