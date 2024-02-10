# 「N個のノード、N-1個のパス」&「すべてのノードを行き来可能」　=> 木構造

# 再帰回数上限。再帰関数を書くときは必ず最初に書くこと
import sys

sys.setrecursionlimit(10**6)

# 入力受け取り
N = int(input())

# 辺の情報格納
connect = [[] for i in range(N + 1)]

# 辺の情報受け取り
for i in range(N - 1):
    A, B = map(int, input().split())
    connect[A].append(B)
    connect[B].append(A)
# connect[1]=[2,3,4]ならば1と2,3,4がつながっている、というように確認できる

# 小さい順に回るからソート
for i in range(N + 1):
    connect[i].sort()

# 答えの格納リスト
ans = []


# DFS(今いる都市,前にいた都市)
def DFS(now, pre):
    # 今いる都市を答えに入れる
    ans.append(now)
    # to=今いる都市から行ける都市
    for to in connect[now]:
        # もしtoが前にいた都市と違うなら
        if to != pre:
            # 更に先へ探索する
            DFS(to, now)
            # 戻ってきたら答えへ格納
            ans.append(now)


# 最初の都市=1,前にいた都市=-1(前にいた都市がないので存在しない番号)としてスタート
DFS(1, -1)

# 答えの出力
print(*ans)
