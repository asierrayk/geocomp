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
        # evaluación directa de los polinomios de Bernstein
        pass
    elif algorithm == "recursive"
        # los polinomios de Bernstein se calculen usando la fórmula recursiva que los caracteriza
        pass
    elif algorithm == "horner":
        # método de Horner, dividiendo los valores en dos trozos: los menores que 0.5 y los mayores o iguales a 0.5
        _horner(P, t, num_points)
    elif algorithm == "deCasteljau":
        # evaluará la curva usando el algoritmo de De Casteljau
        _deCasteljau(P, t)

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
    return BINOMIAL_DICT[n
