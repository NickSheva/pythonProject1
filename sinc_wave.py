import numpy as np
import matplotlib.pyplot as plt

time = np.arange(-2*np.pi, 2*np.pi, 0.01)
amplitude = np.sinc(time)

plt.plot(time, amplitude, linewidth=2)

plt.title('Sinc wave', fontsize=24, c='b')
plt.xlabel('Time'+ r'$\rightarrow$')
plt.ylabel('Sinc(time)'+ r'$\rightarrow$')

plt.grid()

plt.axhline(y=0, c='k')
plt.axvline(x=0, c='k')
plt.show()