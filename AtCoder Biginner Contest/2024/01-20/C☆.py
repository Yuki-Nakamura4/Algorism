N = int(input())
A = list(map(int, input().split()))

x = 0  # いちばん最初の人の番号。初期値は0
back = [0] * (N + 1)  # b[i] = i番目の人の後ろにいる人の番号
for i in range(N):
    if A[i] == -1:
        x = i + 1
    else:
        back[A[i]] = i + 1

ans = [x]
for _ in range(N - 1):
    x = back[x]
    ans.append(x)
print(*ans)
