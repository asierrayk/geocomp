# -*- coding: utf-8 -*-
from __future__ import division
from point import *
import numpy as np

class Segment:

    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1

    def __repr__(self):
        return 'Segment[Point(x=%s, y=%s), Point(x=%s, y=%s)]' \
% (self.p0.x, self.p0.y, self.p1.x, self.p1.y)

    def isLeft(self, p):

#        a = (self.p0 - self.p1).norm()
#        b = (self.p0 - p).norm()
#        c = (self.p1 - p).norm()

        return (self.p1.x - self.p0.x)*(p.y-self.p0.y)-(p.x-self.p0.x)*(self.p1.y-self.p0.y)

    def intersect(self, other):
        # We look for t,u such that s1.p0 + t v1 = s2.p0 + u v2

        # v_i es el vector que va de p0 a p1 for self and other
        v1 = self.p1 - self.p0
        v2 = other.p1 - other.p0

        aux1 = (other.p0 - self.p0)
        xProdVectors = v1.crossProduct3D(v2)

        if xProdVectors == 0:
            # 1. collinear lines (overlapping or not)
            if aux1.crossProduct3D(v1) == 0 :
                print 'collinear'


            # 2. parallel lines, no intersection
            elif aux1.crossProduct3D(v1) != 0 :
                return None

        else:
            t = aux1.crossProduct3D(v2.prodEsc(1/xProdVectors))
            u = aux1.crossProduct3D(v1.prodEsc(1/xProdVectors))

            # 3. intersection at the point s1.p0 + t v1 = s2.p0 + u v2
            if 0 <= t <= 1 and 0 <= u <= 1:
                return self.p0 + v1.prodEsc(t)

            #4. non parallel, non intersecting lines
            else:
                return None


    def __intersects__(self, other):
        # v1 es el vector que va de p0 a p1
        v1 = (self.p1 - self.p0).to_array()

        # v2 es el vector que va de other.p0 a other.p1
        v2 = (other.p1 - other.p0).to_array()

        # Segmento_1 es el que va de puno_a a punto_b
        # el _2 va de punto_c a punto_d
        # punto_a + mu * v1 + lambda * v2 = punto_d


        a = np.array([v1,v2])
        a = a.T
        b = other.p1 - self.p0
        b2 = other.p0 - self.p0

        b = b.to_array()
        b2 = b2.to_array()

        det = a[0,0] * a [1,1] - a[1,0] * a[0,1]

        # En este caso ambos vectores son paralelos
        if det == 0:
            dif1 = self.p0 - other.p0
            dif1 = dif1.to_array()
            # Si ocurre esto son paralelos pero están a distinta altura
            if np.cross(v1, dif1) <> 0:
                return None
            # En caso contrario, si están ·-· x-x ó x-x ·-· no intersecan
            # si no sucede esto sí intersecan
            # Basta con que uno de los extremos de other esté entre los
            #     extremos de self
            else:
                # return
                if ((min(self.p0.x, self.p1.x) <= other.p0.x <= \
                    max(self.p0.x, self.p1.x)) and \
                    (min(self.p0.y, self.p1.y) <= other.p0.y <= \
                    max(self.p0.y, self.p1.y))):
                        return other.p0
                elif ((min(self.p0.x, self.p1.x) <= other.p1.x <= \
                    max(self.p0.x, self.p1.x)) and \
                    (min(self.p0.y, self.p1.y) <= other.p1.y <= \
                    max(self.p0.y, self.p1.y))):
                        return other.p1

        else:
            x1 = np.linalg.solve(a, b)
            x2 = np.linalg.solve(a, b2)
        '''
        print self.p0, self.p1, v1
        print 'otro', other.p0, other.p1, v2
        print 'solucion mu para p4', x1[0]
        print 'solucion lambda para p4', x1[1]
        print 'solucion mu para p3', x2[0]
        print 'solucion lambda para p3', x2[1]
        '''
        if 0 <= x1[0] <= 1 and -1 <= x1[1] <= 1 and\
           -1 <= x2[1] <= 1:
            return Point(self.p0.x + x1[0] * v1[0], self.p0.y + x1[0] * v1[1])
        else:
            return None
