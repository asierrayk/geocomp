# -*- coding: utf-8 -*-
from point import *

class Rect(object):
    
    def __init__(self, p1, p2):
        """ p1 y p2 son vértices opuestos del rectángulo
            Guardamos la coordenada de cada lado:
            Lado izquierdo y derecho (coord x)
            Lado de arriba y abajo (coord y)
        """
        self.left = min(p1.x, p2.x)
        self.right = max(p1.x, p2.x)
        
        self.down = min(p1.y, p2.y)
        self.up = max(p1.y, p2.y)
        
    def __intersects__(self, other):
        
        if self.left > other.right or self.right < other.left :
            return False
        if self.up < other.down or self.down > other.up :
            return False
       
        return True
        
