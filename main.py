"""
A simple program that allows users to
add, delete, list, and sort products via the CLI
"""
from store import Store
from products import Product

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[39m\033[49m"

def initial_stock_of_inventory():
    """
    List of products available in the store
    """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    return Store(product_list)

def list_products(store: Store):
    """
    Lists all products in the store.
    """
    print(f"\n{GREEN}Products in store:{RESET}")
    products = store.get_all_products()

    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
    print("-" * 6)

def show_total(store: Store):
    """
    Shows the total quantity of all products in the store.
    """
    total = store.get_total_quantity()
    print(f"\nTotal of {RED}{total}{RESET} items in store")

def make_order(store: Store):
    """
    Lets the user select a product and quantity, then places an order.
    """
    print("\nAvailable products:")
    active_products = store.get_all_products()

    for idx, product in enumerate(active_products, start=1):
        print(f"{GREEN}{idx}{RESET}. {product.name} "
              f"(Price: {product.price}, "
              f"Quantity: {product.quantity})")
    print("-" * 6)
    print("When you want to finish order, enter empty text.")

    # PRODUCT LOOP
    while True:
        selection_input = input("Which product # do you want? ").strip()
        if selection_input == "":
            return

        try:
            selection = int(selection_input) - 1
            if selection < 0 or selection >= len(active_products):
                print("Please enter a valid product number.\n")
                continue
            product = active_products[selection]   # Python IndexError
            break
        except ValueError:
            print("Please enter a valid product number.\n")
            continue

    # QUANTITY LOOP
    while True:
        quantity_input = input("What amount do you want? ").strip()
        if quantity_input == "":
            return

        try:
            quantity = int(quantity_input)
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        try:
            total_price = store.order([(product, quantity)])
            print(f"\n{GREEN}Order successful!{RESET} Total price: {RED}${total_price}{RESET}")
            return
        except Exception as e:
            print(f"{e}\n")

def quit_program(_store):
    """ Quit Program """
    print("Goodbye!")
    raise SystemExit

def start(store: Store):
    """
    Full menu loop using a dispatch table with integer input validation.
    """

    actions = {
        1: list_products,
        2: show_total,
        3: make_order,
        4: quit_program
    }

    while True:
        print("\n   Store Menu")
        print("   " + 10 * "-")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit\n")

        choice = get_menu_choice("Please choose a number: ")

        action = actions.get(choice)

        if action:
            action(store)
        else:
            print()

def get_menu_choice(prompt: str) -> int:
    """
    Reads a numeric menu choice from the user.
    """
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")

def main():
    """
    Initializes the store and starts the program.
    """
    shop = initial_stock_of_inventory()
    start(shop)


if __name__ =="__main__":
    main()
