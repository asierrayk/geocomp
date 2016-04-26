from __future__ import division
import numpy as np 

def polyeval_bezier(P, num_points, algorithm):
    grid = np.linspace(0,1,num_points)    
    
    if algorithm == "horner":
        np.polyval(P,t)
    elif algorithm == "deCasteljau":
        _deCasteljau(P,t)

def _deCasteljau(P, t):
    n = P.shape[0] - 1 #comprobar valor
    bezier = np.zeros(len(t))
    for j in range(len(t)):
        b = np.copy(P)
        for k in range(1, n+1):
            for i in range(n+1-k): # Calculamos b[i] = (b_i)^k
                b[i] = (1-t[j])*b[i]+ t[j]*b[i+1]
        bezier[j] = b[0]
    return bezier
    
def _horner(P, t, num_points):
    n = P.shape[0]
    t = np.linspace(0,1,num_points)
    t_0 = t[:len(t)/2]
    t_0 = t_0/(1-t_0)
    t_1 = t[len(t)/2:]
    pol_0 = [P[i] * comb(n,i) for i in range(n+1/2)]
    
    bezier_0 = np.polyval(pol_0, t_0)

    pol_1 = [P[n-i] * comb(n,i) for i in range(n+1/2)]
    
    bezier_1 = np.polyval(P, t_1)
    
    bezier = np.concatenate((bezier_0, bezier_1))

def bezier_subdivision(P, k, epsilon, lines=False):
    pass

def backward_differences_bezier(P, m, h=None):
    pass


