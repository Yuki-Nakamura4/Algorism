# 巡回セールスマン問題

N = int(input())

A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

# どの都市に訪れてどの都市に訪れていないかを表す集合の個数
ALL = 1 << N

# cost[i][j]:訪れた都市の集合がnで、最後に都市iにいるときのコストの最小値
cost = []
for n in range(ALL):
    cost.append([10**100] * N)

# 初期条件。最初にいるときの始点はnに含めない
cost[0][0] = 0


# nで表現される集合に要素iが含まれるかどうかを判定してTrue/Falseを返す関数
def has_bit(n, i):
    return n & (1 << i) > 0


for n in range(ALL):  # すべての集合について
    for i in range(N):
        # iからjに移動する遷移を試す
        for j in range(N):
            # すでに訪問済みか、同じ都市ならスキップ
            if has_bit(n, j) or i == j:
                continue
            cost[i | (1 << j)][j] = min(cost[i | (1 << j)][j], cost[i][j] + A[i][j])

# 全都市を訪れて戻ってくる最小コストが答え
print(cost[ALL - 1][0])
