import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv('housing.csv')

X = df.iloc[:,0:-1]
y = df.iloc[:,-1]


x = df.iloc[0,:-1]
# モデル構築
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X,y)

from sklearn.externals import joblib

# joblib.dump(model, "model.pkl")
model_new = joblib.load('model.pkl')
print(x)
print(model_new.predict([x]))


#パラメータの確認(w)
np.set_printoptions(precision=3,suppress=True)
print(model.coef_)

# xがそもそも桁数バラバラ・・・
# 重みを見るだけでは、どの変数が影響を与えているのか分からない。
# => file6.pyへ
