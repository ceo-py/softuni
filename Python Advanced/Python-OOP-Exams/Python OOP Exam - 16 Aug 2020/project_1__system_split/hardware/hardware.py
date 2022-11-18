from project.functionality.valitaion import Validation
from project.software.software import Software


class Hardware:

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        Validation.enough_capacity(self.capacity, self.memory,
                                   self.software_components,
                                   software,
                                   "Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def __str__(self):
        output = [f"Hardware Component - {self.name}",
                  f"Express Software Components: {sum(1 for s in self.software_components if s.software_type == 'Express')}",
                  f"Light Software Components: {sum(1 for s in self.software_components if s.software_type == 'Light')}",
                  f"Memory Usage: {sum(s.memory_consumption for s in self.software_components)} / {self.memory}",
                  f"Capacity Usage: {sum(s.capacity_consumption for s in self.software_components)} / {self.capacity}",
                  f"Type: {self.hardware_type}",
                  f"Software Components: "]

        if self.software_components:
            output[-1] += ", ".join(s.name for s in self.software_components)
        else:
            output[-1] += "None"

        return "\n".join(output)


