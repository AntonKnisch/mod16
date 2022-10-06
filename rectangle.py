class Rectangle :
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area_reqtangle(self):
        return self.a * self.b


class Square:
    def __init__(self, a=0 ):
        self.a = a
    def get_area_square(self) :
        return self.a** 2


class Circle:
    def __init__(self,circle=0):
        self.radius_of_circle = circle
    def get_area_circle(self):
        return self.radius_of_circle * 3.14 ** 2