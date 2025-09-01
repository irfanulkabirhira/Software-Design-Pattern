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
        # Create the Factory
        menu_factory = MenuFactory()

        # Get and serve VegMeal
        item1 = menu_factory.get_item("VegMeal")
        if item1:
            print(item1.serve())

        # Get and serve NonVegMeal
        item2 = menu_factory.get_item("NonVegMeal")
        if item2:
            print(item2.serve())

        # Get and serve Drink
        item3 = menu_factory.get_item("Drink")
        if item3:
            print(item3.serve())



        # Remove NonVegMeal
        print("\nRemoving 'NonVegMeal'...\n")
        menu_factory.remove_item("NonVegMeal")

        # Try to serve NonVegMeal after removal
        item4 = menu_factory.get_item("NonVegMeal")
        if item4:
            print(item4.serve())
        else:
            print("NonVegMeal is no longer available.")


# Step 5 : Verify the output
if __name__ == "__main__":
    Factory_pattern.main()
