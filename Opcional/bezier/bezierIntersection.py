# -*- coding: utf-8 -*-
#import matplotlib.pyplot as plt
#from bezier import polyeval_bezier as ev
#import numpy as np

class BezierIntersection():
    
    def __init__(self):
        self.figure, self.axes = plt.subplots(figsize=(10, 10))
        self.axes.set_xlim(-10, 10)
        self.axes.set_ylim(-10, 10)
        self.touched_circle = None
        self.line = None
        self.cid_press = self.figure.canvas.mpl_connect('button_press_event', self.click_event)
        self.cid_move = self.figure.canvas.mpl_connect('motion_notify_event', self.motion_event)
        self.cid_release = self.figure.canvas.mpl_connect('button_release_event', self.release_event)
        self.cid_pick = self.figure.canvas.mpl_connect('pick_event', self.pick_event)




if __name__ == '__main__':
    #%matplotlib qt
    b = BezierInteractive()
