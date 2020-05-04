import numpy as np
#ベクトルの定義
b = np.array([[1],[2],[3]])
print(b)

#行列の定義
X = np.array([[1,2],[3,4]])
print(X)

#転置
print(X.T)

#逆行列
# linear algebra:線形代数
X_inv = np.linalg.inv(X)
print(X_inv)

#行列積
XX_inv = np.dot(X, X_inv)
print(XX_inv)


## よくある間違い
a = np.array([[1],[2],[3]])
a = np.array([[1,2,3]])
print(a.T.T)

# Numpyでよく使う処理 大きさの取得
row, col = X.shape
print(row,col)

