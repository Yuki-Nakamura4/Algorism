N = int(input())

# A[i] + B[i]の大きい順位でソートする
arr = []
for i in range(N):
    a, b = map(int, input().split())
    # -A[i] - B[i]を先頭に入れておくことで、昇順にしたときA[i] + B[i]の大きい順になる
    arr.append([-a - b, a, b])

arr.sort()
ans = 0

for i in range(N):
    c, a, b = arr[i]
    if i % 2 == 0:
        ans += a
    else:
        ans -= b

print(ans)
