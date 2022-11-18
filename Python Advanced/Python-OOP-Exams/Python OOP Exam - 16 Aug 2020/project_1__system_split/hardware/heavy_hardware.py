from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    __TYPE = "Heavy"
    __CAPACITY_SPACE = 2
    __MEMORY_SPACE = 0.75

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, HeavyHardware.__TYPE, capacity_consumption * HeavyHardware.__CAPACITY_SPACE,
                         int(memory_consumption * HeavyHardware.__MEMORY_SPACE))

