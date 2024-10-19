from abc import ABC, abstractmethod
from math import pi, sqrt

class Shapes(ABC):
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimetr():
        pass

class Circle(Shapes):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def __str__(self):
        s = 'Круг в точке (' + str(self.x) + ', ' + str(self.y) + ') и радиусом ' + str(self.r)
        print(s)
        print('S = ' + str(round(self.area(), 2)))
        print('P = ' + str(round(self.perimetr(), 2)))
    def area(self):
        a = pi * (self.r**2)
        return a
    def perimetr(self):
        p = 2 * pi * self.r 
        return p
class Triangle(Shapes):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def __str__(self):
        s = 'Треугольник, построенный на точках (' + str(self.x1) + ', ' + str(self.y1) + '), (' + str(self.x2) + ', ' + str(self.y2) + '), (' + str(self.x3) + ', ' + str(self.y3) + ')'
        print(s)
        print('S = ' + str(round(self.area(), 2)))
        print('P = ' + str(round(self.perimetr(), 2)))
    def side_a(self):
        return sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)
    def side_b(self):
        return sqrt((self.x2 - self.x3)**2 + (self.y2 - self.y3)**2)
    def side_c(self):
        return sqrt((self.x3 - self.x1)**2 + (self.y3 - self.y1)**2)
    def perimetr(self):
        p = self.side_a() + self.side_b() + self.side_c()
        return p
    def area(self):
        sq = sqrt((self.perimetr()/2) * ((self.perimetr()/2) - self.side_a()) * ((self.perimetr()/2) - self.side_b()) * ((self.perimetr()/2) - self.side_c()))
        return sq

class Rectangle(Shapes):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
    def __str__(self):
        s = 'Прямоугольник, построенный на точках (' + str(self.x1) + ', ' + str(self.y1) + '), (' + str(self.x2) + ', ' + str(self.y2) + '), (' + str(self.x3) + ', ' + str(self.y3) + '), (' + str(self.x4) + ', ' + str(self.y4) + ')'
        print(s)
        print('S = ' + str(round(self.area(), 2)))
        print('P = ' + str(round(self.perimetr(), 2)))
    def side_a(self):
        return sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)
    def side_b(self):
        return sqrt((self.x2 - self.x3)**2 + (self.y2 - self.y3)**2)
    def perimetr(self):
        p = (self.side_a() + self.side_b())*2
        return p
    def area(self):
        a = self.side_a() * self.side_b()
        return a
class Square(Rectangle):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)
    def __str__(self):
        s = 'Квадрат, построенный на точках (' + str(self.x1) + ', ' + str(self.y1) + '), (' + str(self.x2) + ', ' + str(self.y2) + '), (' + str(self.x3) + ', ' + str(self.y3) + '), (' + str(self.x4) + ', ' + str(self.y4) + ')'
        print(s)
        print('S = ' + str(round(self.area(), 2)))
        print('P = ' + str(round(self.perimetr(), 2)))
    def side_a(self):
        return super().side_a()
    def perimetr(self):
        return self.side_a() * 4
    def area(self):
        return self.side_a() ** 2
class Rhomb(Shapes):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
    def __str__(self):
        s = 'Ромб, построенный на точках (' + str(self.x1) + ', ' + str(self.y1) + '), (' + str(self.x2) + ', ' + str(self.y2) + '), (' + str(self.x3) + ', ' + str(self.y3) + '), (' + str(self.x4) + ', ' + str(self.y4) + ')'
        print(s)
        print('S = ' + str(round(self.area(), 2)))
        print('P = ' + str(round(self.perimetr(), 2)))
    def side_a(self):
        return sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)
    def diag_1(self):
        return sqrt((self.x1 - self.x3)**2 + (self.y1 - self.y3)**2)
    def diag_2(self):
        return sqrt((self.x2 - self.x4)**2 + (self.y2 - self.y4)**2)
    def perimetr(self):
        p = (self.side_a())*4
        return p
    def area(self):
        a = (self.diag_1() * self.diag_2())/2
        return a
c = Circle(1, 2, 3)
c.__str__()
t = Triangle(0, 1, 0, 0, 2, 0)
t.__str__()
r = Rectangle(0, 0, 3, 0, 3, 4, 0, 4)
r.__str__()
sqa = Square(0, 0, 2, 0, 2, 2, 0, 2)
sqa.__str__()
rho = Rhomb(0, 2, 3, 4, 6, 2, 3, 0)
rho.__str__()
