import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)


xlabels = ['0°', '90°', '180°', '270°', '360°']
xpositions = [0, np.pi/2, np.pi, np.pi*3/2, np.pi*2]

ylabels = ['-1.0', '-0.5', '0', '0.5', '1.0']
ypositions = [-1, -0.5, 0, 0.5, 1]

fig = plt.figure(figsize=(8, 2))

plt.subplots_adjust(wspace=0.5, hspace=1)

f1 = fig.add_subplot(1, 3, 1,title='y=sin(x)',xticks=xpositions,xticklabels=xlabels)
f1.grid(True)
f1.plot(x, y1, color='r', label='y=sin(x)')
f1.set_ylim([-1.2, 1.2])

f2 = fig.add_subplot(1, 3, 2,title='y=cos(x)',xticks=xpositions,xticklabels=xlabels)
f2.grid(True)
f2.plot(x, y2, color='b', label='y=cos(x)')
f2.set_ylim([-1.2, 1.2])

f3 = fig.add_subplot(1, 3, 3,title='y=tan(x)',xticks=xpositions,xticklabels=xlabels)
f3.grid(True)
f3.plot(x, y3, color='g', label='y=tan(x)')
f3.set_ylim([-1.2, 1.2])

plt.show()
