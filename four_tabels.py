import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, ax = plt.subplots(2, 2, figsize=(5, 5))
ax[0, 0].hist(data[0])
ax[1, 0].scatter(data[0], data[1])
ax[0, 1].plot(data[0], data[1])
ax[1, 1].hist2d(data[0], data[1])

plt.show()