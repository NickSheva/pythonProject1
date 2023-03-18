import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig, ax = plt.subplots()
ax = fig.add_subplot(projection='3d')

# создание данных
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

#построение поверхности
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

#настройка оси z
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# добавление легенды с цветами и их значениями
fig.colorbar(surf, shrink=0.5, aspect=5)

#plt.savefig('mplot3d.png', bbox_inches='tight', dpi=100)
plt.show()