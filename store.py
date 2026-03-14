""" Stores products """

from products import Product

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[39m\033[49m"

class Store:
    """ The Store class will contain a variable—a list of products available in the store. """
    def __init__(self, products):
        """ Initializes the store. """
        if products is None:
            products = []
        self.products = list(products)

    def add_product(self, product):
        """ Adds a product to the store. """

        if not isinstance(product, Product):
            raise TypeError(f"Product must be an {RED}instance of Product{RESET}.")
        self.products.append(product)

    def remove_product(self, product):
        """ Removes a product from the store. """
        if not isinstance(product, Product):
            raise TypeError(f"Product must be an {RED}instance of Product{RESET}.")
        self.products.remove(product)

    def get_total_quantity(self)->int:
        """ Returns the total quantity of the store. """

        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self)->list:
        """ Returns a list of all active products in the store. """

        active_products = []
        for product in self.products:
            if product.active:
                active_products.append(product)

        return active_products

    def order(self, shopping_list) -> float:
        """
        Receives a list of tuples, where each tuple contains:
        (Product instance, quantity as int)
        """

        total_price = 0

        for product, quantity in shopping_list:

            if product not in self.products:
                raise ValueError(f'Product "{GREEN}{product.name}{RESET}" {RED}not found{RESET} in store.')

            if not product.active:
                raise ValueError(f'"{GREEN}{product.name}{RESET}" is {RED}not in stock{RESET}.')

            total_price += product.buy(int(quantity))

        return total_price
