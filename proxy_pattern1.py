from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename):  # <-- fixed here
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading {self.filename} from disk...")

    def display(self):
        print(f"Displaying {self.filename}")

class ProxyImage(Image):
    def __init__(self, filename):  # <-- fixed here
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

def client_code(image: Image):
    image.display()

# Client code
proxy_image = ProxyImage("high_res_photo.jpg")
print("First call (image will load):")
client_code(proxy_image)
print("\nSecond call (image is cached):")
client_code(proxy_image)
