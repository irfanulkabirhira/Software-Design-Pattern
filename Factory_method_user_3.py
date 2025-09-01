from abc import ABC, abstractmethod

# Step 1 : Creating the Abstract Method
class MenuItem(ABC):
    @abstractmethod
    def serve(self):
        pass


# Step 2 : Creating the Concrete Classes
class VegMeal(MenuItem):
    def serve(self):
        return "Serving a Veg Meal."


class NonVegMeal(MenuItem):
    def serve(self):
        return "Serving a Non-Veg Meal."


class Drink(MenuItem):
    def serve(self):
        return "Serving a Drink."


# Step 3 : Create a Factory to generate objects of concrete class
class MenuFactory:
    available_items = ["VegMeal", "NonVegMeal", "Drink"]

    @staticmethod
    def get_item(item_type):
        if item_type not in MenuFactory.available_items:
            return None

        if item_type == "VegMeal":
            return VegMeal()
        elif item_type == "NonVegMeal":
            return NonVegMeal()
        elif item_type == "Drink":
            return Drink()
        else:
            return None

    @staticmethod
    def remove_item(item_type):
        if item_type in MenuFactory.available_items:
            MenuFactory.available_items.remove(item_type)
            print(f"{item_type} has been removed from the menu.")
        else:
            print(f"{item_type} not found in the menu.")


# Step 4 : Use the Factory to get object of concrete class
class Factory_pattern:
    @staticmethod
    def main():
        menu_factory = MenuFactory()

        while True:
            print("\n--- Menu ---")
            print("1. Order VegMeal")
            print("2. Order NonVegMeal")
            print("3. Order Drink")
            print("4. Remove Item from Menu")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                item = menu_factory.get_item("VegMeal")
                if item:
                    print(item.serve())
                else:
                    print("VegMeal is not available.")

            elif choice == "2":
                item = menu_factory.get_item("NonVegMeal")
                if item:
                    print(item.serve())
                else:
                    print("NonVegMeal is not available.")

            elif choice == "3":
                item = menu_factory.get_item("Drink")
                if item:
                    print(item.serve())
                else:
                    print("Drink is not available.")

            elif choice == "4":
                remove_choice = input("Enter item to remove (VegMeal, NonVegMeal, Drink): ").strip()
                menu_factory.remove_item(remove_choice)

            elif choice == "5":
                print("Exiting... Thank you!")
                break

            else:
                print("Invalid choice! Please try again.")


# Step 5 : Verify the output
if __name__ == "__main__":
    Factory_pattern.main()
