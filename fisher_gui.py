import numpy as np
import matplotlib.pyplot as plt
from fisher import Fisher    
     
Dim = 2
N0 = 15
N1 = 12
N = 8

# N(\mu, \sigma^2) = sigma * np.random.randn(...) + mu

mu0 = np.array([10, 0])
X0 = np.random.randn(N0,Dim) + mu0
print "X0", X0
mu1 = np.array([-10, 10])
X1 = 2*np.random.randn(N1,Dim) + mu1
print "X1", X1
X = 7*np.random.randn(N,Dim)

#X0_list = [[1,4],[1,5],[2,4]] #ejemplo
#X1_list = [[3,3],[4,5],[6,9],[5,5]] #ejemplo
X0_list = X0.tolist()
X1_list = X1.tolist()
F = Fisher()
F.train_fisher(X0_list,X1_list)
print "Clasificacion", F.classify_fisher(X)

########## GUI #################
plt.plot(X0[:,0], X0[:,1], 'o')
plt.plot(X1[:,0], X1[:,1], 'o')
plt.plot(X[:,0], X[:,1], 'o')

Xs = np.linspace(-15,15,300)
Ys = np.linspace(-15,15,300)
XX, YY = np.meshgrid(Xs,Ys)
x, y = XX.flatten(), YY.flatten()
pts = np.hstack((x[:,np.newaxis], y[:,np.newaxis]))
ZZ = np.asarray(F.classify_fisher(pts)).reshape(300,300)

plt.contour(XX,YY,ZZ)

plt.show()
#####################  
    
