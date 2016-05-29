import matplotlib.pyplot as plt

class CLBuilder: # circles + lines
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_title('circles and lines')
        self.lines = []
        #self.circles = []
        self.ind = 0
        self.xs = []
        self.ys = []
        self.newline = True
        #
        self.touched_circle = None
        self.click_cid = self.fig.canvas.mpl_connect('button_press_event', self.click_event)
        self.key_cid = self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        #self.cid_pick = self.fig.canvas.mpl_connect('pick_event', self.pick_event)        
        #self.cid_move = self.fig.canvas.mpl_connect('motion_notify_event', self.motion_event)
        #self.cid_release = self.fig.canvas.mpl_connect('button_release_event', self.release_event)


    def click_event(self, event):
        print('click', event.xdata, event.ydata)
        #if event.inaxes!=self.line.ax: return
        if event.button != 1:
            return
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
        
        c_id = plt.Circle((event.xdata, event.ydata), radius=0.5)
        #print ' circle', c_id
        #self.circles.append(c_id) # tengo los circulos guardados con su id
        self.ax.add_artist(c_id)
        
        self.fig.canvas.draw()
    
    def on_key(self, event):
        if event.key == ' ' :
            print ('you pressed space > new line')
            self.ind = self.ind + 1
            self.newline = True
    
    '''
    def motion_event(self, event):
        if self.touched_circle == None:
            return
        if event.inaxes == self.ax:
            dx = event.xdata - self.initial_event.xdata
            dy = event.ydata - self.initial_event.ydata
            self.touched_circle.center = self.x0 + dx, self.y0 + dy
            centers = map(lambda x: x.center, self.ax.artists)
            #self.line.set_data(*zip(*centers))
            self.fig.canvas.draw()

    def release_event(self, event):
        self.touched_circle = None

    def pick_event(self, event):
        self.initial_event = event.mouseevent
        if event.mouseevent.button != 3:
            return
        self.touched_circle = event.artist
        print 'touched: ', self.touched_circle
        self.x0 = event.mouseevent.xdata
        self.y0 = event.mouseevent.ydata
    '''

cl = CLBuilder()
##
plt.show()
