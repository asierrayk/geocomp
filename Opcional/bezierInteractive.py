# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from bezier import polyeval_bezier as ev
import numpy as np

class BezierInteractive():
    def __init__(self):
        self.figure, self.axes = plt.subplots(figsize=(10, 10))
        self.axes.set_xlim(-10, 10)
        self.axes.set_ylim(-10, 10)
        self.touched_circle = None
        self.line = []
        self.curve = []
        self.ind_point = 0
        self.ind_curve = 0
        self.ind = 0
        self.polygon = []
        self.newCurve = True
        self.drag = False
        self.cid_press = self.figure.canvas.mpl_connect('button_press_event', self.click_event)
        self.cid_move = self.figure.canvas.mpl_connect('motion_notify_event', self.motion_event)
        self.cid_release = self.figure.canvas.mpl_connect('button_release_event', self.release_event)
        self.cid_pick = self.figure.canvas.mpl_connect('pick_event', self.pick_event)
        self.key_cid = self.figure.canvas.mpl_connect('key_press_event', self.on_key)
        self.colors = ['b','g','c','m','y','k']
        self.ind = 0
        
    
    def click_event(self, event):
        if event.button == 2:
            self.figure.canvas.mpl_disconnect(self.cid_press)
            self.figure.canvas.mpl_disconnect(self.cid_move)
            self.figure.canvas.mpl_disconnect(self.cid_move)
            plt.close(self.figure)
            return
        
        if event.button == 3:
            return
        
        self.initial_event = event
            
        c = plt.Circle((event.xdata, event.ydata), radius=0.3, color = self.colors[self.ind % len(self.colors)], picker = True)
        #self.polygon = np.append(self.polygon, [[event.xdata, event.ydata]], axis=0)
        if self.newCurve:
            self.polygon.append([[event.xdata, event.ydata]])
        else:
            self.polygon[self.ind].append([event.xdata, event.ydata])
            
        self.axes.add_artist(c)
        self.drawPolygonal(self.ind)
        self.drawBezier(self.ind)
            
        self.figure.canvas.draw()
        
    def motion_event(self, event):
        if self.touched_circle == None:
            return
        if event.inaxes == self.axes:
            dx = event.xdata - self.initial_event.xdata
            dy = event.ydata - self.initial_event.ydata
            if not self.drag:
                print "entra"
                for i in xrange(len(self.polygon)):
                    for j in xrange(len(self.polygon[i])):
                        #print self.polygon[i] == list(self.touched_circle.center)
                        #print "p", self.polygon[i]
                        #print "c", self.touched_circle.center
                        if self.polygon[i][j] == list(self.touched_circle.center):
                            #print "entra"
                            self.ind_curve = i
                            self.ind_point = j
                            print "curva", self.ind_curve
                            print "punto", self.ind_point                            
                            self.drag = True
            self.touched_circle.center = self.x0 + dx, self.y0 + dy
            self.polygon[self.ind_curve][self.ind_point] = list(self.touched_circle.center)
            self.drawPolygonal(self.ind_curve)
            self.drawBezier(self.ind_curve)          
            
            self.figure.canvas.draw()
        
    def release_event(self, event):
        self.touched_circle = None
        self.drag = False
        
    def pick_event(self, event):
        self.initial_event = event.mouseevent
        if event.mouseevent.button != 3:
            return
        self.touched_circle = event.artist
        self.x0 = event.mouseevent.xdata
        self.y0 = event.mouseevent.ydata
        
    def on_key(self, event):
        if event.key == ' ' :
            print ('you pressed space > new curve')
            self.ind = self.ind + 1
            #self.polygon[self.ind] = zip(*map(lambda x: x.center, self.axes.artists))
            self.newCurve = True
    
    def drawPolygonal(self, ind):
        if self.newCurve:
            p = plt.Line2D(*zip(*(self.polygon[ind])), color = '0.25')
            self.line.append(p)
            self.axes.add_line(self.line[ind])
        else:
            self.line[ind].set_data(*zip(*(self.polygon[ind])))
    
    def drawBezier(self, ind):    
        if self.newCurve:
            c = plt.Line2D(*zip(*(self.polygon[ind])), color = self.colors[self.ind % len(self.colors)])
            self.curve.append(c)
            self.axes.add_line(self.curve[ind])
            self.newCurve = False
        else:
            points = ev(np.asarray(self.polygon[ind]), 100, 'horner')            
            self.curve[ind].set_data(points[:,0],points[:,1])
        
if __name__ == '__main__':
    #%matplotlib qt
    b = BezierInteractive()