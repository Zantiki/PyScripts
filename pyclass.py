"""
A circle class
"""
import math

# inherits from object
class Circle(object):
    """the circle class (Effectively its own module)
    Another important note is that is is normal for class attributes in python to be exposed"""
    # Class variable
    version = "0.1"

    # make the instances lightweight if there are many of them by suppressing the object dictionary
    __slots__ = ["diameter"]

    # not a constructor, but initializes the instance variables
    def __init__(self, radius):
        self.radius = radius

    # convert dotted access to method calls
    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    # object method
    def area(self):
        """Calculate the circle radius"""
        return math.pi * self.radius ** 2.0

    # refers to an instance of this specific object if we call __perimeter (same goes for the subclass)
    def perimeter(self):
        """Calculate the circle perimeter"""
        return 2.0 * math.pi * self.radius

    # A static method since we do not need instance variables, and it is only valid for circles
    @staticmethod
    def angle_to_grade(angle):
        """Convert angles to gradients"""
        return math.tan(math.radians(angle)) * 100.0

    # Alternative constructor as a class method
    @classmethod
    def from_bbd(cls, bbd):
        """Construct a circle from a bbd"""
        radius = bbd / 2.0 / math.sqrt(2.0)
        # Returns a new class instance, since we cannot now what sub-class we are dealing with
        return cls(radius)


class Tire(Circle):
    """Tires are circles corrected for rubber width"""
    # Will override parent method
    def perimeter(self):
        """Calculate the perimeter of a tire"""
        # This return statement works as the tire is a specialisation of a circle, with the same attributes
        return Circle.perimeter(self) * 1.25


def main():
    """Run a test"""
    print("Circle version: {}".format(Circle.version))
    circle = Circle(10.0)
    tire = Tire(10.0)
    print("Your circle has a radius of {}".format(circle.radius))
    print("Your circle has an diameter of {}".format(circle.diameter))
    print("Your circle has an area of {}".format(circle.area()))
    print("Your tire has a perimeter of {}".format(tire.perimeter()))

    circle_2 = Circle.from_bbd(5)
    tire_2 = Tire.from_bbd(5)

    print("Your bbd_circle has an area of {}".format(circle_2.area()))
    print("Your bbd_circle has an diameter of {}".format(circle_2.diameter))
    print("Your bbd_circle has an radius of {}".format(circle_2.radius))

    print("Your bbd_tire has an perimeter of {}".format(tire_2.perimeter()))
    print("Your bbd_circle has an perimeter of {}".format(circle_2.perimeter()))


if __name__ == '__main__':
    main()

