import numpy as np

x = np.array([1,2,3])
y = np.array([2, 3.9, 6.1])
xc = x - x.mean()
yc = y - y.mean()

xx = xc * xc 
print(xx, 'xx')
xy = xc * yc
print(xy)

print('a')
a = xy.sum() / xx.sum()
print(a)