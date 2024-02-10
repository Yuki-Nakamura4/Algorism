N = int(input())
h = list(map(int, input().split()))

# cost[i]: 足場iに辿り着くまでの最小コスト。
# N個の足場それぞれのコストを調べたいので、N個の要素を持つリストを作る。
cost = [0] * N

# 初期条件
cost[0] = 0
# 2つ目の足場はジャンプ元が1通り
cost[1] = cost[0] + abs(h[0] - h[1])  # absは絶対値を求める関数
# それ以降の足場はジャンプ元が2通りあるため、コストが小さい方を選ぶ
for i in range(2, N):
    cost[i] = min(
        cost[i - 1] + abs(h[i - 1] - h[i]), cost[i - 2] + abs(h[i - 2] - h[i])
    )

# 答えは最後の足場までの最小コスト
print(cost[N - 1])
