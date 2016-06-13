# -*- coding: utf-8 -*-
from point import *

class Rect(object):
    def __init__(self, p1, p2):
        """ p1 y p2 son vértices opuestos del rectángulo
            Guardamos la coordenada de cada lado:
            Lado izquierdo y derecho (coord x)
            Lado de arriba y abajo (coord y)
        """
        self.l_izq   = min(p1.x, p2.x)
        self.l_der  = max(p1.x, p2.x)
        self.l_abaj = min(p1.y, p2.y)
        self.l_arriba    = max(p1.y, p2.y)
        
    def __intersects__(self, other):
        intersec_horizon = (self.l_izq <= other.l_izq <= self.l_der) or \
                           (self.l_izq <= other.l_der <= self.l_der)
        intersec_vertic = (self.l_abaj <= other.l_abaj <= self.l_arriba) or \
                           (self.l_abaj <= other.l_arriba <= self.l_arriba)
        
        return intersec_horizon and intersec_vertic                   
                         
