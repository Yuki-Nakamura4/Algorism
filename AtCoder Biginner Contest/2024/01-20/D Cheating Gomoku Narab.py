H, W, K = map(int, input().split())

S = [input() for _ in range(H)]
INF = 10**9


def solve(a):
    # 行の長さがK未満の場合はINFを返す
    if len(a) < K:
        return INF
    o, x = 0, 0
    for i in range(K):
        if a[i] == "o":
            o += 1
        elif a[i] == "x":
            x += 1
    # xが1つもない場合は、K-oを返す
    ret = K - o if x == 0 else INF
    # 1つずつズラしながらK個目以降のoとxの数を数える
    for i in range(K, len(a)):
        if a[i - K] == "o":
            o -= 1
        elif a[i - K] == "x":
            x -= 1
        if a[i] == "o":
            o += 1
        elif a[i] == "x":
            x += 1
        ret = min(ret, K - o if x == 0 else INF)
    return ret


ans = min(solve(s) for s in S)

for i in range(W):
    t = [s[i] for s in S]  # 列を取り出す
    ans = min(ans, solve(t))

print(ans if ans < INF else -1)
