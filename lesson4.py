import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('original.csv')
df_c = df - df.mean()

print(df_c.head(3))
print(df_c.describe())

x = df_c['x']
y = df_c['y']



plt.scatter(x,y,label='y')

xx = x * x
xy = x * y

a = xy.sum() / xx.sum()
print(a)
plt.plot(x, a*x,label='y_hat',color='red')
plt.legend()
plt.show()


x_new = 40
mean = df.mean()
print(mean)
xc = x_new - mean['x'] # x - x_
print(xc)
yc = a*xc
print(a*xc) # a(x-x_)

#もとのスケールの予測値（センタリングの解除）
y_hat = yc + mean['y']
print(y_hat)


def predict(x):
    a = 10069.022519284063
    xm = 37.62222
    ym = 121065.0

    #中心化
    xc = x - xm
    y_hat = a * xc + ym

    return y_hat

print(predict(50))

