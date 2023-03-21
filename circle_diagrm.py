import matplotlib.pyplot as plt
import numpy as np

labels = ['Rolex', 'Omege', 'Longines', 'Patek Philippe', 'Cartier', 'Audemars Piguet', 'Tissot', 'TAG Heuer', 'IWC',
          'Jaeger_LeCultre', 'Hublot', 'Vacheron Constantin', 'Breetling', 'Officine Panerai', 'Richard Mile',
          'Breguet', 'Others']
sizes = [23.4, 8.5, 6.6, 6.1, 5.5, 3.4, 4.0, 3.4, 3.2, 2.6, 2.6, 2.2, 1.8, 1.9, 1.8, 1.7, 21.3]
explode = [0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # сместить только первый срез('Rolex')

colors = ['lightblue', 'lightgreen', 'orange', 'cyan', 'gray', 'darkred', 'beige', 'darkblue', 'indigo', 'blue', 'white',
           'g', 'r', 'c', 'm', 'y', 'burlywood', 'w', 'h']
#colors = ['tab:blue', 'tab:cyan', 'tab:gray', 'tab:green', 'tab:red', 'tab:orange', 'tab:"indigo"']
fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=120, colors=colors)
ax.set_title('SWISS WATCHS: RETAIL MARKET SHARES BY BRAND IN 2019', fontsize=12, fontweight='bold')
#ax.set_title('', fontsize=12, fontweight='bold')
plt.legend(bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
           loc = "center left", labels = labels)
ax.axis('equal')

plt.show()
