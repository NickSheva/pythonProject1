import matplotlib.pyplot as plt
import pandas
import pandas as pd
import numpy as np
print(plt.style.available)
x = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]
n_x = x[1:-2] * 10
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()


plt.plot(n_x,  linewidth=3)
plt.title('Figure', fontsize=18)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Vlue', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.ylim(30,100)


plt.show()
