"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """


def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect,dx,dy):
    rect.corner.x += dx
    rect.corner.y += dy 

def move_rectangle2(rect,dx,y):
    rect2 = copy.deepcopy(box)
    rect2.corner.x += dx
    rect2.corner.y += dy

def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print('blank', end=' ')
    print_point(blank)

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)
    
    print('move the box')
    move_rectangle2(box,4,4)
    new_center = find_center(box)
    print('new center', end=' ')
    print_point(new_center)

if __name__ == '__main__':
    main()



#-------------

#the header indicates the creation of class Point
#the body is a docstring that explains what the class is for

#Defining a class named Cerveja creates a class object
#The class object is like a factory for creating objects
#to create a Cerveja you call Cerveja as it were a function 


class Cerveja:
    """This is an example class 
    """

Cerveja 

gole = Cerveja()

gole

#The return value is a reference to a Cerveja, which we assign to blank

#Creating a new object is called instantiation, and the object is
#an instance of the class

#Every object is an instance of some class, so "object" and "instance"
#are interchangeable. 

#We assign attributes to an instance 

gole.x = 4
gole.y = 4

gole.x
gole.y

z = gole.x 
z

gole2 = Cerveja()

gole2.x = 2
gole2.y = 2

#The expression gole.x means go to the object gole refers to and get the
#value of x 

'(%g, %g)' % (gole.x, gole.y)

import math 

distance = math.sqrt(gole.x**2 + gole.y**2)
distance

#You can pass an instance as an argument 

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

print_point(gole)    

#Excercice 

def distance_between_points(p1,p2): 
    x = ((p1.x - p2.x) + (p1.y - p2.y))
    if x > 0:
        return math.sqrt(x)
    else:
        return math.sqrt(-x)      

distance_between_points(gole,gole2)

#The book refers to blank. I named it as 'gole'



