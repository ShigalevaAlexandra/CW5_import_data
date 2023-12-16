#def triangle_perimeter() - вычисляет периметр треугольника
#def triangle_area() - вычисляет площадь треугольника
#default_a, default_b, default_c - дефолтные длины сторон, если пользователь не введет свои

from math import sqrt

default_a = 7.0
default_b = 2.0
default_c = 8.0

def triangle_perimeter(a = default_a, b = default_b, c = default_c):

        P = a + b + c
        return (f"Периметр треугольника P = {P}")

#------------------------------------------------------------------------------

def triangle_area(a = default_a, b = default_b, c = default_c):

        p = (a + b + c)/2
        S = sqrt(p * (p - a) * (p - b) * (p - c))
        return (f"Площадь треугольника S = {S}")