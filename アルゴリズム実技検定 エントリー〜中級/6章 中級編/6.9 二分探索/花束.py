R, B = map(int, input().split())
x, y = map(int, input().split())


def check(X):
    # 2種類の花に共通する赤1本と青1本の花をX個分確保する
    r = R - X
    b = B - X
    # この時点で確保できない場合は不可能
    if r < 0 or b < 0:
        return False
    # 残った花を使って、それぞれの花束ごとに追加で必要な花を分配する
    num = r // (x - 1) + b // (y - 1)
    # 必要な花束の個数よりも確保できる花束の個数が多い場合は可能
    return num >= X


ok = 0
# ngは絶対に不可能な値にしたいので、花1種類の本数の最大値+1にしておく
ng = 10**18 + 1


while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
