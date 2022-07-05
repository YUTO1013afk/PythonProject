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


plt.title('graph of trigonometric functions')

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.grid(True)

plt.xticks(xpositions, xlabels)
plt.yticks(ypositions, ylabels)

plt.plot(x, y1, color='r', label='y=sin(x)')
plt.plot(x, y2, color='b', label='y=cos(x)')
plt.plot(x, y3, color='g', label='y=tan(x)')

plt.legend(['y=sin(x)', 'y=cos(x)', 'y=tan(x)'])


plt.ylim([-1.2, 1.2])

plt.show()
