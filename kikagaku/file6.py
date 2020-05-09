#ハズレ値除去、3σ法

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv('housing.csv')

mean = df.mean()

col = 'x6'
print(mean[col])

# 標準偏差(standard deviation)
sigma = df.std()
print(sigma[col])

# μ(平均)±3σ => 99.7%のライン
low = mean[col] - 3 * sigma[col]
high = mean[col] + 3 * sigma[col]
print(low)
print(high)

df_3sigma = df[(df[col] > low) &(df[col] < high)]


print(len(df_3sigma),len(df))

# sns.distplot(df['x6'])

# sns.distplot(df_3sigma['x6'])

_df = df
cols = df.columns
for col in cols:
    low = mean[col] - 3*sigma[col]
    high = mean[col] + 3*sigma[col]
    _df = _df[(_df[col] > low) & (_df[col] < high)]

#original 506 => 415 3σ法でハズレ値除去
print(_df[col])

# サンプルが減る場合の対処法
# -外れ値を平均もしくは中央値などで埋める
# -外れ値を平均もしくは中央値などで埋める
# -主成分分析等を使って、潜在変数に変換したあとに3σを適用←高度
#　補足：正規分布になっているかどうかを判定した変数のみ使用する

###########################################
#  入力変数と出力変数に分割
###########################################

X = _df.iloc[:,:-1]
y = _df.iloc[:,-1]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# 重回帰分析
from sklearn.linear_model import LinearRegression

model = LinearRegression()

# モデルの学習
model.fit(X_train, y_train)

# 検証 ←検証データ
score = model.score(X_train, y_train)
print(score)

test = model.score(X_test, y_test)

print(test)

#############################################
#        スケーリング
#############################################

from sklearn.preprocessing import StandardScaler

# scalerの宣言
scaler = StandardScaler()
scaler.fit(X_train)
# scaling
X_train2 = scaler.transform(X_train)
print('X_train2', X_train2)
X_test2 = scaler.transform(X_test)
print('X_test2',X_test2)

# モデルの宣言
model = LinearRegression()

# モデルの学習
model.fit(X_train2, y_train)

# 検証
print(model.score(X_train2, y_train))
np.set_printoptions(precision=2,suppress=True)
print('model.coef_',model.coef_)

sns.distplot(_df['x13'])
plt.show()