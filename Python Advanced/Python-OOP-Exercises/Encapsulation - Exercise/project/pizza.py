from project.topping import Topping

class Pizza:
    def __init__(self, name: str, dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        value = int(value)
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        if self.__toppings_capacity == len(self.toppings):
            raise ValueError("Not enough space for another topping")
        self.toppings[topping.topping_type] = self.toppings.get(topping.topping_type, 0) + topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())





# import unittest
#
# from dough import Dough
#
#
#
# class Tests(unittest.TestCase):
#     def test_topping_init(self):
#         t = Topping("Tomato", 20)
#         self.assertEqual(t.topping_type, "Tomato")
#         self.assertEqual(t.weight, 20)
#
#     def test_topping_topping_type_error(self):
#         with self.assertRaises(ValueError) as ve:
#             t = Topping("", 20)
#         self.assertEqual("The topping type cannot be an empty string", str(ve.exception))
#
#     def test_topping_weight_error(self):
#         with self.assertRaises(ValueError) as ve:
#             t = Topping("a", -1)
#         self.assertEqual("The weight cannot be less or equal to zero", str(ve.exception))
#
#     def test_dough_init(self):
#         d = Dough("Sugar", "Mixing", 20)
#         self.assertEqual(d.flour_type, "Sugar")
#         self.assertEqual(d.baking_technique, "Mixing")
#         self.assertEqual(d.weight, 20)
#
#     def test_dough_flour_type_error(self):
#         with self.assertRaises(ValueError) as ve:
#             d = Dough("", 'ab', 20)
#         self.assertEqual("The flour type cannot be an empty string", str(ve.exception))
#
#     def test_dough_baking_technique_error(self):
#         with self.assertRaises(ValueError) as ve:
#             d = Dough("ab", '', 20)
#         self.assertEqual("The baking technique cannot be an empty string", str(ve.exception))
#
#     def test_dough_weight_error(self):
#         with self.assertRaises(ValueError) as ve:
#             t = Dough("a", 'ab', -1)
#         self.assertEqual("The weight cannot be less or equal to zero", str(ve.exception))
#
#     def test_pizza_init(self):
#         d = Dough("Sugar", "Mixing", 20)
#         p = Pizza("Burger", d, 5)
#
#         self.assertEqual(p.name, "Burger")
#         self.assertEqual(p.dough, d)
#         self.assertEqual(len(p.toppings), 0)
#         self.assertEqual(p.toppings_capacity, 5)
#
#     def test_pizza_add_topping_error(self):
#         d = Dough("Sugar", "Mixing", 20)
#         t = Topping("Tomato", 20)
#         p = Pizza("Burger", d, 1)
#         p.add_topping(t)
#         with self.assertRaises(ValueError) as ctx:
#             p.add_topping(t)
#         self.assertEqual("Not enough space for another topping", str(ctx.exception))
#
#     def test_pizza_add_topping_new(self):
#         d = Dough("Sugar", "Mixing", 20)
#         t = Topping("Tomato", 20)
#         p = Pizza("Burger", d, 200)
#         p.add_topping(t)
#
#         self.assertEqual(p.toppings["Tomato"], 20)
#         self.assertEqual(len(p.toppings), 1)
#
#     def test_pizza_add_topping_update(self):
#         d = Dough("Sugar", "Mixing", 20)
#         t = Topping("Tomato", 20)
#         p = Pizza("Burger", d, 200)
#         p.add_topping(t)
#         p.add_topping(t)
#
#         self.assertEqual(p.toppings["Tomato"], 40)
#
#     def test_pizza_calculate_total_weight(self):
#         d = Dough("Sugar", "Mixing", 20)
#         t = Topping("Tomato", 20)
#         p = Pizza("Burger", d, 200)
#         p.add_topping(t)
#         p.add_topping(t)
#
#         self.assertEqual(p.calculate_total_weight(), 60)
#
#
# if __name__ == '__main__':
#     unittest.main()