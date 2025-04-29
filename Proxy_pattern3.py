'''
Exercise: Virtual Art Gallery with Lazy
Loading
 • Scenario:
 You are building a Virtual Art Gallery app.
 The gallery has many high-resolution paintings — loading all at once
would be slow and memory-intensive.
 • You need to use the Proxy Pattern to load the paintings on demand
— only when a visitor clicks on them.



'''

from abc import ABC , abstractmethod

class Art(ABC):
    @abstractmethod
    def show_art(self):
        pass



class RealArt(Art):
    pass

    def show_art(self):
        pass



class proxyArt(Art):
    pass
    def show_art(self):
        pass

def client_code(art : Art ):
    art.show_art()



prxy_obejct = proxyArt()

print("1st the Art will Be Loaded ")
client_code(prxy_obejct)

print("\n Second the Art will be showing")
client_code(prxy_obejct)
