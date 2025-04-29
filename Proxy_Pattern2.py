
''' ✅ Manager = Proxy
✅ Movie Star = Real Subject
✅ You = Client
YOU (Client)
   ↓
MANAGER (Proxy)
   ↓
CELEBRITY (Real Object)

'''

# Step 1: Interface
from abc import ABC, abstractmethod

class Celebrity(ABC):
    @abstractmethod
    def meet(self):
        pass

# Step 2: Real Object Class
class MovieStar(Celebrity):
    def __init__(self):
        self.arrange_meeting()

    def arrange_meeting(self):
        print("Arranging meeting with the Movie Star...")

    def meet(self):
        print("Meeting the Movie Star in person!")

# Step 3: Proxy Class
class ManagerProxy(Celebrity):
    def __init__(self):
        self.movie_star = None

    def meet(self):
        if self.movie_star is None:
            self.movie_star = MovieStar()
        self.movie_star.meet()

# Step 4: Client Code
def client_code(celebrity: Celebrity):
    celebrity.meet()

# Step 5: Using the Proxy
manager = ManagerProxy()

print("First Call: Meeting will be arranged and happen")
client_code(manager)

print("\nSecond Call: Meeting without arranging again")
client_code(manager)
