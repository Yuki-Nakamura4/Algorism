import bisect

N, K = list(map(int, list(input().split())))
A = list(map(int, list(input().split())))

ok = bisect.biscet_left(A, K)

if ok == N:
    print(-1)
else:
    print(ok)
