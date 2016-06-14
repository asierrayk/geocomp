# -*- coding: utf-8 -*-

from point import Point

class ConvexHull:
    """
    Class which calculates the convex hull of a list of given points

    Methods
    -------
    graham
    graham_unzip

    Atributes
    ---------
    xs : first components of the convex hull calculated
    ys : second components of the convex hull calculated

    """

    def graham(self, points):
        '''
        Calculate the convex hull of a given set of points.
        Graham's method used.


        Parameters
        ----------
        points :
            list of 2D points

        Return
        ------
        list of points conforming the convex hull of the given points
        '''
        if not isinstance(points, list):
            return

        points.sort()
        n = len(points)
        P = Point.fromListToPoints(points)
        #print 'puntos', P

        L_upper = P[:2] # first 2 elems
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

        # save atrib
        self.xs = [e.x for e in ch]
        self.ys = [e.y for e in ch]

        #ch = zip(self.xs, self.ys)  # esta linea sobra??? parece que si
        return ch

    def graham_unzip(self, points):
        '''
        Calculate convex hull of given points.
        Return first and second components separately.

        Return
        ------
        self.xs
        self.ys
        '''
        self.graham(points)
        return self.xs, self.ys



'''
#         E X A M P L E

C = ConvexHull()
p = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
r = C.graham(p)
'''
