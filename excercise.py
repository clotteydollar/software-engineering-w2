from cmath import pi
from matplotlib.pyplot import pie
from torch import square


## user input turn into float
radius = float(input("Enter the radius of the circle :"))

pi =  3.14159

## function to calculate area of a circle
def area_circle (radius):
    area =pi * radius**2

    return area


print(area_circle(radius))
