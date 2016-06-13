# -*- coding: utf-8 -*-
import numpy as np
from point import Point
from segment1 import Segment
from rectangle import Rect
from bezier import subdivision

class BezierIntersection():

    def __init__(self):
        self.intersPoints = []

    
    def intersect(self, P1, P2, eps):
        A1 = np.asarray(P1)
        A2 = np.asarray(P2)
        m = A1.shape[0] - 1
        n = A2.shape[0] - 1
        
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
            
            
            diff2_1 = np.diff(A1, n=2, axis=0)  # m-1 diffs
            max_diff2_1 = np.max(np.linalg.norm(diff2_1, axis=1))
            

            if m * (m - 1) * max_diff2_1 > eps:
                # calculate bezier polygon subdivision 1
                A11, A12 = subdivision(A1)
                self.intersect(A11.tolist(), P2, eps)
                self.intersect(A12.tolist(), P2, eps)
                
            else:
                
                diff2_2 = np.diff(A2, n=2, axis=0)  # n-1 diffs
                max_diff2_2 = np.max(np.linalg.norm(diff2_2, axis=1))
                
                if n * (n - 1) * max_diff2_2 > eps:
                    # calculate bezier polygon subdivision 2
                    A21, A22 = subdivision(A2)
                    self.intersect(P1, A21.tolist(), eps)
                    self.intersect(P1, A22.tolist(), eps)
                    
                    
                else: # (almost straight lines)
                    # intersectar los segmentos de recta P1 y P2
                    s1 = Segment(Point(A1[0,0], A1[0,1]), 
                                 Point(A1[-1,0], A1[-1,1]))
                    s2 = Segment(Point(A2[0,0], A2[0,1]), 
                                 Point(A2[-1,0], A2[-1,1]))
                    point = s1.intersect(s2)
                    if point is not None:
                        self.intersPoints.append(point)
        
                            
    def getIntersPoints(self):
        return self.intersPoints

if __name__ == '__main__':
    # example:

    P1 = [[0,1], [0,0], [1,0]]
    P2 = [[0,0], [1,0], [1,1]]
    
    i = BezierIntersection()
    i.intersect(P1, P2, 0.1)
    p = i.getIntersPoints()
    #print 'inters:', p
    
    