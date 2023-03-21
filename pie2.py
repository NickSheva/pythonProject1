import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

size = 0.3
vals = np.array([[90, 43], [57, 60],
                 [92, 20]])

cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(3) * 4)
mid_colors = cmap(np.array([1, 2, 3, 4, 5, ]))
inner_colors = cmap(np.array([4, 12, 5,
                              6, 9, 10]))

ax.pie(vals.sum(axis=1), radius=1,
       colors=outer_colors,
       wedgeprops=dict(width=size,
                       edgecolor='w'))

ax.pie(vals.flatten(), radius=1 - size,
       colors=mid_colors,
       wedgeprops=dict(width=size,
                       edgecolor='w'))

ax.pie(vals.flatten(), radius=1 - 2 * size,
       colors=inner_colors,
       wedgeprops=dict(width=size,
                       edgecolor='w'))

ax.set_title('matplotlib.axes.Axes.pie Example')
plt.show()