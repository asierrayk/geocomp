# -*- coding: utf-8 -*-

from point import Point

class ConvexHull:

    def graham(self, points):
        if not isinstance(points, list):
            return
            
        points.sort()
        n = len(points)
        P = self.fromListToPoints(points)
        #print 'puntos', P
        
        L_upper = P[:2] # first two elems
        for i in xrange(2, n):
            last = P[i]
            while len(L_upper) >= 2 and last.isLeft(L_upper[-2], L_upper[-1]):
                L_upper.pop()
            L_upper.append(last)
        #print 'upper', L_upper

        L_lower = [P[-1], P[-2]] # last 2 elems
        for i in range(n-3, -1, -1):
            last = P[i]
            while len(L_lower) >= 2 and last.isLeft(L_lower[-2], L_lower[-1]):
                L_lower.pop()
            L_lower.append(last)
        #print 'lower', L_lower

        L_upper.pop()
        L_lower.pop()
        ch = L_upper + L_lower
        self.xs = [e.x for e in ch]
        self.ys = [e.y for e in ch]
        
        #ch = self.fromPointsToList(ch)
        ch = zip(self.xs, self.ys)
        return ch
    
    def graham_unzip(self, points):
        self.graham(points)
        return self.xs, self.ys

    def fromListToPoints(self, p):
        n = len(p)
        p2 = [Point(p[0][0], p[0][1])]
        for i in range(1, n):
            p2.append(Point(p[i][0], p[i][1]))
        return p2

    def fromPointsToList(self, p):
        p2 = [[p[0].x, p[0].y]]
        n = len(p)
        for i in range(1, n):
            p2.append([p[i].x, p[i].y])


'''       
#         E X A M P L E

C = ConvexHull()
p = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
r = C.graham(p)
'''
