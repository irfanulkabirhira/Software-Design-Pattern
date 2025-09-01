class Restaurant:
    # instance name er ekta protected varibale declare korlam , and initially None rhaklam [ Class Instance]
    _instance = None
    # Class method --> 1 bar e use korte parbo
    def __new__(cls):
        if cls._instance is None :
            # Creating a Restarant
            print("Initialize the Restatant Kitecne....")
            # initialize korteci Restaurant
            cls._instance = super(Restaurant , cls).__new__(cls)
            cls._instance.orders = []
            cls._instance.menu = []
            # Return the single instance
        return cls._instance


    # Adding Menu
    def add_to_menu(self , dish):
        if dish not in self.menu:
            self.menu.append(dish)
            print(f"{dish} has been added to the menue..<3")
        else:
            print(f"{dish} is already on the manue")

    # Showing menue
    def show_menu(self):
        print("Menu is ", self.menu)

    # Placing the orders
    def place_order(self, order):
        if order not in self.orders:
            self.orders.append(order)

    # Showing the orders
    def show_orders(self):
        print("Current Order is : ", self.orders)

    # Removed the orders
    def remove_orders(self , dish):
        if dish in self.menu:
            self.menu.remove(dish)
            print(f"{dish} has been removed from the list")
        else :
            print(f"{dish} is not in the menu")

    #Showing the Removed Order
    def show_remove(self):
        print("Current  Mene is : " ,self.menu)



# Creating Obejct of Restaurant Class
waiter1 = Restaurant()

# adding Menu
waiter1.add_to_menu("pasta")

#Showing Menu
waiter1.show_menu()

# Placing Orders
waiter1.place_order("pasta")

# Showing the orders
waiter1.show_orders()

#Removig the Order
waiter1.remove_orders("pasta")

# Showing the removing Orders
waiter1.show_remove()

