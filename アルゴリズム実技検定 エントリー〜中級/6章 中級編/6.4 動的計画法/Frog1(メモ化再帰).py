# Frog1をメモ化再帰で解く
import sys

sys.setrecursionlimit(1000000)

N = int(input())
h = list(map(int, input().split()))

# cost[i]: 足場iに辿り着くまでの最小コスト。
cost = [0] * N

# done[i]: cost[i]がすでに計算済みであることを示すフラグ
done = [False] * N


# メモ化再帰の実装
def rect(i):
    # 計算済みであれば即座に値を返す
    if done[i]:
        return cost[i]
    # そうでなければ値を計算する
    if i == 0:
        cost[i] = 0
    elif i == 1:
        cost[i] = rect(0) + abs(h[0] - h[1])
    else:
        cost[i] = min(
            rect(i - 1) + abs(h[i - 1] - h[i]), rect(i - 2) + abs(h[i - 2] - h[i])
        )
    # 計算済みフラグを立てて値を返す
    done[i] = True
    return cost[i]


# 答えは足場N-1までの最小コスト
print(rect(N - 1))
