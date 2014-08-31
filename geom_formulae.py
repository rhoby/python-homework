__author__ = 'hoby'

from numpy import *

##########VOLUME OF THYE RECTANGLE######################
def rectangle_area(lenght,width):
     """
     calculate the area of a rectangle from lenght and width.
     :param length:the lenght side of the rectangle
     :param width: the width side of the rectangle
     """
     return lenght*width
print("the area of the rectangle is", rectangle_area(3,4))

##########AREA OF THE CIRCLE##############################
def circle_area(radius):
    """
    calculate the area of a circle by his radius
    :param radius of the circle
    :return: the area of circle
    """
    return pi*radius**2
print("the area of the cicle is", circle_area(4))

############VOLUME OF THE CUBE###########################
def volume_cube(side):
    """
    calculate the volume of the cube
    :param side: the side of the cube
    :return: the volume of the cube
    """
    return side**3
print("the volume of the cube is",volume_cube(4))

#############AREA OF THE SPHERE#########################
def sphere_area(radius):
    """
    calculate the area of the sphere
    :param radius:
    :return: the area of the sphere
    """
    return 4*pi*radius**2
print("the area of the Sphere is", sphere_area(4))

###############AREA OF THE DIAMOND#######################
def diamond_area(diagonal1,diagonal2):
    """
    calculate the area of the diamond
    :param diagonal1 and diangonal2 are the diagonals of the diamond
    :return:the area of the diamond
    """
    return (diagonal1*diagonal2)/2
print("thhe area of the diamond is", diamond_area(5,3))

################AREA OF THE TRIANGLE###########################
def triangle_area(basis,height):
    """
    calculate the area of the triangle by the basis and the height
    :param basis: the basis of the triangle
    :param height: the height of the triangle
    :return:the area of the triangle
    """
    return (basis*height)/2
print("the area of the triangle is", triangle_area(5,3))

###################AREA OF THE TRAPEZIUM##########################
def trapezium_area(basis1,basis2,height):
    """
    calculate the area of the trapezium by basis and height
    :return: the area of the trapezium
    """
    return (basis1+basis2)*height*0.5
print("the area of the trapezium is",trapezium_area(3,4,5))

#######################VOLUME OF THE CYLINDER#############################
def cylinder_volume(r,h):
    """

    :param r: radius of the basis of the cylinder
    :param h: height of the cylinder
    :return: the volume of the cylinder
    """
    return pi*r**2*h
print("the volume of the cylinder is", cylinder_volume(5,6))

###########################AREA OF THE PENTAGON###########################
def Pentagon_area(s,a):
    """
    :param s: the side of the regular pentagon
    :param a: the apothem of the pentagon
    :return: the area of the pentagon
    """
    return 5*(s*a)/2
print("the area of the pengagone is", Pentagon_area(5,4))

###########################VOLUME OF THE CONE#####################################
def cone_volume(radius, height):
    """

    :param radius: the radius of the basis
    :param height: the height of the cone
    :return: the volume of the cone
    """
    return pi*radius**2*height/3
print("the volume of the cone is", cone_volume(3,4))











