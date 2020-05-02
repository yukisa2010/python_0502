import matplotlib.pyplot as plt
import pandas as pd

# 散布図をプロット

df = pd.read_csv('./original.csv')
x = df['x']
y = df['y']

plt.scatter(x,y)
plt.show()