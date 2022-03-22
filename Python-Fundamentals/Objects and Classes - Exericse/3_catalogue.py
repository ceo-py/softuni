class Catalogue:

    def __init__(self, name):
        self.name = str(name)
        self.products = []

    def add_product(self, product_name):
        self.products.append(str(product_name))

    def get_by_letter(self, first_letter):
        return [x for x in self.products if x.startswith(first_letter)]

    def __repr__(self):
        self.products.sort()
        show_result = "Items in the {0} catalogue:\n" \
                 "{1}".format(self.name, '\n'.join(self.products))
        return show_result


# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
