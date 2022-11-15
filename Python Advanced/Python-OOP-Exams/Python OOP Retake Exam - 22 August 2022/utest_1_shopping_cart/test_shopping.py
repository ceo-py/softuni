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
