from matplotlib import pyplot as plt
import random as rand

class LineBuilder:
    def __init__(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_title('click to build line segments')
        self.line, = ax.plot([0], [0])  # empty line
        self.xs = list(self.line.get_xdata())
        self.ys = list(self.line.get_ydata())
        self.cid = self.line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print('click', event)
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()


class Picker:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title('P i c k e r')
        self.cid_pick = self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        self.line, = self.ax.plot(rand.randint(0,100), 'o', picker=5)  # 5 points tolerance
    
    def on_pick(self, event):
        thisline = event.artist
        xdata, ydata = thisline.get_data()
        print('x:', event.mouseevent.xdata, xdata)
        print('y:', event.mouseevent.ydata, ydata)
        ind = event.ind
        print('on pick line:', zip(xdata[ind], ydata[ind]))


class LinesBuilder:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        #fig = plt.figure()
        #self.ax = fig.add_subplot(111)
        self.ax.set_title('click to build line segments')
        self.lines = []
        self.ind = 0
        self.xs = []
        self.ys = []
        self.newline = True
        #
        self.pick_cid = self.fig.canvas.mpl_connect('button_press_event', self.click_event)
        self.key_cid = self.fig.canvas.mpl_connect('key_press_event', self.on_key)

    def click_event(self, event):
        print('click', event.xdata, event.ydata)
        #if event.inaxes!=self.line.axes: return
                
        if self.newline :
            self.xs.append([event.xdata])
            self.ys.append([event.ydata])
            line = plt.Line2D(self.xs[self.ind], self.ys[self.ind])
            self.lines.append(line)
            self.ax.add_line(self.lines[self.ind])
            self.newline = False
        else:
            self.xs[self.ind].append(event.xdata)
            self.ys[self.ind].append(event.ydata)
            print('lineas:', self.ind)
            print zip(self.xs[self.ind], self.ys[self.ind])
            self.lines[self.ind].set_data(self.xs[self.ind], self.ys[self.ind])
        self.fig.canvas.draw()
    
    def on_key(self, event):
        if event.key == ' ' :
            print ('you pressed space > new line')
            self.ind = self.ind + 1
            self.newline = True


            
#lb = LineBuilder()
#p = Picker()
#lsB = LinesBuilder()

plt.show()
