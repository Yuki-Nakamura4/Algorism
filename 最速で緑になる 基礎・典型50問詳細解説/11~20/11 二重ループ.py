N = int(input())

x = []
y = []

for i in range(N):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)

import math

ans = 0

# 組み合わせを全探索
for i in range(N):
    for j in range(i+1, N):
        lenth = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
        ans = max(ans, lenth)

print(ans)
