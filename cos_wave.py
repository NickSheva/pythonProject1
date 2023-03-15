import numpy as np
import matplotlib.pyplot as plt

time = np.arange(-3*np.pi, 3*np.pi, 0.01)
amplitude = np.cos(time)

plt.plot(time, amplitude)
plt.title('Cos wave', c='b', fontsize=20)

plt.xlabel('Time'+ r'$\rightarrow$', fontsize=14)
plt.ylabel('Cos(time)'+ r'$\rightarrow$', fontsize=14)

plt.grid()

plt.axhline(y=0, c='k')
plt.axvline(x=0, c='k')

plt.show()