import numpy as np
import matplotlib.pyplot as plt

time = np.arange(-3*np.pi, 3*np.pi, 0.01)
amplitide = np.sin(time)
plt.plot(time, amplitide)
# Настройка заголовкф для грфика размер и цвет
plt.title('Sine wave', fontsize=20, c='b')
plt.xlabel('Time'+ r'$\rightarrow$', fontsize=14, c='g')
plt.ylabel('Sin(time)'+ r'$\rightarrow$', fontsize=14, c='g')
# вывод сетки
plt.grid()
# выделения oceй при x=0 и y=0
plt.axhline(y=0, c='k')
plt.axvline(x=0, c='k')
plt.savefig('sine_wave.png', bbox_inches='tight', dpi=90)