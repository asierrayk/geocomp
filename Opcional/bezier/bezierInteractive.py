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
        self.indice = 0
        self.polygon = []
        self.newCurve = True
        self.drag = False
        self.cid_press = self.figure.canvas.mpl_connect('button_press_event', self.click_event)
        self.cid_move = self.figure.canvas.mpl_connect('motion_notify_event', self.motion_event)
        self.cid_release = self.figure.canvas.mpl_connect('button_release_event', self.release_event)
        self.cid_pick = self.figure.canvas.mpl_connect('pick_event', self.pick_event)
        self.key_cid = self.figure.canvas.mpl_connect('key_press_event', self.on_key)
    
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
            
        c = plt.Circle((event.xdata, event.ydata), radius=0.3, picker = True)
        #self.polygon = np.append(self.polygon, [[event.xdata, event.ydata]], axis=0)
        self.polygon.append([event.xdata, event.ydata])
        self.axes.add_artist(c)
        self.drawPolygonal()
        self.drawBezier()
            
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
                    #print self.polygon[i] == list(self.touched_circle.center)
                    #print "p", self.polygon[i]
                    #print "c", self.touched_circle.center
                    if self.polygon[i][0] == self.touched_circle.center[0] and self.polygon[i][1] == self.touched_circle.center[1]:
                        #print "entra"
                        self.indice = i
                        #print "indice", self.indice
                        self.drag = True
            print self.indice
            self.touched_circle.center = self.x0 + dx, self.y0 + dy
            self.polygon[self.indice] = [self.touched_circle.center[0], self.touched_circle.center[1]]
            self.drawPolygonal()
            self.drawBezier()          
            
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
            self.polygon[self.ind] = zip(*map(lambda x: x.center, self.axes.artists))
            self.newCurve = True
    
    def drawPolygonal(self):
        if self.newCurve:
            p = plt.Line2D(*zip(*self.polygon))
            self.line.append(p)
            self.axes.add_line(self.line[self.ind])
        else:
            self.line[self.ind].set_data(*zip(*self.polygon))
    
    def drawBezier(self):    
        if self.newCurve:
            self.curve = plt.Line2D(*zip(*map(lambda x: x.center, self.axes.artists)))
            self.axes.add_line(self.curve)
            self.newCurve = False
        else:
            xs = np.asarray(map(lambda x: x.center[0], self.axes.artists))
            ys = np.asarray(map(lambda x: x.center[1], self.axes.artists))
            P = np.vstack((xs,ys)).T
            points = ev(P, 100, 'horner')            
            self.curve.set_data(points[:,0],points[:,1])
        
if __name__ == '__main__':
    #%matplotlib qt
    b = BezierInteractive()
