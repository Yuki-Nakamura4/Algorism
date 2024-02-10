N, M = list(map(int, input().split()))
# 1始まりにするダミーを入れる。Sは整数に直す
S = [0]
C = [0]
for i in range(M):
    s, c = input().split()
    s_val = 0
    for j in range(N):
        if s[j] == "Y":
            s_val |= 1 << j
    S.append(s_val)
    C.append(int(c))

# 集合としてあり得るものの個数。2**Nでも同じ。
ALL = 1 << N

# cost[i][n]:セットiまで見て揃った部品の集合がnのときの最小コスト
cost = []
INF = 10**100
for i in range(M + 1):
    cost.append([INF] * ALL)

# 初期条件
cost[0][0] = 0

# iが小さいところから順に計算
for i in range(1, M + 1):
    for n in range(ALL):
        # セットiを買わない
        cost[i][n] = min(cost[i][n], cost[i - 1][n])
        # セットiを買う
        cost[i][n | S[i]] = min(cost[i][n | S[i]], cost[i - 1][n] + C[i])

# 答えは全部揃っている状態の最小コスト
# ただし、INFのままなら部品を揃えることは不可能
# ALL-1の理由
# 例えば、部品が3つある場合、ALLは1 << 3 = 8となるが、これをビットで表すと1000となる。
# しかし、部品が全て揃っている状態は111(= 7)なので、ALL-1が全ての部品が揃っている状態を表すことになる。
ans = cost[M][ALL - 1]
if ans == INF:
    ans = -1

print(ans)
