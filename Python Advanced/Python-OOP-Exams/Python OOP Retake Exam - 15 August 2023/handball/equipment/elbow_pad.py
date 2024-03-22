from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PROTECTION = 90
    price = 25.0

    def __init__(self):
        super().__init__(protection=ElbowPad.PROTECTION, price=ElbowPad.price)
        self.type_equipment = 'ElbowPad'

    def increase_price(self):
        self.price *= 1.1
