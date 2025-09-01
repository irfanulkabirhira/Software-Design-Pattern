class Burger:
    def __init__(self):
        self.size = None
        self.peparoni = False

    def __str__(self):
        return(
            f"Burger Size : {self.size}\n"
            f"Peparoni: {self.peparoni}\n"
               )

class BurgerBuilder:
    def __init__(self, size):
        self.burger = Burger()
        self.burger.size=size

    def add_peparoni(self):
        self.burger.peparoni = True
        return self

    def build(self):
        return self.burger



burger = BurgerBuilder("Larger")
burger.add_peparoni()
final_burger = burger.build()

print("My Burger order is : ")
print(final_burger)



