from __future__ import division
import numpy as np 

def polyeval_bezier(P, num_points, algorithm):
    grid = np.linspace(0,1,num_points)    
    
    if algorithm == "horner":
        np.polyval(P,t)
    elif algorithm == "deCasteljau":
        _deCasteljau(P,t)

def _deCasteljau(P, t):
    n = P.shape[0] - 1 
    bezier = np.zeros(len(t))
    for j in range(len(t)):
        b = np.copy(P)
        for k in range(1, n+1):
            for i in range(n+1-k): # Calculamos b[i] = (b_i)^k
                b[i] = (1-t[j])*b[i]+ t[j]*b[i+1]
        bezier[j] = b[0]
    return bezier

def bezier_subdivision(P, k, epsilon, lines=False):
    pass

def backward_differences_bezier(P, m, h=None):
    pass


