import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 100)
y =(1-x**2)**0.5

fig, ax = plt.subplots()
plt.plot(x,y, label='blue')
plt.plot(x, -y, label='orange')

plt.title('Table', fontsize=14, fontweight='bold')
plt.xlabel('x_label', c='orange', fontsize=14, rotation=20, loc='right')
plt.ylabel('y_label', c='b', fontsize=14, loc='top')
fig.autofmt_xdate()
# лучшее место loc='best'
plt.legend(ncol=3) # в строчку
# Метод xlim и метод ylim устанавливают начальное значение координатной оси
plt.xlim([-3, 3])
plt.ylim([-2, 2])
plt.axis('equal')

# скрыть ось координат
#plt.axis('off')

plt.show()