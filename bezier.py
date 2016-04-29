# coding=utf-8
from __future__ import division
import numpy as np

def polyeval_bezier(P, num_points, algorithm):
    """
    Parameters
    ----------
    P :
        numpy.array P of dimension (n + 1, dim)
    num_points :
        positive integer
    algorithm :
        string with one of the following values: 'direct',
        'recursive', 'horner' o 'deCasteljau'
    Returns
    -------
    numpy.array of dimension (num_points, dim) with the values of the Bezier
    curve in the instants given by ...
    La función devolverá un numpy.array de dimensión (num_points, dim) con los
    valores de la curva de Bézier en los instantes dados por num_points valores
    equiespaciados entre 0 y 1 (incluyendo extremos).

    """
    grid = np.linspace(0,1,num_points)
    if algorithm == "direct":
        return _direct(P,num_points)
    elif algorithm == "recursive":
        # los polinomios de Bernstein se calculen usando la fórmula recursiva que los caracteriza
        return _recursive(P, num_points)
    elif algorithm == "horner":
        # método de Horner, dividiendo los valores en dos trozos:
        # los menores que 0.5 y los mayores o iguales a 0.5
        return _horner(P, num_points)
    elif algorithm == "deCasteljau":
        # evaluará la curva usando el algoritmo de De Casteljau
        return _deCasteljau(P, num_points)

def _deCasteljau(P, num_points):
    t = np.linspace(0,1,num_points)
    return np.array([_deCasteljau_aux(P, t[i]) for i in range(num_points)])

def _deCasteljau_aux(b, t):
    n = b.shape[0] - 1
    b = np.copy(P).astype("float")
    for k in range(1, n+1):
        for i in range(n+1-k): # Calculamos b[i] = (b_i)^k
            b[i] = (1-t)*b[i] + t*b[i+1]
    return b[0]

def _horner(P, num_points):
    n = P.shape[0] - 1
    t = np.linspace(0,1,num_points)

    t0 = t[:num_points/2] # first num_points/2 points
    t0 = t0[:,np.newaxis] # every point is a 1-dim array
    _t0 = 1 - t0

    t1 = t[num_points/2:] # last num_points/2 points
    t1 = t1[:,np.newaxis]
    _t1 = 1 - t1

    pol_1 = np.array([P[i] * comb(n,i) for i in range(n+1)])
    pol_0 = np.array([P[n-i] * comb(n,i) for i in range(n+1)])

    bezier0 = _t0**n * np.polyval(pol_0, t0/_t0)
    bezier1 = t1**n * np.polyval(pol_1, _t1/t1)

    return np.concatenate((bezier0, bezier1))

def _direct(P, num_points):
    return  np.array([_direct_aux(P, t) for t in np.linspace(0,1,num_points)])

def _direct_aux(P, t):
    n = P.shape[0] - 1
    # bezier = 0
    # for i in range(n+1):
    #    bezier += P[i] * comb(n,i) * t**i * (1-t)**(n-i)
    return sum(P[i]  * comb(n,i) * t**i * (1-t)**(n-i)
        for i in range(n+1))# bezier

def _recursive(P, num_points):
    return  np.array([_recursive_aux(P, t) for t in np.linspace(0,1,num_points)])

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
    diff2 = np.diff(P, n=2, axis=0) # n-1 diffs
    max_diff2 = np.max(np.linalg.norm(diff2, axis=1))
    if lines and n*(n-1)/8 * max_diff2 < epsilon:
        return np.array([P[0], P[-1]])

    # case 0
    if k == 0 or max_diff2 < epsilon:
        return P

    # subdivision
    P0, P1 = subdivision(P)
    R0 = bezier_subdivision(P0, k-1, epsilon, lines)[:-1, :] # all but the last one
    R1 = bezier_subdivision(P1, k-1, epsilon, lines)
    # concatenate results and return them
    return np.vstack((R0,R1))


def subdivision(P):
    # we want the bezier polygon with 2n+1 points over [0, 0.5, 1]
    n, dim = P.shape
    n = n-1
    b = np.copy(P).astype("float")#np.vstack((np.copy(P),np.zeros(dim)))
    t = 0.5

    P0 = np.zeros((n+1, dim))
    P1 = np.zeros((n+1, dim))
    P0[0] = b[0]
    P1[0] = b[n]

    for i in range(1,n+1):
        for k in range(n-i+1):
            b[k] = t*(b[k] + b[k+1])
        P0[i] = b[0]
        P1[i] = b[n-i]

    return P0, P1[::-1, :]


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
    # primero hay que coger los p0...pn con horner
    if h == None:
        h = 1 / m
    points = _horner(P, )
    _, num_points = P.shape
    for i in range(num_points):
        diff_p[i] = np.diff(P, num_points - 1)




BINOMIAL_DICT = dict()
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


RECURSIVE_BERNSTEIN_DICT = dict()
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
