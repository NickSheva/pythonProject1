import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Shcmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.7,
        'Jerde_Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Trantow_Barrows': 123381.38,
        'White_Trantow': 135841.99,
        'Will LLC': 104437.60}

group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
def currency(x, pos):
        if x >= 1e6:
                s = '${:1.1f}M'.format(x*1e-6)
        else:
                s = '${:1.0f}K'.format(x*1e-3)
        return s
formatter = FuncFormatter(currency)


plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(4, 4))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
#fig.autofmt_xdate()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company', title='Company Revenue')
ax.xaxis.set_major_formatter(formatter)

ax.axvline(group_mean, ls='--', color='b')
plt.show()