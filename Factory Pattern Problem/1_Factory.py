from abc import ABC, abstractmethod

# Step 1: Create an interface for menu items
class MenuItem(ABC):
    @abstractmethod
    def serve(self):
        pass


# Step 2: Create concrete classes implementing the interface
class VegMeal(MenuItem):
    def serve(self):
        return "Serving a Veg Meal."


class NonVegMeal(MenuItem):
    def serve(self):
        return "Serving a Non-Veg Meal."


class Drink(MenuItem):
    def serve(self):
        return "Serving a Drink."


# Step 3: Create a Factory class to generate menu items
class MenuFactory:
    menu_items = {
        "VEGMEAL": VegMeal,
        "NONVEGMEAL": NonVegMeal,
        "DRINK": Drink
    }

    @staticmethod
    def get_item(item_type):
        item_type = item_type.upper()
        if item_type in MenuFactory.menu_items:
            return MenuFactory.menu_items[item_type]()
        return None

    @staticmethod
    def remove_item(item_type):
        item_type = item_type.upper()
        if item_type in MenuFactory.menu_items:
            del MenuFactory.menu_items[item_type]
            print(f"{item_type} has been removed from the menu.")
        else:
            print(f"{item_type} not found in the menu.")


# Step 4: Use the Factory to get and remove menu items
class Restaurant:
    @staticmethod
    def main():
        menu_factory = MenuFactory()

        # Get and serve menu items
        item1 = menu_factory.get_item("VegMeal")
        if item1:
            print(item1.serve())

        item2 = menu_factory.get_item("NonVegMeal")
        if item2:
            print(item2.serve())

        item3 = menu_factory.get_item("Drink")
        if item3:
            print(item3.serve())

        print("\nRemoving 'NonVegMeal' from the menu...\n")
        menu_factory.remove_item("NonVegMeal")

        # Try to order NonVegMeal after removal
        item4 = menu_factory.get_item("NonVegMeal")
        if item4:
            print(item4.serve())
        else:
            print("NonVegMeal is no longer available.")


# Step 5: Verify the output
if __name__ == "__main__":
    Restaurant.main()