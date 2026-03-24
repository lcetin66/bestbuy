"""
Module containing product information
"""
RED = "\033[91m"
RESET = "\033[39m\033[49m"

class Product:
    """
    This modul represents a specific product type
    available in the store (for example, MacBook Air M2).
    It encapsulates information about the product, including its name and price.
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        if not isinstance(name, str):
            raise TypeError(f"Product name must be a {RED}string{RESET}.")
        if name == "" or name.isspace():
            raise ValueError(f"The product name {RED}cannot be left blank{RESET}.")

        if not isinstance(price, (int, float)):
             raise TypeError(f'"price" must be a {RED}number{RESET}.')
        if price < 0:
            raise ValueError(f'"price" must be a {RED}non-negative number{RESET}.')

        if not isinstance(quantity, int):
            raise TypeError(f'"quantity" must be an {RED}integer{RESET}.')
        if quantity < 0:
            raise ValueError(f'"quantity" must {RED}not be negative{RESET}.')

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    def get_quantity(self)-> int:
        """
        Getter method for the set.
        Returns the set (int).
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Setter method for the count.
        When the count reaches 0, the product is deactivated.
        """
        if not isinstance(quantity, int):
            raise TypeError(f'"quantity" must be an {RED}integer{RESET}.')
        if quantity < 0:
            raise ValueError(f'"quantity" must {RED}not be negative{RESET}.')

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self)-> bool:
        """
        Getter method for active.
        Returns True if the product is active, otherwise False.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product
        """
        self.active = False

    def show(self):
        """
        Prints a string representing the product to the console, for example:
        'MacBook Air M2, Price: 1450, Quantity: 100'
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        Purchases a specified quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the product quantity.
        """
        if not isinstance(quantity, int):
            raise TypeError(f'"quantity" must be an {RED}integer{RESET}.')

        if not self.active:
            raise ValueError(f'Product "{self.name}" is {RED}inactive{RESET} and cannot be purchased.')

        if quantity < 0:
            raise ValueError(f'"quantity" must {RED}not be negative{RESET}.')
        if quantity > self.quantity:
            raise ValueError(f"You can only buy up to {RED}{self.quantity}{RESET} units.")

        total_price = round(self.price * quantity, 2)
        self.set_quantity(self.quantity - quantity)
        return total_price
