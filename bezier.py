# coding=utf-8
from __future__ import division
import numpy as np

def polyeval_bezier(P, num_points, algorithm):
    """
    Evaluate a Bezier curve given an algorithm.

    Evaluate the Bezier curve given by the Bezier polygon P
    in num_points equally-spaced instants between 0 and 1 included.

    Parameters
    ----------
    P :
        numpy.array of dimension (n + 1, dim). Specifies the Bezier polygon.
    num_points :
        positive integer
    algorithm :
        string with one of the following values: 'direct',
            'recursive', 'horner' o 'deCasteljau'

    Returns
    -------
    numpy.array of dimension (num_points, dim) with the values of the Bezier
        curve in the instants given by num_points equally-spaced values between
        0 and 1 included.
        
    Examples
    --------  
    >>> P = np.asarray([[0,0],[1,0],[1,1]])
    >>> num_points = 5

    >>> polyeval_bezier(P, num_points, "recursive")
    array([[ 0.    ,  0.    ],
           [ 0.4375,  0.0625],
           [ 0.75  ,  0.25  ],
           [ 0.9375,  0.5625],
           [ 1.    ,  1.    ]])
           
    """
    t = np.linspace(0,1,num_points)
    if algorithm == "direct":
        return _direct(P,t)
    elif algorithm == "recursive":
        # using the recursive formula
        return _recursive(P, t)
    elif algorithm == "horner":
        # Horner method
        return _horner(P, t)
    elif algorithm == "deCasteljau":
        # De Casteljau algorithm
        return _deCasteljau(P, t)

def _deCasteljau(P, t):
    """
    Evaluate Bezier curve given by P applying de Casteljau's algorithm.

    Apply recursive relation in Bernstein polynomials to achieve the
    algorithm.

    Parameters
    ----------
    P:
        numpy.array P of dimension (n + 1, dim)
    t:
        numpy.array t of dimension (num_points)
        num_points are the points in which we want to evaluate the Bezier curve

    Returns
    -------
    np.array containing  sequence of points given by the resulting
        Bézier polygons

    """

    n = b.shape[0] - 1
    t = t[:,np.newaxis]
    _t = 1 - t

    b = np.copy(P).astype("float")
    for k in range(1, n+1):
        for i in range(n+1-k): # b[i] = b_i^k
            b[i] = _t*b[i] + t*b[i+1]
    return b[0]
    #return np.array([_deCasteljau_aux(P, i) for i in t])

def _deCasteljau_aux(b, t):
    n = b.shape[0] - 1
    b = np.copy(P).astype("float")

    for k in range(1, n+1):
        for i in range(n+1-k): # Calculamos b[i] = (b_i)^k
            b[i] = (1-t)*b[i] + t*b[i+1]
    return b[0]

def _horner(P, t):
    """
    Evaluate Bezier curve in the points using the horner algorithm to evaluate
    the Bezier curve.

    Notes
    -----
    For further information, see Bézier and B-Spline Techniques (Prautzsch, Hartmut, Boehm, Wolfgang, Paluszny, Marco)
    section 2.3 (observation 4)

    Parameters
    ----------
    P :
        numpy.array of dimension (n + 1, dim)
    t :
        numpy.array of dimension (num_points)
        Contains the points in which we want to evaluate the Bezier curve

    Returns
    -------
    np.array containing sequence of points given by the resulting
        Bézier polygons

    """
    n = P.shape[0] - 1
    num_points = t.shape[0]

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

def _direct(P, t):
    """
    Evaluate Bezier curve in the points using a direct method

    Parameters
    ----------
    P :
        numpy.array P of dimension (n + 1, dim)
    t :
        numpy.array t of dimension (num_points)
        Contains the points in which we want to evaluate the Bezier curve
    Returns
    -------
    np.array containing sequence of points given by the resulting
        Bézier polygons

    """
    # b(t) = sum_i P(i) B(n,i,t)
    # B(n,i,t) = (n C i) t**i * (1-t)**(n-i)
    n = P.shape[0] - 1
    #t = t[:, np.newaxis]#[1, 2, 3] => [[1], [2], [3]]
    _t = 1-t
    return sum(P[i]  * comb(n,i) * t[:,np.newaxis]**i * (_t[:,np.newaxis])**(n-i)
        for i in range(n+1))# bezier


def _recursive(P,t):
    """
    Evaluate Bezier curve in the points using a recursive method to calculate
    the Bernstein polynomial

    Parameters
    ----------
    P :
        numpy.array P of dimension (n + 1, dim)
    t :
        numpy.array t of dimension (num_points)
        Contains the points in which we want to evaluate the Bezier curve
    Returns
    -------
    np.array containing sequence of points given by the resulting
        Bézier polygons

    """
    n = P.shape[0] - 1
    RECURSIVE_BERNSTEIN_DICT.clear() # For each t clear the dictionary
    return sum(P[i] * bernstein(n,i,t)[:,np.newaxis] for i in range(n+1))

def bezier_subdivision(P, k, epsilon, lines=False):
    """
    Generate the Bezier curve using subdivision method.

    Notes
    -----
    For further information, see Bézier and B-Spline Techniques (Prautzsch, Hartmut, Boehm, Wolfgang, Paluszny, Marco)
    sections 3.3 - 3.5
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
    np.array containing sequence of points given by the resulting
        Bézier polygons
    
    Examples
    --------
    >>> P = np.asarray([[0,0],[1,0],[1,1]])
    >>> k = 5
    >>> epsilon = 0.1

    >>> bezier_subdivision(P, k, epsilon,False)
    array([[ 0.    ,  0.    ],
           [ 0.25  ,  0.    ],
           [ 0.4375,  0.0625],
           [ 0.625 ,  0.125 ],
           [ 0.75  ,  0.25  ],
           [ 0.875 ,  0.375 ],
           [ 0.9375,  0.5625],
           [ 1.    ,  0.75  ],
           [ 1.    ,  1.    ]])
           
    >>> bezier_subdivision(P, k, epsilon,True)
    array([[ 0.  ,  0.  ],
           [ 0.75,  0.25],
           [ 1.  ,  1.  ]])

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
    """
    Calculate a Bezier polygon with 2*n+1 points.

    Parameters
    ----------
    P :
        numpy.array of dimension (n + 1, dim). Specifies the Bezier polygon.

    Returns
    -------
    two numpy.array, each one with the Bezier polygon from 0 to 0.5
        and from 0.5 to 1, respectively.

    """
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
    Calculate Bezier curve applying backward differences method.

    Find the initial points of the Bezier curve given by conrol points
    in P.
    Use the backward differences method, by first applying it forward
    to get the n-th order differences of the previously calculated points
    , and then applying it backwards to get the extended points
    p_n+1,...,p_m

    Notes
    -----
    For further information, see Metdos de Bezier y B-splines section 3.6
    by Prautzsch, Bohm, Paluszny.

    Parameters
    ----------
    P :
        initial set of points
    m :
        number of parts of the partition, m + 1 points
    h :
        length of each part of the partition, if h == None then h = 1/m

    Returns
    -------
    The obtained bezier curve

    """
    # primero hay que coger los p0...pn con horner
    if h == None:
        h = 1 / m

    n = P.shape[0] - 1
    dim = P.shape[1]
    t = np.arange(0, (n + 1)*h, h)


    points = _horner(P, t)
    delta = np.zeros((n+1,m-n+1,dim))

    # forward
    dif = [np.diff(points.T, i).T for i in range(n+1)]
    delta[n] = np.repeat(dif[n], m-n+1, axis=0)

    #backward
    for k in range(n-1, -1, -1):
        col_next = delta[k + 1]
        col_next[0] = col_next[0] + dif[k][n-k] # addition
        delta[k] = np.cumsum(col_next, axis=0)
        # cumSum(r,col_next)# tri_matrix.dot(indep_terms)

    return np.vstack((points, delta[0][:-1, :]))



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
    num_points = t.shape[0]
    _t = 1 - t
    if i < 0 or i > n:
        return np.zeros(num_points)
    if n == 0: # then i = 0 B_0^0
        return np.ones(num_points)
    if (n, i) in RECURSIVE_BERNSTEIN_DICT:
        return RECURSIVE_BERNSTEIN_DICT[(n, i)]
    RECURSIVE_BERNSTEIN_DICT[(n, i)] = t*bernstein(n-1, i-1,t) + _t*bernstein(n-1, i,t)
    return RECURSIVE_BERNSTEIN_DICT[(n, i)]
