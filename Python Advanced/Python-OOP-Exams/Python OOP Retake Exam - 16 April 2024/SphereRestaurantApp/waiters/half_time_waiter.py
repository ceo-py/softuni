from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):
    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)

    def calculate_earnings(self):
        return self.hours_worked * 12.0

    def report_shift(self):
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."
