import numpy as np
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('default')

np.random.seed(19680801)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(437)
num_bins = 50
fig, ax = plt.subplots()
# гистограмма
n, bins, patches = ax.hist(x, 50, density=1, facecolor='g', alpha=0.35)
# добавление кривой распределенмя
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
ax.plot(bins, y, '--')



plt.xlabel('Smarts')
plt.ylabel('Probability density')
plt.title(r'Histogrom of IQ')
#fig.tight_layout()

plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.grid(True)

plt.show()