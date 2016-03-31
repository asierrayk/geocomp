# -*- coding: utf-8 -*-
import numpy as np
#import matplotlib.pyplot as plt
from reduce_dim import LDA, PCA

#X0 = np.asarray([[1,2],[1,1]])
#X1 = np.asarray([[3,2],[4,7]])
        
X_train = np.asarray([[1,2],[3,2],[4,7],[1,1]])
y_train = np.asarray([0,1,1,0])
X_test = np.asarray([[1,2],[3,2],[4,7],[1,1]])
X_train[0]

L = LDA()
L.fit(X_train, y_train, 1)
rt = L.transform(X_test)        
print(rt)
