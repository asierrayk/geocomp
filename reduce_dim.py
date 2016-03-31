# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np 
from scipy.linalg import eigh 

class LDA:
    
    def __init__(self):
        self.W
        self.mean_train = None
    
    def fit(self, X_train, y_train, reduced_dim):
        pass #type your code here
        X0 = np.asarray([[1,2],[1,1]])
        X1 = np.asarray([[3,2],[4,7]])
        
        X_train = np.asarray([[1,2],[3,2],[4,7],[1,1]])
        y_train = np.asarray([0,1,1,0])
        
        self.mean_train = np.mean(X_train, axis=0)                
        
        K = max(y_train) + 1
        N, D = X_train.shape
        S_w = np.zeros((D,D))
        for k in [0,K]:
            X[k] = [X_train[i] for i in range (0,N) if y_train[i]==k]
            mean_k = np.mean(X[k], axis=0)                
            
            S[k] = np.cov(X[k], rowvar=0, bias=1) * X[k].shape[0]
            S_w += s[k]
            
            S_b += x[k].shape[0] * (mean_k - mean_train).dot((mean_k - mean_train).T)            
            
        eigh_values, eigh_vectors = eigh(np.linalg.solve(S_w, S_b))
        self.W = np.take(eigh_vectors, range(D-reduced_dim, D)
        
    def transform(self, X):
        pass #type your code here

class PCA:
    
    def fit(self, X_train, reduced_dim):
        pass #type your code here

    def transform(self, X):
        pass #type your code here
