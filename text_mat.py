import matplotlib.pyplot as plt
# форматирование текста
fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
# установка заголовка для рисунка и графика соответственно
fig.suptitle('Заголовок рисунка', fontsize=14, fontweight='bold')
ax.set_title('Заголовок рисунка')

ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

# установка ограничений по осям x и y на [0, 10]
# вместо значения по умолчанию [0, 1]

ax.axis([0, 10, 0, 10])
ax.text(3, 8, 'Курсивный текст на плашке', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

ax.text(2, 6, r'Управнение: $E=mc^2$', fontsize=15)
ax.text(3, 2, 'Unicode: Institut fur Fdstkorperphysik')
ax.text(0.95, 0.01, 'Цветной текст', verticalalignment='bottom',
        horizontalalignment='right', transform=ax.transAxes,
        color= 'green', fontsize=15)

ax.plot([2], [1], 'o')
ax.annotate('Аннотация', xy= (2, 1), xytext=(3, 4), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()