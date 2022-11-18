from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    __TYPE = "Power"
    __CAPACITY_SPACE = 0.25
    __MEMORY_SPACE = 1.75

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, PowerHardware.__TYPE, int(capacity_consumption * PowerHardware.__CAPACITY_SPACE),
                         int(memory_consumption * PowerHardware.__MEMORY_SPACE))
