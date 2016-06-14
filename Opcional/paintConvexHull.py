# -*- coding: utf-8 -*-
from convexHull import ConvexHull
import matplotlib.pyplot as plt

class DrawConvexHull:
    """
    Class which draws the convex hull of the points wich one draws.

    Methods
    -------
    click_event

    Atributes
    ---------
    figure : figure of the plot
    axes : axes of the plot
    points : points in the canvas
    hull : convex hull of points
    cid_click : conexion id for button_press_event
    """
    def __init__(self):
        self.figure, self.axes = plt.subplots(figsize=(10, 10))
        self.axes.set_xlim(-10, 10)
        self.axes.set_ylim(-10, 10)
        self.points = []

        self.hull = None
        self.cid_click = self.figure.canvas.mpl_connect('button_press_event', self.click_event)

    def click_event(self, event):
        p = plt.Circle((event.xdata, event.ydata), radius=0.3)
        self.axes.add_artist(p)

        self.points.append([event.xdata, event.ydata])
        #print 'points', self.points

        ch = ConvexHull()

        if len(self.points) == 1:
            self.hull = plt.Line2D([self.points[0][0]], [self.points[0][1]])
            self.axes.add_line(self.hull)
        elif len(self.points) >= 2:
            xs, ys = ch.graham_unzip(self.points)
            xs.append(xs[0])
            ys.append(ys[0])
            self.hull.set_data(xs, ys)

        self.figure.canvas.draw()

if __name__ == '__main__':
    dch = DrawConvexHull()
    plt.show()
