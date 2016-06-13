# -*- coding: utf-8 -*-
import numpy as np
from point import Point
from segment import Segment
from rectangle import Rect
from bezier import subdivision

class BezierIntersection():

    @staticmethod
    def intersect(P1, P2, eps):
        A1 = np.asarray(P1)
        A2 = np.asarray(P2)
        
        x = min(A1[:,0])
        y = min(A1[:,1])
        min1 = Point(x, y)
        x = max(A1[:,0])
        y = max(A1[:,1])
        max1 = Point(x, y)
        
        x = min(A2[:,0])
        y = min(A2[:,1])
        min2 = Point(x, y)
        x = max(A2[:,0])
        y = max(A2[:,1])
        max2 = Point(x, y)

        r1 = Rect(min1, max1)
        r2 = Rect(min2, max2)
        
        if r1.__intersects__(r2) :
            
            m = A1.shape[0] - 1
            diff2_1 = np.diff(A1, n=2, axis=0)  # m-1 diffs
            max_diff2_1 = np.max(np.linalg.norm(diff2_1, axis=1))

            n = A2.shape[0] - 1
            diff2_2 = np.diff(A2, n=2, axis=0)  # n-1 diffs
            max_diff2_2 = np.max(np.linalg.norm(diff2_2, axis=1))

            if m * (m - 1) * max_diff2_1 > eps:
                # calculate bezier polygon subdivision
                A11, A12 = subdivision(A1)
                BezierIntersection.intersect(A11.tolist(), P2, eps)
                BezierIntersection.intersect(A12.tolist(), P2, eps)
            elif n * (n - 1) * max_diff2_2 > eps:
                # calculate bezier polygon subdivision
                A21, A22 = subdivision(A2)
                BezierIntersection.intersect(P1, A21.tolist(), eps)
                BezierIntersection.intersect(P1, A22.tolist(), eps)
            else: # (almost straight lines)
                # intersectar los segmentos de recta P1 y P2
                s1 = Segment(Point(P1[0][0], P1[0][1]), 
                             Point(P1[-1][0], P1[-1][1]))
                s2 = Segment(Point(P2[0][0], P2[0][1]), 
                             Point(P2[-1][0], P2[-1][1]))
                point = s1.__intersects__(s2)
                print '(1)', A1[0], A1[-1], '(2)', A2[0], A2[-1], '>>', point
                if point is not None:
                    return point


if __name__ == '__main__':
    P1 = [[0,2], [0,0], [1,0]]
    P2 = [[0,0], [1,0], [1,2]]
    
    p1 = Point(0,3) 
    p2 = Point(3,0)
    p3 = Point(0,0) 
    p4 = Point(7,7) 
    s1 = Segment(p1,p2)
    s2 = Segment(p3,p4)
    
    i = s1.__intersects__(s2)
    print 'i ', i
    
    p = BezierIntersection.intersect(P1,P2, 0.01)
    print 'inters::', p