#seabornの使い方、訓練用・テストデータの分解

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv('housing.csv')

X = df.iloc[:,0:-1]
y = df.iloc[:,-1]

# モデル構築
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X,y)

score = model.score(X,y)
print(score)

#訓練用データ(train)と検証用データ(test)

from sklearn.model_selection import train_test_split

# 分割
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1) #random_stateは乱数のシードを固定

#モデルの学習
model.fit(X_train, y_train)
#検証←検証データ
test = model.score(X_test,y_test)
print(test)



