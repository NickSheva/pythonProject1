import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
cos, sin = np.cos(X), np.sin(X)

plt.plot(X, cos, c='b', label='cosine')
plt.plot(X, sin, c='r', label='sine')
plt.legend(loc='upper left', frameon=False)

plt.show()