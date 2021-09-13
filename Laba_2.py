class Rectangle:
    _name = "This is area"

    def __init__(self, length, width,  name_2):
        self.length = length
        self.width = width
        self.name_2 = name_2

        def get.length(self):
            return self.length

        def set.length(self, value):
            self.length = value

        def del.length(self):
            del self.length

    def area(self):
        """defind area function"""
        """defind limitations area function"""

        ar = f""" This is perimeter : {(self.length + self.width) * 2} """
        if not ar < str(0.0) >= str(20.0):
            return ar
        else:
            return "data is not correctly"

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
            self.length = value

        def del_length(self):
            del self.length


all_p = Rectangle(1, 1, 'area')
print(all_p.area(), all_p.perimeter())
