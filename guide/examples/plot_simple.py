"""
A simple example
=================

"""

import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 100)
Y = np.sin(X)

plt.plot(X, Y, linewidth=2)
plt.show()
