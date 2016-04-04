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
        
        K = max(y_train) + 1
        N, D = X_train.shape
        #print "N:", N, "D:", D, "K:", K, "D':",reduced_dim
        S_w = np.zeros((D,D))
        S_b = np.zeros((D,D))
        for k in range(0,K):
            #print "clase --------------------------------------------", k
            
            X_k = np.asarray([X_train[i] for i in range(0,N) if y_train[i]==k])
            #print "X_k ", X_k
            mean_k = np.mean(X_k, axis=0) 
            N_k = X_k.shape[0]
            
            # S within
            for x in X_k:
                aux5 = np.outer((x - mean_k),(x - mean_k))
                S_w += aux5
            #S_w += np.cov(X_k, rowvar=0, bias=1) * N_k
            
            # S between
            aux = N_k * np.outer((mean_k - self.mean_train),(mean_k - self.mean_train))
            #print "Sb_k ",aux
            S_b += aux            
            
        #aux3 = np.linalg.solve(S_w, S_b)
        #aux4 = np.linalg.inv(S_w) * S_b
        #print "Sw, Sb"
        #print S_w
        #print S_b
        #print "matriz nada",
        eigh_values, eigh_vectors = eigh(S_b, S_w) #aux4
        #print "autoval ", eigh_values
        #print "autovec ", eigh_vectors
        aux2 = np.take(eigh_vectors.T, range(D-1, D-reduced_dim-1, -1), axis=0)
        aux22 = np.take(eigh_vectors.T, range(D-reduced_dim,D), axis=0)
        #print "sol: ", aux2 , aux22
        self.W_LDA = aux22
        
    def transform(self, X):
        #print "X ", X
        #print "mean_t ", self.mean_train
        #print "W ", self.W_LDA
        return (X - self.mean_train).dot(self.W_LDA.T)
            
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
        