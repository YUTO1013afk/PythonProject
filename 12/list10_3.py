import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x = np.random.randn(10000)

plt.hist(x,bins='auto')
plt.show()
