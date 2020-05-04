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

XTX = np.dot(X.T,X)

XTX_inv = np.linalg.inv(XTX)

Xy = np.dot(X.T, y)

w = np.dot(XTX_inv, Xy)


# w = (XtX)inv*X.T