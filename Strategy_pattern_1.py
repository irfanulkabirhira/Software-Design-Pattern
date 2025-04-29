

'''
==> chosiing an algo dynamically without changing the main code
==> Strategy → choose behavior at runtime (e.g., Travel methods)
'''
from abc import ABC , abstractmethod
# Strategy Interface
class TravelStrategy(ABC):
    @abstractmethod
    def travel(self):
        pass

# Concrete Strategies
class CarStrategy(TravelStrategy):
    def travel(self):
        return "Traveling by Car: Fast but costly."

class BusStrategy(TravelStrategy):
    def travel(self):
        return "Traveling by Bus: Affordable but slow."

class BikeStrategy(TravelStrategy):
    def travel(self):
        return "Traveling by Bike: Eco-friendly but tiring."

# Context
class TravelContext:
    def __init__(self, strategy: TravelStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: TravelStrategy):
        self.strategy = strategy

    def travel(self):
        return self.strategy.travel()

# Client
traveler = TravelContext(CarStrategy())
print(traveler.travel())   # Car travel

traveler.set_strategy(BusStrategy())
print(traveler.travel())   # Bus travel

traveler.set_strategy(BikeStrategy())
print(traveler.travel())   # Bike travel
