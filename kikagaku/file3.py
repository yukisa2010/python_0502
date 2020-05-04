import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv('housing.csv')
# print(df.describe())
xxx = input('please input a variable: ')
sns.distplot(df[xxx])
# plt.show()

# correlation 相関係数
sns.pairplot(df)
plt.show()


