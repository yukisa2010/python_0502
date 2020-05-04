import numpy as np

X = np.array([
    [1,2,3],
    [1,2,5],
    [1,3,4],
    [1,5,9]
])

y = np.array([
    [1],
    [5],
    [6],
    [8]
])

# Step1
XtX = np.dot(X.T, X)

#Step2
XtX_inv = np.linalg.inv(XtX)

#Step3
Xty = np.dot(X.T, y)

#Step4
w = np.dot(XtX_inv, Xty)

print(w)

#########################################
# 重回帰分析のみ読み込み
#########################################

from sklearn.linear_model import LinearRegression

# モデルの宣言 => 重回帰分析
model = LinearRegression()

# モデルの学習←パラメータの調整
model.fit(X,y)

# w(係数)
print('w(係数)')
print(model.coef_)

# 接点（1を置く必要なし）
print('接点')
print(model.intercept_)

# 予測精度
print('予測精度')
print(model.score(X,y))

# 予測値
x = np.array([[1,2,3]])
print('xの値[1,2,3]の予測値')
print(model.predict(x))

