import matplotlib.pyplot as plt
import pandas as pd
table = pd.read_excel('data.xlsx')
x = table.values[:, 0]
y = table.values[:, 2]
plt.title('График интенсивности света от времени')
plt.xlabel('Время')
plt.ylabel('Интенсивность света, %')
plt.figure(figsize=(15, 7))
plt.plot(x, y)
plt.show()