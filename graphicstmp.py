import matplotlib.pyplot as plt
import pandas as pd
table = pd.read_excel('data.xlsx')
x = table.values[:, 0]
y = table.values[:, 1]
plt.title('График температуры от времени')
plt.xlabel('Время')
plt.ylabel('Температура, *С')
plt.figure(figsize=(15, 7))
plt.plot(x, y)
plt.savefig("tmp.png")
