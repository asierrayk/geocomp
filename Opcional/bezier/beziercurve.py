import matplotlib.pyplot as plt
import numpy as np
from bezier import polyeval_bezier as ev
# ev(P, num_points, alg) with 'direct','recursive', 'horner' o 'deCasteljau'

class BezierCurve:
	def __init__(self):
		self.n = 100 # number of points for aproximation
		self.xs = [] #line
		self.ys = [] #line
		self.line = None #polygone
		self.curve = None
	
	def addPoint(self, x, y): 
		'''
		podria devolver 
		el poligono (linea)
		la curva (linea con mas puntos)
		'''
		self.xs.append(x)
		self.ys.append(y)
		polygon = np.asarray(zip(self.xs, self.ys))
		self.curve = ev(polygon, self.n, 'horner')
		#curve_xs = 
		#curve_ys = [e[1] for e in curve]

		'''
		# len(xs) != 0
		if len(self.xs) == 1 :
			self.line = plt.Line2D(self.xs, self.ys)
			self.curve = plt.Line2D(curve_xs, curve_ys)
			# deben ser agregado a exes : self.ax.add_line(line)
		else :
			self.line.set_data(self.xs, self.ys)
			self.curve.set_data(curve_xs, curve_ys)

		#print self.xs, self.ys
		#print curve

		#return self.line, self.curve

		'''
	def getPolygon(self):
		return self.xs, self.ys
		
	def getCurve(self):
		return [e[0] for e in self.curve], [e[1] for e in self.curve]


# example
pp = [[0,0], [1,2], [3,2], [4,0]]
bc = BezierCurve()
for x in pp:
	bc.addPoint(x[0], x[1])
x,y = bc.getPolygon()
u,t = bc.getCurve()
print zip(x, y)
print 'sep'
print zip(u,t)