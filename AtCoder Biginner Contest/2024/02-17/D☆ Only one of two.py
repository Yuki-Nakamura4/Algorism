# 模範解答: 最初に二分探索をすると見通しが良くなる典型例
from math import lcm

N, M, K = map(int, input().split())
lo, hi = 0, 10**18
while lo + 1 < hi:
    mi = (lo + hi) // 2
    c = mi // N + mi // M - mi // lcm(N, M) * 2
    if c < K:
        lo = mi
    else:
        hi = mi
print(hi)

# これもTLEになる
# import math

# N, M, K = map(int, input().split())

# shou = K // (N+M-2)
# amari = K % (N+M-2)

# lcm = (N * M) // math.gcd(N, M)

# lcm * shou


# count = 0

# for o in range(lcm*shou, lcm*(shou+1)):
#     if o % N == 0 != o % M == 0:
#         count += 1
#         if count == amari:
#             print(o)


# TLEになる
# import heapq

# N, M, K = map(int, input().split())

# numlist= []
# heapq = []

# for i in range(1, N*K):
#     numlist.append(N * i)

# for i in range(1, M*K):
#     numlist.append(M * i)


# count = 0

# for item in numlist:
#     if numlist.count(item) == 1:
#         heapq.heappush(-(item))
#         count += 1
#         if count == K:
#             break

# ans = -(heapq.heappop())

# print(ans)
