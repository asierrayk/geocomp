from __future__ import division
import numpy as np 

def polyeval_bezier(P, num_points, algorithm):
    pass

def _deCasteljau(P, t):
    n = P.shape[0] - 1 
    b = np.copy(P)
    for k in range(1, n+1):
        for i in range(n+1-k): # Calculamos b[i] = (b_i)^k
            b[i] = (1-t)*b[i]+ t*b[i+1]
    return b[0]

def bezier_subdivision(P, k, epsilon, lines=False):
    pass

def backward_differences_bezier(P, m, h=None):
    pass

