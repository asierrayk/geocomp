# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
from scipy.linalg import eigh


class LDA:
    """
    Class which implements Fisher's discriminant for multiple classes.

    First trains with given points belonging to known classes.
    Then classifies using the values obtained during the training.

    Notes
    -----
    LDA stands for Lineal Discriminant Analysis.
    For further information, see Bishop, section 4.1.6

    Methods
    -------
    fit
    transform

    Atributes
    ---------
    W_LDA : projection matrix
    mean_train : mean of the total training data set

    """

    def __init__(self):
        self.W_LDA = None
        self.mean_train = None

    def fit(self, X_train, y_train, reduced_dim):
        """
        Create projection matrix.

        For that, use given training data: X_train and y_train.

        Notes
        -----
        After applying the projection matrix to the yet to be classified
        points, they will change their dimension to the given reduced_dim.

        Parameters
        ----------
        X_train :
            array of dimension (N,D) which contains
            N points with known classes.
        y_train :
            array that tells which classes the points
            from X_train belong to.
        reduced_dim :
            integer number (less than number of classes and D)
            used for dimension reduction.

        Examples
        --------
        >>> X_train = [[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]
        >>> X_train = np.array(X_train)
        >>> y_train = np.array([1, 1, 1, 2, 2, 2])
        >>> L = LDA()
        >>> L.fit(X_train, y_train, 1)
        >>> L.W_LDA
        array([[  5.55111512e-17],
               [  8.66025404e-01]])

        """
        # Save the mean value for further use
        self.mean_train = np.mean(X_train, axis=0)

        classes = np.unique(y_train)
        N, D = X_train.shape

        # S within
        S_w = np.zeros((D, D))
        for k in classes:
            X_k = X_train[y_train == k, :]
            N_k = X_k.shape[0]

            S_w += np.cov(X_k, rowvar=0, bias=1) * N_k

        # S between
        S_t = np.cov(X_train, rowvar=0, bias=1) * N
        S_b = S_t - S_w

        # Select eigenvectors whose eigenvals are the reduced_dim greatest
        eigh_vectors = eigh(S_b, S_w, eigvals=(D - reduced_dim, D - 1))[1]
        w = (eigh_vectors.T)[::-1]  # descending order
        self.W_LDA = w.T

    def transform(self, X):
        """
        Project set of points.

        Project given array of points to the space generated by the
        previously selected eigenvectors. Resulting points will be of
        dimension reduced_dim.

        Parameters
        ----------
        X :
            array of points we wish to project.

        Returns
        -------
        Array of points
            Result of projecting points in X with projection matrix W_LDA

        Examples
        --------
        >>> X_train = [[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]
        >>> X_train = np.array(X_train)
        >>> y_train = np.array([1, 1, 1, 2, 2, 2])
        >>> L = LDA()
        >>> L.fit(X_train, y_train, 1)
        >>> X_red = L.transform([[3, 0], [2, -3], [-2, -4]])
        >>> X_red
        array([[  1.66533454e-16],
               [ -2.59807621e+00],
               [ -3.46410162e+00]])

        """
        X_red = (X - self.mean_train).dot(self.W_LDA)
        return np.asarray(X_red)


class PCA:
    """
    Implements dimensionality reduction using principal component analysis.

    Notes
    -----
    For further information, see Bishop, section 12.1

    Methods
    -------
    fit
    transform

    Atributes
    ---------
    W_PCA : projection matrix
    mean_train : mean of the total training data set

    """

    def __init__(self):
        self.W_PCA = None
        self.mean_train = None

    def fit(self, X_train, reduced_dim):
        """
        Create projection matrix.

        For that, use given training data: X_train.

        Notes
        -----
        After applying the projection matrix to the yet to be classified
        points, they will change their dimension to the given reduced_dim.

        Parameters
        ----------
        X_train :
            array of dimension (N,D) which contains
            N points.
        reduced_dim :
            integer number (less than number of classes and D)
            used for dimension reduction.

        Examples
        --------
        >>> X = [[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]
        >>> X = np.array(X)
        >>> P = PCA()
        >>> P.fit(X, 1)
        >>> P.W_PCA
        array([[ 0.83849224]
               [ 0.54491354]])

        """
        N, D = X_train.shape
        self.mean_train = np.mean(X_train, axis=0)

        S_t = np.cov(X_train, rowvar=0, bias=1)
        eigh_vectors = eigh(S_t, eigvals=(D - reduced_dim, D - 1))[1]
        w = (eigh_vectors.T)[::-1]
        self.W_PCA = w.T

    def transform(self, X):
        """
        Project set of points.

        Project given array of points to the space generated by the
        previously selected eigenvectors. Resulting points will be of
        dimension reduced_dim.

        Parameters
        ----------
        X :
            array of points we wish to project.

        Returns
        -------
        Array of points
            Result of projecting points in X with projection matrix W_PCA

        Examples
        --------
        >>> X = [[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]
        >>> X = np.array(X)
        >>> P = PCA()
        >>> P.fit(X, 1)
        >>> X_red = P.transform(X)
        >>> X_red
        array([[-1.38340578]
               [-2.22189802]
               [-3.6053038 ]
               [ 1.38340578]
               [ 2.22189802]
               [ 3.6053038 ]])

        """
        X_red = (X - self.mean_train).dot(self.W_PCA)
        return X_red
