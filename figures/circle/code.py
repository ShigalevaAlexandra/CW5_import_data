#def circle_perimeter() - вычисляет длину окружности
#def circle_area() - вычисляет площадь окружности
#default_radius - дефолтный радиус, если пользователь не введет свой

from math import pi
from math import pow

default_radius = 5.0

def circle_perimeter(radius = default_radius):

        C = 2 * pi * radius
        return (f"Длина окружности С = {C}")

#------------------------------------------------------------------------------

def circle_area(radius = default_radius):

        S = pi * pow(radius, 2)
        return (f"Площадь окружности S = {S}")