# from abc import ABC, abstractmethod
from math import sqrt

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
            return Line(self, other) or Triangle(self, other)
        else:
            raise TypeError

point1 = Point(4, 5)
point2 = Point(8, 11)
point3 = Point(12, 5)

print(point1, point2, point3)

# 2
# Написать класс, Line отвечающий за отрезок.
# Обьект класса Line инстанциируется с помощью двух обьектов класса Point

class Line:
    __first_point = None
    __second_point = None

    def __init__(self, a, b):
        if isinstance(a, Point) and isinstance(b, Point):
            self.__first_point = a
            self.__second_point = b
        else:
            raise TypeError

    def __str__(self):
        return f'Line from {self.__first_point.x}:{self.__first_point.y} ' \
               f'to {self.__second_point.x}:{self.__second_point.y}'

    def line_sqrt(self):
        return (((self.__second_point.x - self.__first_point.x)**2 + self.__second_point.y - self.__first_point.y)** 0.5)

line1 = Line(point1, point2)
print("Линия 1",line1)

line2 = Line(point2, point3)
print("Линия 2",line2)
line3 = Line(point3, point1)
print("Линия 3",line3)

distance = Line.line_sqrt
print("Длина линии A = ", distance(line1))
print("Длина линии B = ", distance(line2))
print("Длина линии C = ", distance(line3))

#
# """Задание № 2 Доработайте классы Triangle и Circle: добавьте в них иниты,
# в которых бы определялись условия для создания обьектов.
# Для Triangle это три обьекта Point, для Circle это обьект Point и радиус"""

class Triangle:
    __first_point = None
    __second_point = None
    __third_point = None


    def __init__(self, a, b, c, ):
        if isinstance(a, Point) and isinstance(b, Point) and isinstance(c, Point):
            self.__first_point = a
            self.__second_point = b
            self.__third_point = c
        else:
            raise TypeError

    def __str__(self):
        return f"Это треугольник и точки координат: a - x:{self.__first_point.x} y:{self.__first_point.y}, "\
                                                  f"b - x:{self.__second_point.x} y:{self.__second_point.y}, "\
                                                  f"c - x:{self.__third_point.x} y:{self.__third_point.y}"

trian = Triangle(point1, point2, point3)
print(trian)


class Circle:
    __k = None
    __r = None

    def __init__(self, k, r):
        if isinstance(k, Point) and isinstance(r, (float, int)):
            self.__r = r
            self.__k = k
        else:
            raise TypeError

    def __str__(self):
        return f"Это круг с радиусом равный {self.__r} и точка k имеет координат x:{self.__k.x} : y:{self.__k.y}"


rad_cir = Circle(point1, 3)
print(rad_cir)
