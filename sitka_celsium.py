import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerow = next(reader)
    for index, column in enumerate(headerow):
        print(index, column)
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

# переводим градусы из Фаренгейтф в Цельсия
h_t = np.array(highs) # преобразуем список с помощью numpy
h_c = (h_t - 32) / 1.8
h = np.int_(h_c) # преобразуем float в int

l_m = np.array(lows)
l_c = (l_m - 32) / 1.8
l = np.int_(l_c)


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
plt.plot(dates, h, 'r', linewidth=0.9, alpha=0.5)
plt.plot(dates, l, 'b', linewidth=0.9, alpha=0.5)
plt.fill_between(dates, h, l, facecolor='blue', alpha=0.1)
plt.title('Daily high and low temperature -2018 SITKA', fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('TEMPERATURE(С)', fontsize=14)
plt.ylim(-9, 25)
plt.savefig('weather-sitka2018.png', facecolor='lightblue', dpi=100)