import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi,50)
y = np.tan(x)

plt.plot(x, y)
plt.show()