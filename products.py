"""
Module containing product information
"""
class Product:
    """
    This modul represents a specific product type
    available in the store (for example, MacBook Air M2).
    It encapsulates information about the product, including its name and price.
    """
    def __init__(self, name:str, price:float, quantity:int)-> None:
        self.name = name
        self.price = price
        self.quantity = quantity

        if name == "" or name.isspace():
            raise ValueError('The product name cannot be left blank.')
        self.name = name

        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError('"price" must be a non‑negative number.')
        self.price = price

        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError('"quantity" must be an integer and must not be negative.')
        self.quantity = quantity

        self.active = True

    def get_quantity(self)-> int:
        """
        Getter method for the set.
        Returns the set (int).
        """
        return self.quantity

    def set_quantity(self, quantity: int)-> None:
        """
        Setter method for the count.
        When the count reaches 0, the product is deactivated.
        """
        if quantity == 0:
            self.active = False

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

    def buy(self, quantity: int)-> float:
        """
        Purchases a specified quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the product quantity.
        """
        if quantity < 0:
            raise ValueError('"quantity" must not be negative.')
        if quantity > self.quantity:
            raise ValueError(f"You can only buy up to {self.quantity} units.")

        total_price = round(self.price * quantity, 2)
        self.quantity -= quantity
        return total_price
