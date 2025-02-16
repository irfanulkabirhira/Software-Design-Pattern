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
        else:
            print(f"{dish} is already on the menu")

    # Showing menu
    def show_menu(self):
        print("Menu is:", self.menu)

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
        print("Current Orders:", self.orders)

    # Removing the orders
    def remove_orders(self, dish):
        if dish in self.menu:
            self.menu.remove(dish)
            print(f"{dish} has been removed from the menu")
        else:
            print(f"{dish} is not in the menu")

    # Showing the removed orders
    def show_remove(self):
        print("Current Menu is:", self.menu)


# Creating Object of Restaurant Class
restaurant = Restaurant()

# Adding Menu
restaurant.add_to_menu("pasta")
restaurant.add_to_menu("burger")

# Showing Menu
restaurant.show_menu()

# Placing Orders
restaurant.place_order("pasta", "waiter1")  # Allowed waiter
restaurant.place_order("burger", "waiter4")  # Not an allowed waiter

# Showing Orders
restaurant.show_orders()

# Removing an Order from Menu
restaurant.remove_orders("pasta")

# Showing the Removed Menu
restaurant.show_remove()
