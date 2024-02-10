# 部分和問題

N = int(input())

# 1始まりにするため先頭にダミーを入れる
ps = [0] + list(map(int, input().split()))

p = sum(ps)

# exist[i][j]:i番目までの問題を解いて、得点がs点になるような組み合わせが存在するかどうか
exist = []
for i in range(N + 1):
    exist.append([False] * (p + 1))

# 初期条件
exist[0][0] = True

# iが小さい順に求めていく
for i in range(1, N + 1):
    for s in range(p + 1):
        # 問題iを解かない場合
        exist[i][s] = exist[i][s] or exist[i - 1][s]
        # 問題iを解く場合
        if s - ps[i] >= 0:
            exist[i][s] = exist[i][s] or exist[i - 1][s - ps[i]]

# 答えはexist[N][s]のなかでTrueになっているsの個数
ans = 0
for s in range(p + 1):
    if exist[N][s]:
        ans += 1

print(ans)
