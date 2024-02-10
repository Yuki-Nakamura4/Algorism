N, K = map(int, input().split())
h = list(map(int, input().split()))

# cost[i]: 足場iに辿り着くまでの最小コスト。
# N個の足場それぞれのコストを調べたいので、N個の要素を持つリストを作る。
cost = [float("inf")] * N
# float("inf")はPythonで無限大を表現するための一般的な方法
# 最小値を見つけるためのアルゴリズムでは、最初に最小値をfloat("inf")として設定し、その後で見つけた値と比較していく

# 初期条件
cost[0] = 0

# それ以降の足場はジャンプ元が複数通りあるため、コストが小さいものを選ぶ
for i in range(1, N):
    for j in range(1, min(i, K) + 1):
        cost[i] = min(cost[i], cost[i - j] + abs(h[i] - h[i - j]))

# 答えは最後の足場までの最小コスト
print(cost[N - 1])
