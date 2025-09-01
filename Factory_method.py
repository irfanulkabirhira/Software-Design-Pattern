from abc import ABC, abstractmethod

# Step 1 : Creating the Abstract Method
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# CStep 2 : Creating the Concrete Class
class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Triangle(Shape):
    def draw(self):
        return "Drawing a Triangle"

# step 3: Create a Factory to generate objects of concrete class
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "Rectangle":
            return Rectangle()
        elif shape_type == "Circle":
            return Circle()
        elif shape_type == "Triangle":
            return Triangle()
        else:
            return None


# Step 4 : Use the Facotory to get object of concrete class
class Factory_pattern:
    @staticmethod
    def main():
        # Create the Facotry
        shape_factor = ShapeFactory()

        # get an object of Rectangle and call it draw method
        shape1 = shape_factor.get_shape("Rectangle")
        print(shape1.draw())
        # get an object of Circle and call it draw method

        # get an object of Circle and Call it draw method
        shape2 = shape_factor.get_shape("Circle")
        print(shape2.draw())

        #get an object of Triangle and call it draw method
        shape3 = shape_factor.get_shape("Triangle")
        print(shape3.draw())


# Verify the output

if __name__ == "__main__":
    Factory_pattern.main()