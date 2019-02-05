# jensens_inequality
イェンセンの不等式を式だけではなく図解できるようにプロットした

## イェンセンの不等式(Jensen's inequality)

機械学習分野でよく出てくる．

トピックモデルや行列因子分解(Non-negative Matrix Factorization)の補助関数法の基本的なアプローチである．

### 数式

```math
\phi_1, \cdots, \phi_v, \cdots \phi_V \ge 0, \quad
\sum_{v=1}^{V} \phi_v = 1
```

を満たし， $`f(x)`$ が上に凸な関数であるとき，

```math
f \left( \sum_{v=1}^{V} \phi_v x_v \right) \ge \sum_{v=1}^{V} \phi_v f \left( x_v \right)
```

が成り立つ．
