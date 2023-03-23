import numpy as np
import matplotlib.pyplot as plt

labels= ['США', 'Тайвань', 'Северная Корея', 'Страны АСЕАН', 'Япония', 'Европейский союз',
         'Гонконг', 'Индия', 'Россия', 'Бразилия']
sizes = [22, 2, 5, 11, 10, 24, 18, 3, 3, 2]
explode = [0.1, 0.1, 0.1, 0.1, 0.3,  0.1, 0.1, 0.2, 0.2, 0.1]
colors = ['wheat', 'lavender', 'lightblue', 'blue', 'cyan', 'lightgreen', 'white', 'lightgray', 'yellow', 'purple']
# wedgeprops=dict(width=0.6) круг в нутри
# wedgeprops={'lw':0.2, 'ls':'-','edgecolor':"k"
wedge_props = {'linewidth': 2, 'edgecolor': 'gray'}
text_props = {'weight': 'bold'}
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, explode=explode, shadow=True, autopct='%1.f%%', colors=colors,
       startangle=180,  wedgeprops=wedge_props, textprops=text_props) # rotatelabels=True,
ax.set_title('Экспорт Китая', fontweight='bold')

ax.axis('equal')
plt.show()
