import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)


# イェンセンの不等式をプロットする
### イェンセンの不等式で用いるf(x)を適当に定義
def f(x) :
    # return -x*x/5*3+5*x-5
    return np.log(x)

## パラメータを適当に決める
V = 3
split = 0.1

### phiを初期化したら区切り数で条件に揃える
phi = np.zeros(V)
for _ in np.arange(0, 1/split) :
    phi[np.random.randint(0,V)] += split

print("phi:"+str(phi))
print("sum phi:"+str(sum(phi)))

xmin = 1
xmax = 8

x_1 = 2
x_n = 4
x_vec = np.linspace(x_1,x_n, V)
y_vec = f(x_vec)
# データ点をプロット
plt.vlines(x_vec, 0, y_vec, "black", linestyle="dashed", label=r'$x_1,\cdots,x_'+str(V)+'$')
# データ点の始点と終点をつなぐ
plt.plot([x_vec[0],x_vec[-1]], [y_vec[0],y_vec[-1]], "black")

# 関数fを描画する範囲決定
x_list = np.arange(xmin,xmax,0.01)
y_list = f(x_list)
ymin = min(y_list)
ymax = max(y_list)

# 漸近線をプロット
plt.hlines([0], 0, xmax)
plt.vlines([0], 0, ymax)

# 関数fをプロット
plt.plot(x_list, y_list, color="blue", label=r'$f(x)$')


# イェンセンの不等式を確かめる
## 不等式の右辺を計算
phi = np.array(phi)
x_vec = np.array(x_vec)
num_right = sum(phi*np.array(f(x_vec)))
print("Inequality's right:"+str(num_right))

## 不等式の左辺を計算
num_left = f(sum(phi*np.array(x_vec)))
print("Inequality's  left:"+str(num_left))


# イェンセンの不等式をプロットする
x_jensen = np.dot(phi, x_vec)
plt.scatter(x_jensen, num_left, color="blue", label="Inequality's left")
plt.scatter(x_jensen, num_right, label="Inequality's right")


# 表示
plt.legend()
plt.show()
