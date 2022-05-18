data_input = input()


class BankAccount:
    account_info = []

    def __init__(self, bank, name, balance):
        self.name = name
        self.bank = bank
        self.balance = float(balance)

    def __repr__(self):
        return f"{self.name} -> {self.balance:.2f} ({self.bank})"


while data_input != "end":
    info = data_input.split(" | ")
    BankAccount.account_info.append(BankAccount(*info))
    data_input = input()

[print(show) for show in sorted(BankAccount.account_info, key=lambda item: (-item.balance, len(item.bank)))]
