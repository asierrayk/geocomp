import numpy as np
import matplotlib.pyplot as plt


# Examples (plt.subplots):
plt.close('all')


#plt.subplots(2, 3, 'all', 'all')

figure, axes = plt.subplots(figsize=(10, 10))
axes.set_xlim(-10, 10)
figure.canvas.draw() # no se que es esto

x = np.linspace(-10, 10, 100)
y = np.cos(x)
axes.plot(x, y)
figure.canvas.draw()


def on_press(event):
    print 'Ouch!'
    print event

def on_press2(event):
    c = plt.Circle((event.xdata, event.ydata), radius=0.1)
    axes.add_artist(c)
    figure.canvas.draw()

cid_press = figure.canvas.mpl_connect('button_press_event', on_press2)
#figure.canvas.mpl_disconnect(cid_press)


plt.show()
