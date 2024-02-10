A, B, X = map(int, list(input().split()))

ok = 0
ng = 10**9 + 1

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    d = len(str(mid))
    price = A
    if price <= X:
        ok = mid
    else:
        ng = mid

print(ok)
