N, K = map(int, input().split())
A = list(map(int, input().split()))

ok = N
ng = -1

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if A[mid] >= K:
        ok = mid
    else:
        ng = mid

# 条件を満たす要素が存在しない場合はokが初期値のままとなるため、-1を出力
if ok == N:
    print(-1)
else:
    print(ok)

# 二分探索を用いた解法が成立するためには、今回の問題のように
# 探索対象の数列などがどこかを境界として条件を満たす領域と満たさない領域に二分される
# という性質を持っている必要がある。
# このような性質を単調性と呼ぶ。
# ほとんどの場合、単調性を持つ数列はソートされている。
