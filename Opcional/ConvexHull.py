# -*- coding: utf-8 -*-
import numpy as np
from Point import Point

class ConvexHull:

    def graham(self, points):
        if not isinstance(points, list):
            return
            
        points.sort()
        n = len(points)
        P = self.fromListToPoints(points, n)
        '''
        P = np.asarray(Points)
        n = P.shape[0]
        P = np.sort(P, )
        P = self.fromListToPoints(P, n)
        '''

        #print 'puntos', P
        
        L_upper = P[:2] # first two elem
        for i in xrange(2, n):
            last = P[i]
            while len(L_upper) >= 2 and last.isLeft(P[-2], P[-1]):
                L_upper.pop()
            L_upper.append(last)

        L_lower = P[-2:]
        for i in range(n-3, -1, -1):
            last = P[i]
            while len(L_lower) >= 2 and last.isLeft(P[-2], P[-1]):
                L_lower.pop()
            L_lower.append(last)

        return L_upper.pop() + L_lower.pop()

    def fromListToPoints(self, p, n):
        p2 = [Point(p[0][0], p[0][1])]
        for i in range(1, n):
            p2.append(Point(p[i][0], p[i][1]))
        return p2


#         E X A M P L E

C = ConvexHull()
p = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
#r = C.graham(p)

# .. paso a paso:

p.sort()
n = len(p)
P = C.fromListToPoints(p, n)

L_upper = P[:2]
# i = 2
last = P[2]
b = last.isLeft(P[-2], P[-1]) # esto da false !


