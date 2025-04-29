'''
=> Common ekta strcuter follow kore jeta shoabr jonno fixed
why use:
------------
==> Reuse the [ same work flow ] -->>But Customize Specific Class

==> Template → fixed workflow, with some customizable steps (e.g., Tea vs Coffee)
🧠 Think Broadly – More Real-Life Examples:
------------------------------------------------
    Online Orders:
    ==============

        Step 1: Login ✅

        Step 2: Choose Product ❗

        Step 3: Checkout ✅

        Step 4: Payment ❗
        → Each store (Amazon, Daraz) can customize product/purchase steps.

    Interview Process:
    ===================
        Step 1: Resume Screening ✅

        Step 2: Written Test ❗ (varies by company)

        Step 3: Final Interview ✅

'''

from abc import ABC, abstractmethod

# Base class (Template)
class TongMama(ABC):
    def prepare_recipe(self):
        self.boil_water()         # ✅ same for all
        self.brew()               # ❗ changes in subclass
        self.pour_in_cup()        # ✅ same for all
        self.add_masala()         # ❗ changes in subclass

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_masala(self):
        pass

# Concrete Class 1: Tea
class Tea(TongMama):
    def brew(self):
        print("Steeping the tea")

    def add_masala(self):
        print("Adding lemon")

# Concrete Class 2: Coffee
class Coffee(TongMama):
    def brew(self):
        print("Dripping coffee through filter")

    def add_masala(self):
        print("Adding sugar and milk")

# Client Code
print("Making tea...")
tea = Tea()
tea.prepare_recipe()

print("\nMaking coffee...")
coffee = Coffee()
coffee.prepare_recipe()
