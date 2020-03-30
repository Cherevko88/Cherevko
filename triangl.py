from math import sqrt, sin

class Point:
    __x = 0
    __y = 0

    def __init__(self, a, b):
        if isinstance(a, (int,float)) and isinstance(b, (int,float)):
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

# print(point1, point2, point3)

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
        return ((self.__second_point.x - self.__first_point.x)**2 + (self.__second_point.y - self.__first_point.y)**2)** 0.5

line1 = Line(point1, point2)
# print("Линия 1",line1)

line2 = Line(point2, point3)
# print("Линия 2",line2)

line3 = Line(point3, point1)
# print("Линия 3",line3)

distance = Line.line_sqrt
# print("Длина линии A = ", distance(line1))
# print("Длина линии B = ", distance(line2))
# print("Длина линии C = ", distance(line3))

#
# """Задание № 2 Доработайте классы Triangle и Circle: добавьте в них иниты,
# в которых бы определялись условия для создания обьектов.
# Для Triangle это три обьекта Point, для Circle это обьект Point и радиус
# Реализуйте для Triangle и Circle метод _area, который бы возвращал площаль фигуры."""

# self.first_point, self.second_point, self.third_point = self.check_points(first_point, second_point,
#                                                                           third_point)
class Triangle:
    __first_point = None
    __second_point = None
    __third_point = None
    _area = None

    def __init__(self, first_point, second_point, third_point):
        if isinstance(first_point, Point) and isinstance(second_point, Point) and isinstance(third_point, Point):
            self.__first_point = first_point
            self.__second_point = second_point
            self.__third_point = third_point
        else:
            raise TypeError

    def check_points(self, first_point, second_point, third_point):
        if first_point.Point.x == second_point.Point.x == third_point.Point.x or \
           first_point.Point.y == second_point.Point.y == third_point.Point.y:
            raise TypeError
        return first_point, second_point, third_point


    def triang_sqrt(self):
        line_tringle =((self.__second_point.x - self.__first_point.x)**2 +
                     (self.__second_point.y - self.__first_point.y)**2)** 0.5
        return line_tringle

    def area(self):
        ab = self.triang_sqrt(self.first_point, self.second_point)
        bc = self.triang_sqrt(self.__second_point, self.__third_point)
        ac = self.triang_sqrt(self.__first_point, self.__third_point)

        if ab != bc != ac:
            p = (ab + bc + ac) / 2
            self.area = sqrt(p * (p - ab) * (p - bc) * (p - ac))
        return self.area

    def __str__(self):
        return f"Это треугольник "\
               f"и точки координат: a - x:{self.__first_point.x} y:{self.__first_point.y}, "\
               f"b - x:{self.__second_point.x} y:{self.__second_point.y}, "\
               f"c - x:{self.__third_point.x} y:{self.__third_point.y}"


trian = Triangle(point1, point2, point3)
# print(trian.area())
print(trian)
