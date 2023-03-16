import matplotlib.pyplot as plt
import numpy as np

#plt.plot([1, 2, 3, 4], [1, 4, 9, 19], 'bo')
#plt.axis([0, 5, 0, 20])
#plt.show()

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'dr:', t, t**2, 'bs', t, t**3, 'g^')
plt.show()