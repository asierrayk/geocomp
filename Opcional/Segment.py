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