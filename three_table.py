import matplotlib.pyplot as plt
import seaborn as sns


x = ['А', 'Б', 'В']
y = [10, 50, 30]


plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(x, y)
plt.subplot(132)
plt.scatter(x, y)
plt.subplot(133)
plt.plot(x, y)
plt.suptitle("Tables")


plt.savefig('tabels.png', bbox_inches='tight')