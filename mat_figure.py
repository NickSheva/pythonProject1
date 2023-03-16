import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 18, 0.03)
s = np.sin(x)
c = np.cos(x)

fig, ax = plt.subplots()
plt.plot(x, s, 'c', label='sin_x', linewidth=1)
plt.plot(x, c, 'bo', label='cos_x', linewidth=3)
plt.fill_between(x,s, facecolor='blue', alpha=0.2)
plt.fill_between(x,c, facecolor='blue')
fig.legend()
plt.title('FIGURE')
plt.xlabel('x_label')
plt.ylabel('y_label')

plt.savefig('saved_figure.png',  bbox_inches='tight', facecolor='lightblue')




