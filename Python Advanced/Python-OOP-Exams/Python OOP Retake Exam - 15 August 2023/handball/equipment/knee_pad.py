from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PROTECTION = 120
    price = 15.0

    def __init__(self):
        super().__init__(protection=KneePad.PROTECTION, price=KneePad.price)
        self.type_equipment = 'KneePad'

    def increase_price(self):
        self.price *= 1.2
