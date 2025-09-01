# Product class
class Computer:
    def __init__(self):
        self.processor = None
        self.ram = None
        self.storage = None
        self.graphics_card = None
        self.os = None

    def __str__(self):
        return (f"Computer Specifications:\n"
                f"Processor: {self.processor}\n"
                f"RAM: {self.ram}\n"
                f"Storage: {self.storage}\n"
                f"Graphics Card: {self.graphics_card}\n"
                f"Operating System: {self.os}")


# Builder class
class ComputerBuilder:
    def __init__(self, processor, ram):
        self.computer = Computer()
        self.computer.processor = processor
        self.computer.ram = ram

    def add_storage(self, storage):
        self.computer.storage = storage
        return self

    def add_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card
        return self

    def add_os(self, os):
        self.computer.os = os
        return self

    def build(self):
        return self.computer


# Using the builder
my_pc = (ComputerBuilder("Intel i9", "32GB")
         .add_storage("1TB SSD")
         .add_graphics_card("NVIDIA RTX 4080")
         .add_os("Windows 11")
         .build())

print(my_pc)
