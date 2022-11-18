from project.software.software import Software


class LightSoftware(Software):
    __CAPACITY_CONSUMPTION = 1.5
    __MEMORY_CONSUMPTION_consumption = 0.5
    __TYPE = "Light"

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, LightSoftware.__TYPE, int(capacity_consumption * LightSoftware.__CAPACITY_CONSUMPTION),
                         int(memory_consumption * LightSoftware.__MEMORY_CONSUMPTION_consumption))
