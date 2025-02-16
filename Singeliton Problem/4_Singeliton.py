class Restaurant:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            # Creating a Restaurant
            print("Creating a Restaurant ....")
            cls._instance = super(Restaurant, cls).__new__(cls)
            cls._instance.orders = []
            cls._instance.menu = []
            cls._instance.waiter_list = ["waiter1", "waiter2", "waiter3"]  # List of allowed waiters
        return cls._instance

    # Adding Menu
    def add_to_menu(self, dish):
        if dish not in self.menu:
            self.menu.append(dish)
            print(f"{dish} added to the menu.")
        else:
            print(f"{dish} is already on the menu.")

    # Showing menu
    def show_menu(self):
        if self.menu:
            print("Menu is:", self.menu)
        else:
            print("Menu is currently empty.")

    # Placing orders (only if the waiter is in the waiter_list)
    def place_order(self, order, waiter):
        if waiter not in self.waiter_list:
            print(f"Sorry, {waiter} is not allowed to place orders.")
            return
        if order not in self.orders:
            self.orders.append(order)
            print(f"Order '{order}' has been placed by {waiter}.")
        else:
            print(f"Order '{order}' is already in the list.")

    # Showing the orders
    def show_orders(self):
        if self.orders:
            print("Current Orders:", self.orders)
        else:
            print("No orders have been placed.")

    # Removing the orders
    def remove_orders(self, dish):
        if dish in self.menu:
            self.menu.remove(dish)
            print(f"{dish} has been removed from the menu.")
        else:
            print(f"{dish} is not in the menu.")

    # Showing the removed orders
    def show_remove(self):
        print("Current Menu is:", self.menu)


# Main program loop to take user input
def main():
    restaurant = Restaurant()

    while True:
        print("\nOptions:")
        print("1. Add to Menu")
        print("2. Show Menu")
        print("3. Place Order")
        print("4. Show Orders")
        print("5. Remove from Menu")
        print("6. Show Removed Menu")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            dish = input("Enter the dish to add to the menu: ")
            restaurant.add_to_menu(dish)

        elif choice == '2':
            restaurant.show_menu()

        elif choice == '3':
            order = input("Enter the dish to order: ")
            waiter = input("Enter the waiter's name: ")
            restaurant.place_order(order, waiter)

        elif choice == '4':
            restaurant.show_orders()

        elif choice == '5':
            dish = input("Enter the dish to remove from the menu: ")
            restaurant.remove_orders(dish)

        elif choice == '6':
            restaurant.show_remove()

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 7.")

# Run the program
if __name__ == "__main__":
    main()
