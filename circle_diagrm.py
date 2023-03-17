import matplotlib.pyplot as plt

# круговая диаграмма со срезами против чавовой стрелки
labels = 'Турецкая лира (TRL) ', 'Венгерский форинт (HUF)', 'Японская иена (JPY)','Южноафриканский рэнд (ZAR)','Шведская крона (SEK)'
sizes = [33.26, 23.29, 17.73, 12.25, 18.72]
explode = (0.1, 0, 0, 0, 0) # сместить только 2-й срез ('hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, autopct='%1.1f%%', labels=labels, shadow=True, startangle=90)

plt.title('Рейтинг снижение валют к рублю за 2023 год', fontsize=14)

ax1.axis('equal')  # равное соотношение гарантирует, что диаграмма будет в виде круга
plt.show()