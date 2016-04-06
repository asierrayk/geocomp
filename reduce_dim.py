# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np 
from scipy.linalg import eigh 

class LDA:
    
    def __init__(self):
        self.W_LDA = None
        self.mean_train = None
        self.rd = None
    
    def fit(self, X_train, y_train, reduced_dim):
    
        self.mean_train = np.mean(X_train, axis=0)                
        
        K = np.unique(y_train)#max(y_train) + 1
        N, D = X_train.shape
        
        # S within
        S_w = np.zeros((D,D))
        for k in K:
            #print "clase --------------------------------------------", k
            X_k = X_train[y_train == k, :]
            
            #i] for i in range(N) if y_train[i]==k])
            N_k = X_k.shape[0]
            
            S_w += np.cov(X_k, rowvar=0, bias=1) * N_k
            
        # S between
        S_t = np.cov(X_train, rowvar=0, bias=1) * N
        S_b = S_t - S_w
        #print "Sw, Sb"
        #print S_w
        #print S_b
        
        eigh_vectors = eigh(S_b, S_w, eigvals=(D-reduced_dim, D-1))[1]
        aux1 = (eigh_vectors.T)[::-1]
        
        
        self.W_LDA = aux1.T
        self.rd = reduced_dim
        
    def transform(self, X):
        #print "X ", X
        #print "mean_t ", self.mean_train
        #print "W ", self.W_LDA
        sol1 = (X - self.mean_train).dot(self.W_LDA)
        print "lasformas"
        print sol1.shape
        print X.shape[0], self.rd
        sol1 = np.asarray(sol1)
        return np.asarray(sol1)#sol1 #np.zeros((X.shape[0],self.rd))
            
class PCA:

    def __init__(self):
        self.W_PCA = None
        self.mean_train = None   
        self.rd = None
    
    def fit(self, X_train, reduced_dim):        
        '''N, D = X_train.shape
        self.mean_train = np.mean(X_train, axis=0)                
        
        S_t = np.cov(X_train, rowvar=0, bias=1)
        eigh_values, eigh_vectors = eigh(S_t)
        self.W_PCA = np.take(eigh_vectors.T, range(D-reduced_dim, D), axis=0) 
        '''
        self.rd = reduced_dim
            
    def transform(self, X):
        #a = (X-self.mean_train).dot(self.W_PCA.T)
        return np.zeros((X.shape[0],self.rd))
        