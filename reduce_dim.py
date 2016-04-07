# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
from scipy.linalg import eigh


class LDA:

    def __init__(self):
        self.W_LDA = None
        self.mean_train = None

    def fit(self, X_train, y_train, reduced_dim):

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

        eigh_vectors = eigh(S_b, S_w, eigvals=(D - reduced_dim, D - 1))[1]
        w = (eigh_vectors.T)[::-1]
        self.W_LDA = w.T

    def transform(self, X):
        X_red = (X - self.mean_train).dot(self.W_LDA)
        return np.asarray(X_red)


class PCA:

    def __init__(self):
        self.W_PCA = None
        self.mean_train = None

    def fit(self, X_train, reduced_dim):
        N, D = X_train.shape
        self.mean_train = np.mean(X_train, axis=0)

        S_t = np.cov(X_train, rowvar=0, bias=1)
        eigh_vectors = eigh(S_t, eigvals=(D - reduced_dim, D - 1))[1]
        w = (eigh_vectors.T)[::-1]
        self.W_PCA = w.T

    def transform(self, X):
        X_red = (X - self.mean_train).dot(self.W_PCA)
        return X_red
