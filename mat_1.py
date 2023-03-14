import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.style.use('seaborn-v0_8')
plt.plot(x, y, 'g', linewidth=3)
plt.savefig('saved_figure-100dpi.png', dpi = 100)

