from Assignment.ItemToPurchase import ItemToPurchase
from Assignment.ShoppingCart import ShoppingCart


class ShoppingApp:
    def __init__(self):
        self.shopping_cart = None

    def start(self):
        # Prompt for customer name and date
        customer_name = input("Enter customer's name: ")
        current_date = input("Enter today's date: ")

        print(f"Customer name: {customer_name}")
        print(f"Today's date: {current_date}")

        # Create a ShoppingCart object
        self.shopping_cart = ShoppingCart(customer_name, current_date)

        # Launch the menu
        self.print_menu()

    def print_menu(self):
        while True:
            print("\nMENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit")
            option = input("Choose an option: ").lower()

            if option == 'a':
                self.add_item_to_cart()
            elif option == 'r':
                self.remove_item_from_cart()
            elif option == 'c':
                self.change_item_quantity()
            elif option == 'i':
                self.shopping_cart.print_descriptions()
            elif option == 'o':
                self.shopping_cart.print_total()
            elif option == 'q':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def add_item_to_cart(self):
        print("ADD ITEM TO CART")
        name = input("Enter the item name: ")
        description = input("Enter the item description: ")
        price = float(input("Enter the item price: "))
        quantity = int(input("Enter the item quantity: "))
        self.shopping_cart.add_item(ItemToPurchase(name, price, quantity, description))

    def remove_item_from_cart(self):
        print("REMOVE ITEM FROM CART")
        item_name = input("Enter name of item to remove: ")
        self.shopping_cart.remove_item(item_name)

    def change_item_quantity(self):
        print("CHANGE ITEM QUANTITY")
        name = input("Enter the item name: ")
        quantity = int(input("Enter the new quantity: "))
        self.shopping_cart.modify_item(ItemToPurchase(name, quantity=quantity))
