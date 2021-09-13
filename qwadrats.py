
from math import sqrt
import math

'''Quadrilateral, Trapezoid, Parallelogram, Rectangle and Square'''

"""definition first method"""


class Quadrilateral:
    def __init__(self, side_a, side_b, side_c, side_d):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.side_d = side_d

    def def_area(self):

        s = (self.side_a * self.side_b) / 2

        g = sqrt(self.side_a**2 + self.side_b**2)

        p = (self.side_a + self.side_b + self.side_c + self.side_d) / 2

        s2 = sqrt(p * (p - g) * (p - self.side_c) * (p - self.side_d))
        return s + s2


qw = Quadrilateral(1, 19, 10, 11)
print(qw.def_area())


class Trapezoid(Quadrilateral):
    """Aspects"""

    def __init__(self, side_a, side_b, side_c, side_d):
        "initializazion class of parents"
        super().__init__(1, 3, 4, 5)
        self.h = 3

    def area_trapezoid(self):

        return (self.side_a * self.side_b) / 2 * self.h


tr = Trapezoid(1, 3, None, None)
print(tr.area_trapezoid())


class Paralelogram(Quadrilateral):
    """Aspects"""

    def __init__(self, side_a, side_b, side_c, side_d):
        "initializazion class of parents"
        super().__init__(1, 3, 4, 5)

    def area_parelelogram(self):

        return self.side_a * self.side_b


pa = Paralelogram(1, 3, 4, 5)
print(pa.area_parelelogram())


class Rectangle(Quadrilateral):
    """Aspects"""

    def __init__(self, side_a, side_b, side_c, side_d):
        "initializazion class of parents"
        super().__init__(1, 3, 4, 5)

    def area_rectangle(self):

        return self.side_a * self.side_b


rl = Rectangle(1, 3, None, None)
print(rl.area_rectangle())


class Square(Quadrilateral):
    """Aspects"""

    def __init__(self, side_a, side_b, side_c, side_d):
        "initializazion class of parents"
        super().__init__(1, 3, 4, 5)

    def area_Square(self):

        return self.side_a * self.side_a


rl = Rectangle(1, 3, None, None)
print(rl.area_rectangle())
