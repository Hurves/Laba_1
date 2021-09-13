class Rectangle:
    _name = "This is area"

    def __init__(self, length, width,  name_2):
        self.length = length
        self.width = width
        self.name_2 = name_2

    def area(self):
        """defind area function"""
        """defind limitations area function"""

        ar = f""" This is perimeter : {(self.length + self.width) * 2} """
        if not ar < str(0.0) >= str(20.0):
            return ar
        else:
            return "data is not correctly"

    def perimeter(self):
        """defind area function"""
        """defind limitations area function"""

        ap = f"""  {Rectangle._name} : {self.length * self.width}"""
        if not ap < str(0.0) >= str(20.0):
            return ap
        else:
            return "data is not correctly"

    def get_length(self):
        return self.length

    def set_length(self, value):
        self._length = value

    def del_length(self):
        del self._length

    def get_width(self):
        return self.width

    def set_width(self, value):
        self._width = value

    def del_width(self):
        del self._width

    def get_name_2(self):
        return self.name_2

    def set_name_2(self, value):
        self.name_2 = value

    def del_name_2(self):
        del self.name_2


all_p = Rectangle(1, 1, 'area')
print(all_p.area(), all_p.perimeter())
all_p.set_width(2)
print(all_p._width)
