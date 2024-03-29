# 再帰上限を増やす
import sys

sys.setrecursionlimit(1000000)

# 入力
N = int(input())
# child[i]: 頂点iの子(部下)となる頂点たち
child = []
for i in range(N):
    child.append([])
for i in range(1, N):
    b = int(input())
    # b-1番目の頂点がi番目の頂点の親であることを示し、
    # i番目の頂点がb-1番目の頂点の子であることを示している
    child[b - 1].append(i)


# 再帰関数を定義する
# dfs(i): 頂点iをの子の給料をすべて求め、自身の給料を計算して返す
def dfs(i):
    # 子がいない場合、給料は1
    if len(child[i]) == 0:
        return 1
    else:
        values = []
        for j in child[i]:
            values.append(dfs(j))
        return max(values) + min(values) + 1


# 　答えは頂点0の給料
print(dfs(0))
