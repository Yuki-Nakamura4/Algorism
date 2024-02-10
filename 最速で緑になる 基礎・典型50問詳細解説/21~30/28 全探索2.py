# 入力の受け取り
N, X = list(map(int, input().split()))

# L,aの格納リスト
L = []
a = []

# N回
for i in range(N):
    # 一旦リストで受け取り
    tmp = list(map(int, input().split()))
    # リストの0番目=L
    L.append(tmp[0])
    # リストの1番目~=a
    a.append(tmp[1:])

# 全ての掛け算パターンの結果
Pro = [1]

# i=0~(N-1)
for i in range(N):
    # 一時的に結果を格納するリスト
    tmpPro = []

    # i番目の袋のa全てについて
    for ai in a[i]:
        # ここまでの全ての掛け算パターンの結果
        for p in Pro:
            # 掛け算して格納
            tmpPro.append(ai * p)

    # ProをtmpProで更新
    Pro = tmpPro

# 結果がXとなったパターンを数える
ans = Pro.count(X)

# 答えを出力
print(ans)
