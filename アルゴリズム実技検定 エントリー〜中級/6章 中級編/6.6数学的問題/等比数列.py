def solve(A, R, N):
    # R-1のとき、Nの値を無視してAを返す
    if R == 1:
        return A

    # AにRをN-1回かける
    for _ in range(N - 1):
        A *= R

        # Aが10**9を超えたら途中で　終了して"large"を返す
        if A > 10**9:
            return "large"

    return A


A, R, N = map(int, input().split())

ans = solve(A, R, N)
print(ans)
