# -*- coding: utf-8 -*-
import numpy as np

class ConvexHull:
    
    def graham(self, Points):
        P = np.asarray(Points)
        P = np.sort(P)
        n = P.shape[0]        
        
        L_upper = P[:2]
        
        for i in xrange(3, n):
            last = P[i]
            while L_upper.shape[0] >= 2 and  last.isLeft(P[-2, -1]):
                L_upper.pop()
            L_upper.append(last)
            
        L_lower = P[-2:]
        
        
        for i in range(n-3, -1, -1):
            last = P[i]
            while L_lower.shape[0] >= 2 and  last.isLeft(P[-2, -1]):
                L_lower.pop()
            L_lower.append(last)
            
        return np.vstack(L_upper.pop(), L_lower.pop())
                
            
            