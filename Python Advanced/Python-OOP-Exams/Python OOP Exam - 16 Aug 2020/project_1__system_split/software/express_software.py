from project.software.software import Software


class ExpressSoftware(Software):
    __MEMORY_CONSUMPTION = 2
    __TYPE = "Express"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, ExpressSoftware.__TYPE, capacity_consumption,
                         memory_consumption * ExpressSoftware.__MEMORY_CONSUMPTION)
