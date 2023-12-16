#def square_perimeter() - вычисляет периметр квадрата
#def square_area() - вычисляет площадь квадрата
#default_a - дефолтная длины стороны, если пользователь не введет свою

from math import pow

default_a = 15.0

def square_perimeter(a = default_a):

        P = a * 4
        return (f"Периметр квадрата P = {P}")

#------------------------------------------------------------------------------

def square_area(a = default_a):

        S = pow(a, 4)
        return (f"Площадь квадрата S = {S}")