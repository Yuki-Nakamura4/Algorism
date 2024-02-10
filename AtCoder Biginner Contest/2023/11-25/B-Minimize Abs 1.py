N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = []

for i in range(N):
    if A[i] <= L:
        ans.append(L)
    elif A[i] >= R:
        ans.append(R)
    elif L < A[i] < R:
        ans.append(A[i])

# 「*」を使うと、リストの中身を展開して出力してくれる
print(*ans)

# 模範解答
N, L, R = map(int, input().split())
A = list(map(int, input().split()))

for x in A:
    if A[i] <= L:
        print(L, end=" ")
    elif A[i] >= R:
        print(R, end=" ")
    elif L < A[i] < R:
        print(A[i], end=" ")
