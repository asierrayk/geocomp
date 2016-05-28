import matplotlib.pyplot as plt

'''
event.button:
1 - left click
2 - middle click
3 - right click
4 - scroll up
5 - scroll down
'''
class MoveCircles():
    def __init__(self):
        self.figure, self.axes = plt.subplots(figsize=(10, 10))
        self.axes.set_xlim(-10, 10)
        self.axes.set_ylim(-10, 10)
        self.touched_circle = None
        self.cid_press = self.figure.canvas.mpl_connect('button_press_event', self.click_event)
        self.cid_move = self.figure.canvas.mpl_connect('motion_notify_event', self.motion_event)
        self.cid_release = self.figure.canvas.mpl_connect('button_release_event', self.release_event)

    def click_event(self, event):
        if event.button == 3:
            self.figure.canvas.mpl_disconnect(self.cid_press)
            self.figure.canvas.mpl_disconnect(self.cid_move)
            self.figure.canvas.mpl_disconnect(self.cid_move)
            plt.close()
            return

        self.initial_event = event

        for c in self.axes.artists:
            if c.contains(event)[0]:
                self.touched_circle = c
                self.x0, self.y0 = c.center
                return

        c = plt.Circle((event.xdata, event.ydata), radius=0.5)
        self.axes.add_artist(c)
        self.figure.canvas.draw()

    def motion_event(self, event):
        if self.touched_circle == None:
            return
        if event.inaxes == self.axes:
            dx = event.xdata - self.initial_event.xdata
            dy = event.ydata - self.initial_event.ydata
            self.touched_circle.center = self.x0 + dx, self.y0 + dy
            self.figure.canvas.draw()

    def release_event(self, event):
        self.touched_circle = None


class DrawLine():
    def __init__(self):
        self.figure, self.axes = plt.subplots(figsize=(10, 10))
        self.axes.set_xlim(-10, 10)
        self.axes.set_ylim(-10, 10)
        self.touched_circle = None
        self.circles = []
        self.line = None
        self.cid_press = self.figure.canvas.mpl_connect('button_press_event', self.click_event)
        self.cid_move = self.figure.canvas.mpl_connect('motion_notify_event', self.motion_event)
        self.cid_release = self.figure.canvas.mpl_connect('button_release_event', self.release_event)

    def click_event(self, event):
        if event.button == 3:
            self.figure.canvas.mpl_disconnect(self.cid_press)
            self.figure.canvas.mpl_disconnect(self.cid_move)
            self.figure.canvas.mpl_disconnect(self.cid_move)
            plt.close()
            return

        self.initial_event = event

        for c in self.axes.artists:
            if c.contains(event)[0]:
                self.touched_circle = c
                self.x0, self.y0 = c.center
                return

        c = plt.Circle((event.xdata, event.ydata), radius=0.5)
        self.circles.append(c)
        if not self.line:
            self.line = plt.Line2D(*zip(*map(lambda x: x.center, self.circles)))
            self.axes.add_line(self.line)
        else:
            self.line.set_data(*zip(*map(lambda x: x.center, self.circles)))
        self.axes.add_artist(c)
        self.figure.canvas.draw()

    def motion_event(self, event):
        if self.touched_circle == None:
            return
        if event.inaxes == self.axes:
            dx = event.xdata - self.initial_event.xdata
            dy = event.ydata - self.initial_event.ydata
            self.touched_circle.center = self.x0 + dx, self.y0 + dy
            self.line.set_data(*zip(*map(lambda x: x.center, self.circles)))
            self.figure.canvas.draw()

    def release_event(self, event):
        self.touched_circle = None

####
'''
ax.set_title('click to build line segments')
'''
###
mv = MoveCircles()
dl = DrawLine()
##
plt.show()
