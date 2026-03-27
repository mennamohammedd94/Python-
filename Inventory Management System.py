class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = product

    def update_stock(self, name, quantity):
        if name in self.products:
            self.products[name].quantity += quantity

    def show_inventory(self):
        for product in self.products.values():
            print(product.name, product.quantity)


# Example
inv = Inventory()
inv.add_product(Product("Laptop", 10))
inv.add_product(Product("Mouse", 50))

inv.update_stock("Laptop", 5)
inv.show_inventory()