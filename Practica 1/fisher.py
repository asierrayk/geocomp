# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 23:23:52 2016

"""

from __future__ import division
import numpy as np


class Fisher:

    """
    Class which solves classification problems for two classes, applying
    Fisher's Linear Discriminant.
    First trains with given points with known classes.
    Then classifies using the values obtained during the training.

    Methods
    -------
    set_threshold
    train_fisher
    classify_fisher

    Atributes
    ---------
    w : weights vector
    c : threshold

    """

    def __init__(self):
        self.w = None  # Vector de pesos
        self.c = None  # Umbral

    def set_threshold(self, mu, sigma, N):
        """
        Set threshold value.

        Notes
        -----
        This is an auxiliary function only to be used from method train_fisher

        Parameters
        ----------
        mu :
            list which contains values of mu0 and mu1
        sigma :
            list which contains values of sigma0 and sigma1
        N :
            list which contains values of N0 and N1

        """
        a = -1 / 2 / sigma[0]**2 + 1 / 2 / sigma[1]**2
        b = mu[0] / sigma[0]**2 - mu[1] / sigma[1]**2
        c = -1 / 2 * mu[0]**2 / sigma[0]**2 + 1 / 2 * mu[1]**2 / \
            sigma[1]**2 + np.log(N[0] / sigma[0]) - np.log(N[1] / sigma[1])
        poli = np.asarray([a, b, c])
        roots = np.roots(poli)

        if 2 * a * roots[1] + b < 0:
            self.c = roots[1]
        else:
            self.c = roots[0]

    def train_fisher(self, X0, X1):
        """
        Set up internally the values of the weight vector: self.w,  and
        threshold: self.c
        Do so from the given training lists of points, X0 and X1

        Notes
        -----
        X0 and X1 can contain points of any dimension, but all of them should
        have the same dimension

        Parameters
        ----------
        X0 :
            List of points belonging to class 0
        X1 :
            List of points belonging to class 1

        Examples
        --------
        >>> F = Fisher()
        >>> F.train_fisher([[1,2],[1,1]], [[-1,-2],[-2,-2]])

        >>> F.w
        array([-0.58123819, -0.81373347])

        >>> F.c
        0.69792998921064653

        """

        X0 = np.asarray(X0)
        N0, D0 = X0.shape
        M0 = np.mean(X0, axis=0)  # Media en las filas (cada fila es un punto)
        S0 = np.cov(X0, rowvar=0, bias=1) * N0

        X1 = np.asarray(X1)
        N1, D1 = X1.shape  # D1 y D2 deberian ser iguales
        M1 = np.mean(X1, axis=0)
        S1 = np.cov(X1, rowvar=0, bias=1) * N1

        # HALLAR w

        Sw = S0 + S1
        dir_w = np.linalg.solve(Sw, (M1 - M0))
        # direccion del discriminante de Fisher
        self.w = dir_w / np.linalg.norm(dir_w)

        # HALLAR UMBRAL c

        # umbral que minimiza la probabilidad de error
        # busco c en  p(c,C1) = p(c,C2)  con
        # p(c,Ci) = p(c|Ci)*p(Ci) = N(y|mu,sig)* Ni/N
        # N(y|mu,sig) = 1/(sq(2*pi)*sig) * exp(- ((y-mu)/sig)^2 )

        mu0 = np.dot(self.w, M0)
        mu1 = np.dot(self.w, M1)
        sigma0 = np.std(X0.dot(self.w))
        sigma1 = np.std(X1.dot(self.w))

        self.set_threshold([mu0, mu1], [sigma0, sigma1], [N0, N1])

    def classify_fisher(self, X):
        """
        Classify list of points, applying Fisher's Linear Discriminant

        Parameters
        ----------
        X :
            List of points we wish to classify.

        Returns
        -------
        List of integers
            Contains the class index for every point in the input.
            The i-th element of the output list represents the class index
            of the i-th element in the input

        Examples
        --------
        >>> F = Fisher()
        >>> F.train_fisher([[1,2],[1,1]], [[-1,-2],[-2,-2]])
        >>> F.classify_fisher([[1,1],[1,-2],[1.4,-3.2],[-1.1,-2.1]])
        [0, 1, 1, 1]

        """

        X = np.asarray(X)
        result = np.dot(self.w, X.T) >= self.c
        return result.astype(int).tolist()
