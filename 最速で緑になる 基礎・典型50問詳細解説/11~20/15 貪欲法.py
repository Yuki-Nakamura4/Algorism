N, W = map(int, input().split())

Cheese = []

for i in range(N):
    A, B = map(int, input().split())
    Cheese.append([A, B])

# 1gあたりのおいしさが大きい順にソート
Cheese.sort(reverse=True)

ans = 0

cheese_weight = 0

for i in range(N):
    if cheese_weight + Cheese[i][1] <= W:
        ans += Cheese[i][0] * Cheese[i][1]
        cheese_weight += Cheese[i][1]
    else:
        ans += Cheese[i][0] * (W - cheese_weight)
        break

print(ans)
