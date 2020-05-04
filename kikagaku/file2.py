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


# 重回帰分析のみ読み込み
from sklearn.linear_model import LinearRegression

# モデルの宣言
model = LinearRegression()
# モデルの学習←パラメータの調整
model.fit(X,y)

print(model.coef_)

print(model.intercept_)

print(model.score(X,y))

x = np.array([[1,2,3]])
print(model.predict(x))