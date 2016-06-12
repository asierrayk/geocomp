# -*- coding: utf-8 -*-
from __future__ import division
from Point import *
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
        
    def __intersects__(self, other):
        # v1 es el vector que va de p0 a p1
        v1 = self.p1 - self.p0
        
        # v2 es el vector que va de other.p0 a other.p1
        v2 = other.p1 - other.p0
        
        # Segmento_1 es el que va de puno_a a punto_b
        # el _2 va de punto_c a punto_d
        # punto_a + mu * v1 + lambda * v2 = punto_d
        
        
        a = np.array([v1,v2])
        b = other.p1 - self.p0

        det = np.linalg.det(a)
        
        # En este caso ambos vectores son paralelos
        if det == 0:
            dif1 = self.p0 - other.p0
            # Si ocurre esto son paralelos pero están a distinta altura
            if np.cross(v1, dif1) <> 0:
                return false
            # En caso contrario, si están ·-· x-x ó x-x ·-· no intersecan
            # si no sucede esto sí intersecan
            # Basta con que uno de los extremos de other esté entre los 
            #     extremos de self
            else:
                return ((min(self.p0.x, self.p1.x) <= other.p0.x <= \
                    max(self.p0.x, self.p1.x)) and \
                    (min(self.p0.y, self.p1.y) <= other.p0.y <= \
                    max(self.p0.y, self.p1.y))) or \
                    ((min(self.p0.x, self.p1.x) <= other.p1.x <= \
                    max(self.p0.x, self.p1.x)) and \
                    (min(self.p0.y, self.p1.y) <= other.p1.y <= \
                    max(self.p0.y, self.p1.y)))
                
        else:
            x = np.linalg.solve(a, b)
        
        return x[0] >= -1 and x[0] <= 1 and x[1] >= -1 and x[1] <= 1
            
    
