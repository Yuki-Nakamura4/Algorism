import sys

sys.setrecursionlimit(10**7)

N = int(input())

graph = [[] for _ in range(N)]

for i in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


# その要素の子の合計(+自分自身)を数える関数
def dfs(v, p=0):
    res = 1
    for nv in graph[v]:
        if nv == p:
            continue
        res += dfs(nv, v)
    return res


ans = []

for i in graph[0]:
    ans.append(dfs(i))

ans.sort()

# ansの要素のうち最大を除く合計+最後に消す自身を足して出力
print(sum(ans[:-1]) + 1)
