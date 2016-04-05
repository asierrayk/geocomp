# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np 
from scipy.linalg import eigh 

class LDA:
    
    def __init__(self):
        self.W_LDA = None
        self.W_LDA2 = None
        self.mean_train = None
    
    def fit(self, X_train, y_train, reduced_dim):
    
        self.mean_train = np.mean(X_train, axis=0)                
        
        K = max(y_train) + 1
        N, D = X_train.shape
        
        S_w = np.zeros((D,D))
        for k in range(0,K):
            #print "clase --------------------------------------------", k
            X_k = np.asarray([X_train[i] for i in range(0,N) if y_train[i]==k])
            mean_k = np.mean(X_k, axis=0) 
            N_k = X_k.shape[0]
            
            # S within
            S_w += np.cov(X_k, rowvar=0, bias=1) * N_k
            
        # S between
        S_t = np.cov(X_train, rowvar=0, bias=1) * N
        S_b = S_t - S_w
        #print "Sw, Sb"
        #print S_w
        #print S_b
        
        
        eigh_values, eigh_vectors = eigh(S_b, S_w) #aux4
        #eigh_vectors = (eigh_vectors.T)[::-1]
        aux1 = eigh_vectors[:, range(D-1, D-reduced_dim-1, -1)]
        #aux1 = np.take(eigh_vectors, range(reduced_dim), axis=0)  
        
        
        #aux2 = np.take(eigh_vectors.T, range(D-1, D-reduced_dim-1, -1), axis=0)
        aux22 = np.take(eigh_vectors.T, range(D-reduced_dim,D), axis=0)
        print "sol: ", aux1 
        #print "sol2 ", aux2
        print "sol3", aux22.T
        self.W_LDA = aux22.T
        self.W_LDA2 = aux1
        
    def transform(self, X):
        #print "X ", X
        #print "mean_t ", self.mean_train
        #print "W ", self.W_LDA
        sol1 = (self.mean_train - X).dot(self.W_LDA)
        sol2 = (self.mean_train - X).dot(self.W_LDA2)
        print sol2
        print sol1
        return sol2
            
class PCA:

    def __init__(self):
        self.W_PCA = None
        self.mean_train = None   
    
    def fit(self, X_train, reduced_dim):        
        N, D = X_train.shape
        self.mean_train = np.mean(X_train, axis=0)                
        
        S_t = np.cov(X_train, rowvar=0, bias=1)
        eigh_values, eigh_vectors = eigh(S_t)
        self.W_PCA = np.take(eigh_vectors.T, range(D-reduced_dim, D), axis=0)     
            
    def transform(self, X):
        return (X-self.mean_train).dot(self.W_PCA.T)
        