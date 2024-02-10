# リストを使うとややこしいが、連想配列を使うと簡単になることがある

N = int(input())

# 座標の格納用リスト
points = []

# defaultdictを用意 初期値は0
# defaultdfictは存在しないキーを指定したときに自動で初期値を設定してくれる
# そのため、キーが存在するかを毎回確認する必要がない
from collections import defaultdict

# (x,y)が存在したらp[(x,y)]=1
p = defaultdict(int)

for i in range(N):
    x, y = map(int, input().split())
    # 座標をpointsへ格納
    points.append([x, y])
    # p[(x,y)]=1を記録
    p[(x, y)] = 1

ans = 0

for p1 in range(N):
    # p2=(p1+1)~(N-1)
    for p2 in range(p1 + 1, N):
        # p1のx座標,y座標
        p1_x, p1_y = points[p1]
        # p1のx座標,y座標
        p2_x, p2_y = points[p2]

        # x座標またはy座標が同じ場合は次の座標へ
        if p1_x == p2_x or p1_y == p2_y:
            continue
        # 座標(p1_x,p2_y)と座標(p2_x,p1_y)の点が存在すれば
        if p[(p1_x, p2_y)] == 1 and p[(p2_x, p1_y)] == 1:
            ans += 1

# 二重に数えているので2で割る
ans //= 2

print(ans)
