import matplotlib.pyplot as plt
import numpy as np

year = [1950, 1975, 2000, 2018, 2022]
population = [2.12, 3.681, 5.312, 6.981, 8.0324]
fig, ax = plt.subplots(figsize=(5,5))
plt.plot(year, population, ls='--', lw=5)


plt.title('World Pupulation')
plt.yticks([0, 2, 4, 6, 8, 10])
plt.grid()
plt.show()