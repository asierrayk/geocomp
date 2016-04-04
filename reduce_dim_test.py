# -*- coding: utf-8 -*-
import numpy as np
#import matplotlib.pyplot as plt
from reduce_dim import LDA, PCA

#X0 = np.asarray([[1,2],[1,1]])
#X1 = np.asarray([[3,2],[4,7]])
        
X_train = np.asarray([[1,2,3],[3,2,5],[4,7,7],[1,1,6]])
y_train = np.asarray([0,1,1,0])
X_test = np.asarray([[1,2,5],[3,2,7],[4,7,3],[1,1,9],[2,3,3]])

L = LDA()
L.fit(X_train, y_train, 2)
rt = L.transform(X_test)        
print(rt)
