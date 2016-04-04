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
        S_w = np.zeros((D,D))
        S_b = np.zeros((D,D))
        for k in range(0,K):
            X_k = np.asarray([X_train[i] for i in range(0,N) if y_train[i]==k])
            #print(X_k)
            mean_k = np.mean(X_k, axis=0)                
            
            S_w += np.cov(X_k, rowvar=0, bias=1) * X_k.shape[0]
            
            aux = X_k.shape[0] * np.outer((mean_k - self.mean_train.T),(mean_k - self.mean_train))
            #print "Sb_k ",aux
            S_b += aux            
            
        eigh_values, eigh_vectors = eigh(np.linalg.solve(S_w, S_b))
        self.W_LDA = np.take(eigh_vectors.T, range(D-reduced_dim, D), axis=0)
        
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
        