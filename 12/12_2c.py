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

data = [{'x': x, 'y': y1, 'title': 'y=sin(x)', 'xticks': xpositions,
         'xticklabels': xlabels, 'color': 'r', 'ylim': [-1.2, 1.2]},
        {'x': x, 'y': y2, 'title': 'y=cos(x)', 'xticks': xpositions,
         'xticklabels': xlabels, 'color': 'b', 'ylim': [-1.2, 1.2]},
        {'x': x, 'y': y3, 'title': 'y=tan(x)', 'xticks': xpositions,
         'xticklabels': xlabels, 'color': 'g', 'ylim': [-1.2, 1.2]}
        ]

for i, value in enumerate(data):
    fsub = fig.add_subplot(1, len(data), i+1)
    fsub.set_title(value['title'])
    fsub.grid(True)
    fsub.set_xticks(value['xticks'])
    fsub.set_xticklabels(value['xticklabels'])
    fsub.plot(value['x'], value['y'],
              color=value['color'], label=value['title'])
    fsub.set_ylim(value['ylim'])

plt.show()
