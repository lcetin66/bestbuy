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
        if not isinstance(products, list):
            raise TypeError("Products must be a list of Product instances.")
        
        for item in products:
            if not isinstance(item, Product):
                raise TypeError(f"All items in the products list must be {RED}Product instances{RESET}.")
                
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

        if product not in self.products:
             raise ValueError(f'Product "{GREEN}{product.name}{RESET}" {RED}not found{RESET} in store.')

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
        if not isinstance(shopping_list, list):
            raise TypeError("Shopping list must be a list of (Product, quantity) tuples.")

        total_price = 0
        for item in shopping_list:
            if not isinstance(item, (list, tuple)) or len(item) != 2:
                raise TypeError("Each item in the shopping list must be a (Product, quantity) tuple.")
            
            product, quantity = item
            
            if not isinstance(product, Product):
                raise TypeError(f"The first element of each tuple must be an {RED}instance of Product{RESET}.")
            if not isinstance(quantity, int):
                raise TypeError(f"The second element of each tuple (quantity) must be an {RED}integer{RESET}.")

            if product not in self.products:
                raise ValueError(f'Product "{GREEN}{product.name}{RESET}" {RED}not found{RESET} in store.')

            if not product.active:
                raise ValueError(f'"{GREEN}{product.name}{RESET}" is {RED}not in stock{RESET}.')

            total_price += product.buy(quantity)

        return total_price
