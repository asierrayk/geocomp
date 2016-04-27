# coding=utf-8
from __future__ import division
import numpy as np

BINOMIAL_DICT = dict()
RECURSIVE_BERNSTEIN_DICT = dict()



def polyeval_bezier(P, num_points, algorithm):
    '''
    Parameters
    ----------
    P :
        numpy.array P de dimensión (n + 1, dim)
    num_points :
        entero positivo
    algorithm :
        algorithm será una cadena con uno de los valores siguientes: 'direct',
        'recursive', 'horner' o 'deCasteljau'
    Returns
    -------
    La función devolverá un numpy.array de dimensión (num_points, dim) con los valores de la curva de Bézier en los instantes dados por num_points valores equiespaciados entre 0 y 1 (incluyendo extremos).
    '''
    grid = np.linspace(0,1,num_points)
    if algorithm == "direct":
        return _direct(P,num_points)
    elif algorithm == "recursive":
        # los polinomios de Bernstein se calculen usando la fórmula recursiva que los caracteriza
        pass
    elif algorithm == "horner":
        # método de Horner, dividiendo los valores en dos trozos: los menores que 0.5 y los mayores o iguales a 0.5
        return _horner(P, num_points)
    elif algorithm == "deCasteljau":
        # evaluará la curva usando el algoritmo de De Casteljau
        _deCasteljau(P, t)

def _deCasteljau(P, num_points): 
    t = np.linspace(0,1,num_points)
    return [_deCasteljau_aux(P.astype(float), t[i]) for i in range(num_points)]
    
def _deCasteljau_aux(b, t):
    n = b.shape[0] - 1
    b = np.copy(P)
    for k in range(1, n+1):
        for i in range(n+1-k): # Calculamos b[i] = (b_i)^k
            b[i] = (1-t)*b[i] + t*b[i+1]
    return b[0]    

def _horner(P, num_points):
    n = P.shape[0] - 1
    t = np.linspace(0,1,num_points)
    
    t_0 = t[:num_points/2]
    t_0 = t_0/(1-t_0)
    t_0 = t_0[:,np.newaxis]
    pol_0 = [P[i] * comb(n,i) for i in range(n+1)]

    bezier_0 = (1-t_0)**n * np.polyval(pol_0, t_0)

    t_1 = t[num_points/2:]
    t_1 = (1-t_1)/t_1
    t_1 = t_1[:,np.newaxis]
    pol_1 = [P[n-i] * comb(n,i) for i in range(n)]

    bezier_1 = t_1**n * np.polyval(pol_1, t_1)

    return np.concatenate((bezier_0, bezier_1))
    
def _direct(P, num_points):
    return  [_direct_aux(P, t) for t in np.linspace(0,1,num_points)]
    
def _direct_aux(P, t):
    n = P.shape[0] - 1
    bezier = 0
    for i in range(n+1):
        bezier += P[i] * comb(n,i) * t**i * (1-t)**(n-i)
    return bezier

def bezier_subdivision(P, k, epsilon, lines=False):
    '''
    Parameters
    ----------
    k :
        entero que indica el número de subdivisiones
    epsilon :
        será el umbral de parada, que mide cuán cercana a una recta está la curva
    lines :
        Si lines=True, devolverá sólo la sucesión de extremos, sin puntos intermedios.
    Returns
    -------
    np.array que contendrá la sucesión de puntos dada por los polígonos de Bézier resultantes.
    '''
    pass

def backward_differences_bezier(P, m, h=None):
    '''
    evaluará la curva de Bézier en los puntos de la forma h*k para k=0,...,m
    Se usará el método de diferencias "hacia atrás" explicado en clase
    Parameters
    ----------
    P :
    m :
        habrá m + 1 puntos
    h :
        Si h=None entonces h=1/m
    '''
    pass


def comb(n, i):
    '''
    numeros combinatorios (n choose i)
    using a dictionary
    '''
    if i == 0:
        return 1
    if n == 0:
        return 0
    if (n, i) in BINOMIAL_DICT:
        return BINOMIAL_DICT[n,i]
    BINOMIAL_DICT[n, i] = comb(n-1, i-1) + comb(n - 1, i)
    return BINOMIAL_DICT[n,i]
