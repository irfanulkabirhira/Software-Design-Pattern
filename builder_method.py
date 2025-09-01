# Burger Class
class Burger:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.lettuce = False
        self.tomato = False

    def __str__(self):
        return (
            f"Burger size: {self.size}\n"
            f"Cheese: {self.cheese}\n"
            f"Pepperoni: {self.pepperoni}\n"
            f"Lettuce: {self.lettuce}\n"
            f"Tomato: {self.tomato}\n"
        )


# Burger Builder Class
class BurgerBuilder:
    def __init__(self, size):
        self.burger = Burger()
        self.burger.size = size

    def add_cheese(self):
        self.burger.cheese = True
        return self

    def add_pepperoni(self):
        self.burger.pepperoni = True
        return self

    def add_lettuce(self):
        self.burger.lettuce = True
        return self

    def add_tomato(self):
        self.burger.tomato = True
        return self

    def build(self):
        return self.burger


# Usage Example
if __name__ == "__main__":
    burger = (
        BurgerBuilder("Large")
        .add_cheese()
        .add_pepperoni()
        .add_tomato()
        .build()
    )

    print("🍔 Your Custom Burger Order:")
    print(burger)
