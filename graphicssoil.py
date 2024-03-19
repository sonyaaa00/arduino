import matplotlib.pyplot as plt
import pandas as pd
table = pd.read_excel('data.xlsx')
x = table.values[:, 0]
y = table.values[:, 2]
plt.title('График влажности почвы от времени')
plt.xlabel('Время')
plt.ylabel('Влажность, %')
plt.figure(figsize=(15, 7))
plt.plot(x, y)
plt.show()