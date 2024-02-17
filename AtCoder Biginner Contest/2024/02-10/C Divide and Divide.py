# 模範解答
from functools import cache


# メモ化再帰: 一度計算した結果を保存しておくことで、同じ計算を繰り返さないようにする
@cache
def f(n):
    if n < 2:
        return 0
    return n + f(n // 2) + f((n + 1) // 2)


N = int(input())
print(f(N))
