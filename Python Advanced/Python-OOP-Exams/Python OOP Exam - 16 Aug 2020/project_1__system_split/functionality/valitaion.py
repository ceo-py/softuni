class Validation:

    @staticmethod
    def enough_capacity(capacity: int, total_memory: int, software_objects: list, software: object, message: str):
        if sum(
                s.capacity_consumption for s in software_objects) + software.capacity_consumption > capacity or sum(
                s.memory_consumption for s in software_objects) + software.memory_consumption > total_memory:
            raise Exception(message)

    @staticmethod
    def hardware_exists(hardware_name: str, hardware_list: list, message: str):
        for h in hardware_list:
            if h.name == hardware_name:
                return h

        return message

    @staticmethod
    def find_item(item_name: str, item_list_with_names: list):
        for i in item_list_with_names:
            if i.name == item_name:
                return i

        return "No item"
