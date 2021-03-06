
class Point:
    __x = 0
    __y = 0

    def __init__(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.__x = a
            self.__y = b
        else:
            raise TypeError

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return f'Point x: {self.__x} y: {self.__y}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Line(self, other)
        else:
            raise TypeError



point1 = Point(1.5, 40)
point2 = Point(10, 20)
point3 = Point(10, 20)

print(point1, point2)


# 2
# Написать класс, Line отвечающий за отрезок.
# Обьект класса Line инстанциируется с помощью двух обьектов класса Point

class Line:
    __first_point = None
    __second_point = None

    def __init__(self, a, b):
        if isinstance(a, Point) and isinstance(b, Point):
            if a.x != b.x and a.y != b.y:
                self.__first_point = a
                self.__second_point = b
            else:
                raise TypeError

    def __str__(self):
        return f'Line from {self.__first_point.x}:{self.__first_point.y} ' \
               f'to {self.__second_point.x}:{self.__second_point.y}'



    def line_sqrt(self, __first_point.x, b):

        return (((b.x - a.x)**2 + b.y - a.y)** 0.5)


line1 = Line(point1, point2)
print(line1)

line2 = point2 + point1
print(line2)

print(Line.line_sqrt(Point))
