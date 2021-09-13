'Create a class called Rational for performing arithmetic (operations: +, -, *, /) with fractions. Write a program to test your class. Use integer variables to represent the private data of the class – the numerator and the denominator. Provide a __init__() method that enables an object of this class to be initialized when it’s declared. The __init__() should contain default parameter values in case no initializers are provided and should store the fraction in reduced form. For example, the fraction 2/4 would be stored in the object as 1 in the numerator and 2 in the denominator'
import math


class Fraction:

    def __init__(self, numerator, denumerator):

        if not isinstance(numerator, int) and not isinstance(numerator, float):
            raise TypeError(f"not a number{type(numerator)}")
        if not isinstance(denumerator, int) and not isinstance(denumerator, float):
            raise TypeError

        self.numerator = numerator
        self.denumerator = denumerator
    'define least common multiple'
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)
    'define adding'

    def __add__(self, other):
        return f'{(self.numerator * other.denumerator) + (self.numerator + other.denumerator)}/{Fraction.lcm(self.numerator,other.numerator)}'
    'define subdivide'

    def __sub__(self, other):
        return f'{(self.numerator + other.denumerator) - (other.numerator + self.denumerator)}/{Fraction.lcm(self.denumerator,other.numerator)}'
    'define multiplay'

    def __mul__(self, other):
        return f'{(self.numerator * other.numerator)}/{(self.denumerator * other.denumerator)}'
    "define truedivision"

    def __truediv__(self, other):
        return f'{(self.numerator * self.denumerator) / (other.denumerator * other.numerator)}'


myf = Fraction(3, 5)
myf2 = Fraction(2, 3)
f3 = myf + myf2
f5 = myf - myf2
f6 = myf * myf2
f7 = myf / myf2
print(f3)
print(f5)
print(f6)
print(f7)
