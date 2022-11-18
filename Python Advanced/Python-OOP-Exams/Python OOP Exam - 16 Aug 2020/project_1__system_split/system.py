from project.functionality.valitaion import Validation
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = Validation.hardware_exists(hardware_name, System._hardware, "Hardware does not exist")

        if isinstance(hardware, str):
            return hardware

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = Validation.hardware_exists(hardware_name, System._hardware, "Hardware does not exist")

        if isinstance(hardware, str):
            return hardware

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):

        hardware = Validation.find_item(hardware_name, System._hardware)
        software = Validation.find_item(software_name, System._software)

        if isinstance(hardware, str) or isinstance(software, str):
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        output = ["System Analysis",
                  f"Hardware Components: {len(System._hardware)}",
                  f"Software Components: {len(System._software)}",
                  f"Total Operational Memory: {sum(s.memory_consumption for s in System._software)} / {sum(h.memory for h in System._hardware)}",
                  f"Total Capacity Taken: {sum(s.capacity_consumption for s in System._software)} / {sum(h.capacity for h in System._hardware)}"]

        return "\n".join(output)

    @staticmethod
    def system_split():
        return "\n".join(str(h) for h in System._hardware)





