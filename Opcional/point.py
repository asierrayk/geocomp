# -*- coding: utf-8 -*-
import numpy as np
from functools import total_ordering

@total_ordering
class Point:
    """
    Class which calculates the intersection points of two bezier curves

    Methods
    -------
    __repr__
    __eq__
    __lt__
    __add__
    __sub__
    __mul__
    prodEsc
    isLeft
    to_array
    fromListToPoints
    crossProduct3D


    Atributes
    ---------
    intersPoints : list of intersection points
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.x, self.y)

    def __eq__(self, other):
        return (isinstance(other, Point)
                and (self.x, self.y) == (other.x, other.y))

    def __lt__(self, other):
        return (isinstance(other, Point)
                #and (self.x, self.y) < (other.x, other.y))
                and ((self.x < other.x)
                or (self.x == other.x and self.y < other.y)))

    def __add__(self, other):
        if type(other) is tuple:
            return Point(self.x+other[0], self.y + other[1])
        else:
            return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        if type(other) is tuple:
            return Point(self.x-other[0], self.y - other[1])
        else:
            return Point(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        ''' Dot product'''
        if type(other) is tuple:
            return self.x*other[0] + self.y * other[1]
        else:
            return self.x*other.x + self.y*other.y

    def prodEsc(self, esc):
        '''Product by escalar'''
        return Point(self.x*esc, self.y*esc)


    def isLeft(self, a, b):
        '''
        check is the point is to the left of the vector ab.
        first compute the perpendicular to the left of ab=(x, y), ie, (-y, x)
        then compute dot product <(-y,x), (a self)>
        if the projection is positive self is to the left of ab
        '''
        return (b.x - a.x)*(self.y-a.y)-(self.x-a.x)*(b.y-a.y) >= 0

    def to_array(self):
        '''
        get the list [x, y] with the  components of the Point object

        Return
        ------
        list
        '''
        return [self.x, self.y]

    @staticmethod
    def fromListToPoints(p):
        '''
        transform a list of 2D points into a list of Point objects

        Parameters
        ----------
        p : list of 2D points

        Return
        ------
        list of class Point objects
        '''
        n = len(p)
        p2 = [Point(p[0][0], p[0][1])]
        for i in range(1, n):
            p2.append(Point(p[i][0], p[i][1]))
        return p2

    def crossProduct3D(self, other):
        '''
        calculate the 3D cross product.
        
        '''
        return self.x*other.y - self.y*other.x
'''
def x(self):
return self.x

def y(self):
return self.y
'''
