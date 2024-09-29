from math import atan
class complex:
    def __init__(self, a, b):
        complex.Re = a
        complex.Im = b
    def construct(self):
        self.Re = round(self.Re, 2)
        self.Im = round(self.Im, 2)
        if self.Im >= 0:
            print("z = " + str(self.Re) + " + " + str(self.Im) + "i")
        else:
            print("z = " + str(self.Re) + " - " + str(abs(self.Im)) + "i")
    def expon(self):
        r = round((self.Re**2 + self.Im**2)**(1/2), 2)
        phi = round(atan(self.Re/self.Im), 2)
        print ("z = " + str(r) + "e^(" + str(phi) + "i)")
def c_sum(z1, z2):
    a = z1.Re + z2.Re
    b = z1.Im + z2.Im
    return complex(a, b)
def c_dif(z1, z2):
    a = z1.Re - z2.Re
    b = z1.Im - z2.Im
    return complex(a, b)
def c_prod(z1, z2):
    a = z1.Re * z2.Re - z1.Im * z2.Im
    b = z1.Re * z2.Im + z1.Im * z2.Re
    return complex(a, b)
def c_part(z1, z2):
    a = (z1.Re * z2.Re + z1.Im * z2.Im) / (z2.Re**2 + z2.Im**2)
    b = (z1.Im * z2.Re - z1.Re * z2.Im) / (z2.Re**2 + z2.Im**2)
    return complex(a, b)
A = complex(0, 0)
B = complex(0, 0)
print("Введите вещественную часть первого числа")
A.Re = int(input())
print("Введите мнимую часть первого числа")
A.Im = int(input())
print("Введите вещественную часть второго числа")
B.Re = int(input())
print("Введите мнимую часть второго числа")
B.Im = int(input())
c_sum(A, B).construct()
c_dif(A, B).construct()
c_prod(A, B).construct()
c_part(A, B).construct()