import matplotlib.pyplot as plt
import numpy as np

paint = np.linspace(0, 2 * np.pi, 100)

x = 16 * (np.sin(paint) ** 3)
y = 13 * np.cos(paint) - 5 * np.cos(2*paint) - 2 * np.cos(3*paint) - np.cos(4*paint)
plt.plot(x, y, c='red', linewidth=10)
plt.title('Heart')
plt.show()