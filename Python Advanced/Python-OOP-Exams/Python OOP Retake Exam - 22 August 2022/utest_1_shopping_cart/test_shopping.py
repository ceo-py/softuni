from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestGunit(TestCase):

    def setUp(self) -> None:
        self.shop_card = ShoppingCart("Playstore", 100)

    def test_init(self):
        self.shop_card = ShoppingCart("Playstore", 100)
        shop_name = "Playstore"
        budget = 100
        self.assertEqual(shop_name, self.shop_card.shop_name)
        self.assertEqual(budget, self.shop_card.budget)
        self.assertEqual({}, self.shop_card.products)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as error:
            self.shop_card.shop_name = "playstore"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(error.exception))

    def test_successful_add_to_card(self):
        product_name = "Music DVD"
        product_price = 10
        result = self.shop_card.add_to_cart(product_name, product_price)
        self.shop_card.add_to_cart("two", 1)
        self.assertEqual(f"{product_name} product was successfully added to the cart!", result)
        self.assertEqual({product_name: product_price, "two": 1}, self.shop_card.products)
        self.assertTrue(product_name in self.shop_card.products)
        self.assertTrue(product_price == self.shop_card.products[product_name])

    def test_successful_add_to_card_over_price(self):
        product_name = "Music DVD"
        product_price = 100

        with self.assertRaises(ValueError) as error:
            self.shop_card.add_to_cart(product_name, product_price)

        self.assertEqual(f"Product {product_name} cost too much!", str(error.exception))
        self.assertEqual(0, len(self.shop_card.products))

    def test_successful_remove_from_card(self):
        product_name = "Music DVD"
        product_price = 100
        self.shop_card.products = {product_name: product_price, "two": 1}
        result = self.shop_card.remove_from_cart(product_name)
        self.assertEqual(f"Product {product_name} was successfully removed from the cart!", result)
        self.assertEqual(1, len(self.shop_card.products))

    def test_unsuccessful_remove_from_card(self):
        product_name = "Music DVD"

        with self.assertRaises(ValueError) as error:
            self.shop_card.remove_from_cart(product_name)

        self.assertEqual(f"No product with name {product_name} in the cart!", str(error.exception))
        self.assertTrue(product_name not in self.shop_card.products)

    def test_adding_two_instances(self):
        shop1 = ShoppingCart("Free", 200)
        shop1.products = {"money": 100}
        shop2 = ShoppingCart("Gpu", 300)
        shop2.products = {"4090": 5000}
        merge_shop = shop1 + shop2
        merge_products = {"money": 100,
                          "4090": 5000}

        self.assertEqual("FreeGpu", merge_shop.shop_name)
        self.assertEqual(500, merge_shop.budget)
        self.assertEqual(merge_products, merge_shop.products)

    def test_successful_buy_products(self):
        self.shop_card.products = {"Pen": 10,
                                   "Paper": 40}
        total_sum = sum(self.shop_card.products.values())

        self.assertEqual(f'Products were successfully bought! Total cost: {total_sum:.2f}lv.',
                         self.shop_card.buy_products())
        self.assertTrue("Pen" in self.shop_card.products)
        self.assertTrue("Paper" in self.shop_card.products)

    def test_unsuccessful_buy_products(self):
        self.shop_card.products = {"Pen": 100,
                                   "Paper": 400}
        total_sum = sum(self.shop_card.products.values())

        with self.assertRaises(ValueError) as error:
            self.shop_card.buy_products()

        self.assertEqual(
            f"Not enough money to buy the products! Over budget with {total_sum - self.shop_card.budget:.2f}lv!",
            (str(error.exception)))
        self.assertTrue(total_sum > sum(self.shop_card.products.values()))


if __name__ == "__main__":
    main()


#
#
# from 1_christmas_pastry_shop.shopping_cart import ShoppingCart
# from unittest import TestCase, main
#
#
# class GtestUnit(TestCase):
#
#     def setUp(self):
#         self.name = "TopGun"
#         self.budget = 130.00
#         self.product1 = ("Fire Arm", 45.00)
#         self.product2 = ("Fire Blast", 99.00)
#         self.new_shop_cart = ShoppingCart(self.name, self.budget)
#
#     def test_init_correct(self):
#         self.assertEqual(self.name, self.new_shop_cart.shop_name)
#         self.assertEqual(self.budget, self.new_shop_cart.budget)
#         self.assertEqual({}, self.new_shop_cart.products)
#
#     def test_init_incorrect(self):
#         error_msg = "Shop must contain only letters and must start with capital letter!"
#
#         with self.assertRaises(ValueError) as error:
#             ShoppingCart(self.name.lower(), self.budget)
#
#         self.assertEqual(error_msg, str(error.exception))
#
#         with self.assertRaises(ValueError) as error:
#             ShoppingCart("Test9", self.budget)
#
#         self.assertEqual(error_msg, str(error.exception))
#
#         with self.assertRaises(ValueError) as error:
#             ShoppingCart(" test9", self.budget)
#
#         self.assertEqual(error_msg, str(error.exception))
#
#     def test_successfully_added_to_card(self):
#         result = self.new_shop_cart.add_to_cart(*self.product1)
#         result1 = self.new_shop_cart.add_to_cart(*self.product2)
#         correct_msg = f"{self.product1[0]} product was successfully added to the cart!"
#         correct_msg1 = f"{self.product2[0]} product was successfully added to the cart!"
#         self.assertEqual(correct_msg, result)
#         self.assertEqual(correct_msg1, result1)
#         self.assertEqual(2, len(self.new_shop_cart.products))
#
#     def test_unsuccessfully_added_to_card(self):
#         product_name = "Engine"
#         error_msg = f"Product {product_name} cost too much!"
#         with self.assertRaises(ValueError) as error:
#             self.new_shop_cart.add_to_cart(product_name, 100)
#
#         self.assertEqual(error_msg, str(error.exception))
#
#     def test_successfully_remove_item_from_card(self):
#         correct_msg = f"Product {self.product1[0]} was successfully removed from the cart!"
#         self.new_shop_cart.add_to_cart(*self.product1)
#         self.new_shop_cart.add_to_cart(*self.product2)
#         self.assertTrue(self.product1[0] in self.new_shop_cart.products)
#         result = self.new_shop_cart.remove_from_cart(self.product1[0])
#         self.assertEqual(correct_msg, result)
#         self.assertEqual({"Fire Blast": 99.00}, self.new_shop_cart.products)
#
#     def test_unsuccessfully_remove_item_from_card(self):
#         error_msg = f"No product with name {self.product1[0]} in the cart!"
#         self.new_shop_cart.add_to_cart(*self.product2)
#
#         self.assertTrue(self.product2[0] in self.new_shop_cart.products)
#         with self.assertRaises(ValueError) as error:
#             self.new_shop_cart.remove_from_cart(self.product1[0])
#
#         self.assertEqual(error_msg, str(error.exception))
#         self.assertTrue(self.product1[0] not in self.new_shop_cart.products)
#
#     def test_add_another_shopping_instance(self):
#         shop_data = ("Airport", 460.00)
#         shop2 = ShoppingCart(*shop_data)
#         self.new_shop_cart.add_to_cart(*self.product1)
#         shop2.add_to_cart(*self.product2)
#         new_shop = self.new_shop_cart + shop2
#         self.assertEqual(f"{self.name}{shop_data[0]}", new_shop.shop_name)
#         self.assertEqual(460 + self.budget, new_shop.budget)
#         self.assertTrue(self.product1[0] in new_shop.products)
#         self.assertTrue(self.product2[0] in new_shop.products)
#
#     def test_successfully_buy_products(self):
#         correct_msg = f'Products were successfully bought! Total cost: {self.product1[1]:.2f}lv.'
#         self.new_shop_cart.add_to_cart(*self.product1)
#         result = self.new_shop_cart.buy_products()
#         self.assertEqual(correct_msg, result)
#         self.assertTrue(self.new_shop_cart.budget >= sum(self.new_shop_cart.products.values()))
#
#     def test_unsuccessfully_buy_products(self):
#         error_msg = f"Not enough money to buy the products! Over budget with {(self.product1[1] + self.product2[1]) - self.new_shop_cart.budget:.2f}lv!"
#
#         self.new_shop_cart.add_to_cart(*self.product1)
#         self.new_shop_cart.add_to_cart(*self.product2)
#
#         with self.assertRaises(ValueError) as error:
#             self.new_shop_cart.buy_products()
#
#         self.assertEqual(error_msg, str(error.exception))
#         self.assertTrue(self.product1[1] + self.product2[1] > self.new_shop_cart.budget)
#
# if __name__ == '__main__':
#     main()
