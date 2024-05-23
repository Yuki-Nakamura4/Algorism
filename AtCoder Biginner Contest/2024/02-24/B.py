N = int(input())
P = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    A, B = map(int, input().split())
    ans = min(P.index(A), P.index(B))
    print(P[ans])


# 模範解答
# こちらの方が若干速い
N = int(input())
P = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    A, B = map(int, input().split())
    print(A if P.index(A) < P.index(B) else B)
