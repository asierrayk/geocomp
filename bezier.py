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
    La función devolverá un numpy.array de dimensión (num_points, dim) con los
    valores de la curva de Bézier en los instantes dados por num_points valores
    equiespaciados entre 0 y 1 (incluyendo extremos).
    '''
    grid = np.linspace(0,1,num_points)
    if algorithm == "direct":
        return _direct(P,num_points)
    elif algorithm == "recursive":
        # los polinomios de Bernstein se calculen usando la fórmula recursiva que los caracteriza
        pass
    elif algorithm == "horner":
        # método de Horner, dividiendo los valores en dos trozos:
        # los menores que 0.5 y los mayores o iguales a 0.5
        return _horner(P, num_points)
    elif algorithm == "deCasteljau":
        # evaluará la curva usando el algoritmo de De Casteljau
        _deCasteljau(P, num_points)

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

def _recursive(P, num_points):
    return  [_recursive_aux(P, t) for t in np.linspace(0,1,num_points)]

def _recursive_aux(P,t):
    n = P.shape[0] - 1
    bezier = 0
    for i in range(n+1):
        bezier += P[i] * bernstein(n,i,t)
    RECURSIVE_BERNSTEIN_DICT.clear() # For each t clear the dictionary
    return bezier

def bezier_subdivision(P, k, epsilon, lines=False):
    """
    Parameters
    ----------
    k :
        integer which indicates the number of subdivisions to be made.
    epsilon :
        stopping threshold, which measures how close to a line
            will the curve be.
    lines :
        if lines=True, it will return only a sequence of extremal points,
            without intermediate points.
    Returns
    -------
    np.array containing  sequence of points given by the resulting
        Bézier polygons

    """

    n = P.shape[0] - 1

    # almost straight lines
    diff2 = np.diff(P, n=2, axis=0) # n-1 points
    max_diff2 = np.max(np.linalg.norm(diff2, axis=1))
    if lines and n*(n-1)/8 * max_diff2 < epsilon:
        return np.array([P[0], P[-1]])

    # case 0
    if k == 0 or max_diff2 < epsilon:
        return P

    # subdivision
    P0, P1 = subdivision(P, n)
    bezier_subdivision(P0, k-1, epsilon, lines)
    bezier_subdivision(P1, k-1, epsilon, lines)
    # concatenate results and return them


def subdivision(P, n):
    # we want the bezier polygon with 2n+1 points over [0, 0.5, 1]
    pass



def backward_differences_bezier(P, m, h=None):
    """
    Evaluate Bezier curve in the points...
    evaluará la curva de Bézier en los puntos de la forma h*k para k=0,...,m
    Se usará el método de diferencias "hacia atrás" explicado en clase
    Parameters
    ----------
    P :
    m :
    h :
        if h == None then h = 1/m
        Si h=None entonces h=1/m
    """
    _, num_points = P.shape
    diff_p = np.diff(P, num_points - 1)



def comb(n, i):
    '''
    Computes the value of binomial coefficients (n choose i)
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

def bernstein(n, i, t):
    '''
    Return the degree n Bernstein polynomial of the specified index i evaluated on t (B_i^n(t)),
    With i dominated by n, using a dictionary.
    '''
    if i < 0 or i > n:
        return 0
    if n == 0: # then i = 0 B_0^0
        return 1
    if (n, i) in RECURSIVE_BERNSTEIN_DICT:
        return RECURSIVE_BERNSTEIN_DICT[n,i]
    RECURSIVE_BERNSTEIN_DICT[n, i] = t*bernstein(n-1, i-1,t) + (1-t)*bernstein(n-1, i,t)
    return RECURSIVE_BERNSTEIN_DICT[n,i]
